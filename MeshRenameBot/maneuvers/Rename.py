import asyncio
import logging
import time
import os
import aiofiles.os as aos

from aiofiles import os as aos
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import Client, StopTransmission
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types.messages_and_media.message_entity import MessageEntity
from pyrogram.errors import ThumbnailFileInvalid
from MeshRenameBot.utils.user_input import userin

from ..core.get_config import get_var
from ..core.thumb_manage import get_thumbnail, resize_img
from ..database.user_db import UserDB
from ..maneuvers.ExecutorManager import ExecutorManager
from ..mesh_bot import MeshRenameBot
from ..translations import Translator
from ..utils.c_filter import FilterUtils
from ..utils.progress_for_pyro import progress_for_pyrogram
from .Default import DefaultManeuver

renamelog = logging.getLogger(__name__)


class RenameManeuver(DefaultManeuver):
    def __init__(
        self, client: MeshRenameBot, media_message: Message, cmd_message: Message
    ) -> None:
        super().__init__(client, media_message, cmd_message)
        self._unique_id = int(str(cmd_message.chat.id) + str(cmd_message.id))
        self._fltr_obj = FilterUtils(cmd_message.from_user.id)
        self.user_msg = cmd_message
        self._original_thumb = None

    async def _preserve_original_thumb(self):
        """Extract original thumbnail before download if available"""
        if self._media_message.video and self._media_message.video.thumbs:
            self._original_thumb = self._media_message.video.thumbs[0]
        elif self._media_message.document and self._media_message.document.thumbs:
            self._original_thumb = self._media_message.document.thumbs[0]

    async def _get_thumbnail_path(self, dl_path: str, user_id: int, is_force: bool) -> str:
        """Handle thumbnail generation with original thumb priority"""
        try:
            if self._original_thumb:
                thumb_path = await self._client.download_media(self._original_thumb.file_id)
                if await aos.path.getsize(thumb_path) > 200 * 1024:  # Telegram's limit
                    thumb_path = await resize_img(thumb_path, 320)
                return thumb_path
            return await get_thumbnail(dl_path, user_id, is_force)
        except Exception as e:
            renamelog.warning(f"Thumbnail generation failed: {e}")
            return None

    async def execute(self) -> None:
        self._execute_pending = False
        user_id = self._cmd_message.from_user.id
        user_locale = UserDB().get_var("locale", user_id)
        translator = Translator(user_locale)

        if self._media_message is None or not self._media_message.media:
            await self._cmd_message.reply_text(translator.get("REPLY_TO_MEDIA"), quote=True)
            return

        self._media_message.from_user = self._cmd_message.from_user
        await self._preserve_original_thumb()

        is_video = False
        is_audio = False
        mime = ""

        try:
            mime = self._media_message.document.mime_type.split("/")[0]
        except:
            pass

        if self._media_message.video is not None:
            is_video = True
        elif (self._media_message.audio is not None or self._media_message.voice is not None):
            is_audio = True
        elif mime == "video":
            is_video = True
        elif mime == "audio":
            is_audio = True

        try:
            new_file_name = self._cmd_message.text.split(" ", 1)[1]
        except Exception as e:
            if not self._fltr_obj.has_filters():
                await self._cmd_message.reply_text(translator.get("RENAME_NOFLTR_NONAME"))
                return

            original_file_name = (
                self._media_message.document.file_name if self._media_message.document else
                self._media_message.video.file_name if self._media_message.video else
                self._media_message.audio.file_name if (self._media_message.audio or self._media_message.voice) else
                "no_name"
            )
            new_file_name = await self._fltr_obj.filtered_name(original_file_name)
            if original_file_name == new_file_name:
                await self._cmd_message.reply_text(translator.get("RENAME_NO_FILTER_MATCH"))
                return
            await self._cmd_message.reply_text(translator.get("RENAME_FILTER_MATCH_USED") + f"\nFile name:- {new_file_name}")

        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(translator.get("RENAME_CANCEL"), f"cancel {self._unique_id}")]
        ])

        if get_var("SAVE_FILE_TO_TRACE_CHANNEL"):
            await self._client.forward_messages(
                get_var("TRACE_CHANNEL"),
                self._media_message.chat.id,
                self._media_message.id
            )

        track_msg = translator.get(
            "TRACK_MESSAGE_EXECUTION_START",
            uid=self._unique_id,
            username=self._cmd_message.from_user.username,
            name=self._cmd_message.from_user.mention(style="md"),
            user_id=self._cmd_message.from_user.id,
            file_name=new_file_name,
        )
        await self._client.send_track(track_msg)

        try:
            progress = await self._media_message.reply(
                translator.get("DL_RENAMING_FILE"), quote=True, reply_markup=markup
            )
            dl_path = os.path.join("downloads/{}/".format(str(time.time()).replace(".", "")))
            await aos.makedirs(dl_path, exist_ok=True)
            dl_path = await self._media_message.download(
                file_name=dl_path,
                progress=progress_for_pyrogram,
                progress_args=(
                    translator.get("DOWNLOADING_THE_FILE"),
                    progress,
                    time.time(),
                    get_var("SLEEP_SECS"),
                    self._client,
                    self._unique_id,
                    markup,
                ),
            )
        except Exception as e:
            renamelog.exception("Download error")
            await progress.edit_text(translator.get("RENAME_ERRORED"))
            return

        if dl_path is None:
            await progress.edit_text(translator.get("RENAME_CANCEL_BY_USER"))
            return

        udb = UserDB()
        mode_choice = udb.get_mode(self._media_message.from_user.id)
        is_force = mode_choice == udb.MODE_AS_DOCUMENT or (
            mode_choice == udb.MODE_SAME_AS_SENT and self._media_message.document
        )

        thumb_path = await self._get_thumbnail_path(dl_path, self._cmd_message.from_user.id, is_force)
        await progress.edit_text(translator.get("RENAME_DOWNLOADING_DONE"), reply_markup=None)

        caption = udb.get_var("caption", self._cmd_message.from_user.id)
        if caption:
            caption = caption.format(file_name=new_file_name)

        try:
            if is_audio and not is_force:
                metadata = extractMetadata(createParser(dl_path))
                duration = self._media_message.audio.duration if self._media_message.audio else 0
                if duration == 0 and metadata and metadata.has("duration"):
                    duration = metadata.get("duration").seconds
                performer = metadata.get("author") if metadata and metadata.has("author") else ""

                try:
                    rmsg = await self._client.send_audio(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        duration=duration,
                        performer=performer,
                        thumb=thumb_path,
                        progress=progress_for_pyrogram,
                        progress_args=(
                            translator.get("UPLOADING_THE_FILE", file_name=new_file_name),
                            progress,
                            time.time(),
                            get_var("SLEEP_SECS"),
                            self._client,
                            self._unique_id,
                            markup,
                        ),
                    )
                except ThumbnailFileInvalid:
                    rmsg = await self._client.send_audio(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        duration=duration,
                        performer=performer,
                        thumb=None,
                        progress=progress_for_pyrogram,
                        progress_args=(...),
                    )

            elif is_video and not is_force:
                width = height = 0
                if thumb_path:
                    try:
                        thumb_meta = extractMetadata(createParser(thumb_path))
                        if thumb_meta:
                            width = thumb_meta.get("width", 0)
                            height = thumb_meta.get("height", 0)
                    except:
                        pass

                duration = self._media_message.video.duration if self._media_message.video else 0
                if duration == 0:
                    try:
                        metadata = extractMetadata(createParser(dl_path))
                        if metadata and metadata.has("duration"):
                            duration = metadata.get("duration").seconds
                    except:
                        pass

                try:
                    rmsg = await self._client.send_video(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        duration=duration,
                        width=width,
                        height=height,
                        thumb=thumb_path,
                        progress=progress_for_pyrogram,
                        progress_args=(...),
                    )
                except ThumbnailFileInvalid:
                    rmsg = await self._client.send_video(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        duration=duration,
                        width=width,
                        height=height,
                        thumb=None,
                        progress=progress_for_pyrogram,
                        progress_args=(...),
                    )

            else:
                try:
                    rmsg = await self._client.send_document(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        thumb=thumb_path,
                        force_document=is_force,
                        progress=progress_for_pyrogram,
                        progress_args=(...),
                    )
                except ThumbnailFileInvalid:
                    rmsg = await self._client.send_document(
                        self._cmd_message.chat.id,
                        dl_path,
                        file_name=new_file_name,
                        caption=caption,
                        thumb=None,
                        force_document=is_force,
                        progress=progress_for_pyrogram,
                        progress_args=(...),
                    )

            if rmsg is None:
                await progress.edit_text(translator.get("RENAME_UPLOAD_CANCELLED_BY_USER"))
            else:
                await progress.edit_text(translator.get("RENAME_UPLOADING_DONE"))

            try:
                size = await aos.path.getsize(dl_path)
                userin.count_upload(size)
                userin.update_user(self.user_msg.from_user.id, uploaded=size)
            except Exception as e:
                renamelog.warning(f"Upload stats error: {e}")

        except Exception as e:
            renamelog.exception("Upload error")
            await progress.edit_text(translator.get("RENAME_ERRORED"))
        finally:
            if thumb_path:
                await self._rem_this(thumb_path)
            await self._rem_this(dl_path)

    async def _rem_this(self, path):
        """Safe file removal"""
        try:
            if path and await aos.path.exists(path):
                await aos.remove(path)
        except Exception as e:
            renamelog.warning(f"Failed to remove {path}: {e}")






