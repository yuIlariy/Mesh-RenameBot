import asyncio
import logging
import time
import os
import aiofiles.os as aos
from typing import Optional

from aiofiles import os as aos
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import Client, StopTransmission
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types.messagesandmedia.message_entity import MessageEntity
from MeshRenameBot.utils.user_input import userin

from ..core.getconfig import getvar
from ..core.thumbmanage import getthumbnail
from ..database.user_db import UserDB
from ..maneuvers.ExecutorManager import ExecutorManager
from ..mesh_bot import MeshRenameBot
from ..translations import Translator
from ..utils.c_filter import FilterUtils
from ..utils.progressforpyro import progressforpyrogram
from .Default import DefaultManeuver

renamelog = logging.getLogger(name)


class RenameManeuver(DefaultManeuver):
    def init(
        self, client: MeshRenameBot, mediamessage: Message, cmdmessage: Message
    ) -> None:
        super().init(client, mediamessage, cmdmessage)
        self.uniqueid = int(str(cmdmessage.chat.id) + str(cmdmessage.id))
        self.fltrobj = FilterUtils(cmdmessage.fromuser.id)
        self.usermsg = cmdmessage

    async def getuserthumbnail(self, userid: int) -> Optional[str]:
        """Get user-set thumbnail path if it exists"""
        try:
            thumbpath = UserDB().getthumbnail(userid)
            if thumbpath and isinstance(thumbpath, str) and os.path.exists(thumbpath):
                return thumbpath
        except Exception as e:
            renamelog.error(f"Error getting user thumbnail: {str(e)}", exc_info=True)
        return None

    async def execute(self) -> None:
        self.executepending = False
        userid = self.cmdmessage.fromuser.id
        userlocale = UserDB().getvar("locale", userid)
        translator = Translator(userlocale)

        if self.mediamessage is None or not self.mediamessage.media:
            await self.cmdmessage.reply_text(translator.get("REPLYTO_MEDIA"), quote=True)
            return

        self.mediamessage.from_user = self.cmdmessage.from_user

        # Get user thumbnail FIRST
        thumb_path = await self.getuserthumbnail(userid)

        # Pyrogram accepts 'thumb=None' if none available, so no problem if thumb_path is None

        # Determine media type
        is_video = False
        is_audio = False
        try:
            mime = getattr(self.mediamessage.document, 'mime_type', '').split("/")[0]
            if self.mediamessage.video is not None:
                is_video = True
            elif (self.mediamessage.audio is not None or self.mediamessage.voice is not None):
                is_audio = True
            elif mime == "video":
                is_video = True
            elif mime == "audio":
                is_audio = True
        except Exception as e:
            renamelog.warning(f"Error determining media type: {str(e)}")

        # Get new file name
        try:
            new_filename = self.cmdmessage.text.split(" ", 1)[1]
        except Exception as e:
            if not self.fltrobj.has_filters():
                await self.cmdmessage.reply_text(translator.get("RENAMENOFLTR_NONAME"))
                return

            original_filename = (
                getattr(self.mediamessage.document, 'file_name', None) or
                getattr(self.mediamessage.video, 'file_name', None) or
                getattr(self.mediamessage.audio, 'file_name', None) or
                "no_name"
            )
            new_filename = await self.fltrobj.filteredname(original_filename)
            if original_filename == new_filename:
                await self.cmdmessage.reply_text(translator.get("RENAMENOFILTERMATCH"))
                return
            await self.cmdmessage.reply_text(
                translator.get("RENAMEFILTERMATCHUSED") + f"\nFile name:- {new_filename}"
            )

        # Setup progress tracking
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(translator.get("RENAMECANCEL"), f"cancel {self.uniqueid}")]
        ])

        if getvar("SAVEFILETOTRACE_CHANNEL"):
            await self.client.forward_messages(
                getvar("TRACECHANNEL"),
                self.mediamessage.chat.id,
                self.mediamessage.id
            )

        await self.client.send_track(translator.get(
            "TRACKMESSAGEEXECUTION_START",
            uid=self.uniqueid,
            username=self.cmdmessage.from_user.username,
            name=self.cmdmessage.from_user.mention(style="md"),
            userid=self.cmdmessage.from_user.id,
            filename=new_filename,
        ))

        # Download file
        try:
            progress = await self.mediamessage.reply(
                translator.get("DLRENAMINGFILE"), quote=True, reply_markup=markup
            )
            dl_path = os.path.join("downloads/{}/".format(str(time.time()).replace(".", "")))
            await aos.makedirs(dl_path, exist_ok=True)
            dl_path = await self.mediamessage.download(
                file_name=dl_path,
                progress=progressforpyrogram,
                progress_args=(
                    translator.get("DOWNLOADINGTHEFILE"),
                    progress,
                    time.time(),
                    getvar("SLEEPSECS"),
                    self.client,
                    self.uniqueid,
                    markup,
                ),
            )
            if dl_path is None:
                await progress.edit_text(translator.get("RENAMECANCELBYUSER"))
                return
        except Exception as e:
            renamelog.error(f"Download error: {str(e)}", exc_info=True)
            await progress.edit_text(translator.get("RENAMEERRORED"))
            return

        # Get upload mode
        udb = UserDB()
        mode_choice = udb.get_mode(self.mediamessage.from_user.id)
        is_force = (
            mode_choice == udb.MODEAS_DOCUMENT or
            (mode_choice == udb.MODESAMEASSENT and self.mediamessage.document is not None)
        )

        await progress.edit_text(translator.get("RENAMEDOWNLOADINGDONE"), reply_markup=None)

        # Prepare caption
        caption = udb.getvar("caption", self.cmdmessage.from_user.id)
        if caption and isinstance(caption, str):
            try:
                caption = caption.format(filename=new_filename)
            except Exception as e:
                renamelog.warning(f"Error formatting caption: {str(e)}")

        # Upload file (always use user's thumbnail if no other)
        try:
            if is_audio and not is_force:
                duration = getattr(self.mediamessage.audio, 'duration', 0)
                performer = ""
                try:
                    metadata = extractMetadata(createParser(dl_path))
                    if duration == 0 and metadata and metadata.has("duration"):
                        duration = metadata.get("duration").seconds
                    if metadata.has("author"):
                        performer = metadata.get("author")
                except Exception as e:
                    renamelog.warning(f"Metadata extraction error: {str(e)}")

                rmsg = await self.client.send_audio(
                    chat_id=self.cmdmessage.chat.id,
                    audio=dl_path,
                    file_name=new_filename,
                    caption=caption,
                    duration=duration,
                    performer=performer,
                    thumb=thumb_path, # Passed the user thumbnail here
                    progress=progressforpyrogram,
                    progress_args=(
                        translator.get("UPLOADINGTHEFILE", filename=new_filename),
                        progress,
                        time.time(),
                        getvar("SLEEPSECS"),
                        self.client,
                        self.uniqueid,
                        markup,
                    ),
                )

            elif is_video and not is_force:
                width = height = 0
                duration = getattr(self.mediamessage.video, 'duration', 0)
                try:
                    if self.mediamessage.video and self.mediamessage.video.thumbs:
                        # Use the video's original thumbnail dimensions if available
                        width = self.mediamessage.video.thumbs[0].width
                        height = self.mediamessage.video.thumbs[0].height
                    elif thumb_path:
                        # If a user thumbnail exists, use its dimensions
                        thumbmeta = extractMetadata(createParser(thumb_path))
                        if thumbmeta:
                            width = thumbmeta.get("width", 0)
                            height = thumbmeta.get("height", 0)
                    
                    if duration == 0:
                        metadata = extractMetadata(createParser(dl_path))
                        if metadata and metadata.has("duration"):
                            duration = metadata.get("duration").seconds
                except Exception as e:
                    renamelog.warning(f"Video metadata error: {str(e)}")

                rmsg = await self.client.send_video(
                    chat_id=self.cmdmessage.chat.id,
                    video=dl_path,
                    file_name=new_filename,
                    caption=caption,
                    duration=duration,
                    width=width,
                    height=height,
                    thumb=thumb_path, # Passed the user thumbnail here
                    progress=progressforpyrogram,
                    progress_args=(
                        translator.get("UPLOADINGTHEFILE", filename=new_filename),
                        progress,
                        time.time(),
                        getvar("SLEEPSECS"),
                        self.client,
                        self.uniqueid,
                        markup,
                    ),
                )

            else:
                rmsg = await self.client.send_document(
                    chat_id=self.cmdmessage.chat.id,
                    document=dl_path,
                    file_name=new_filename,
                    caption=caption,
                    thumb=thumb_path, # Passed the user thumbnail here
                    force_document=is_force,
                    progress=progressforpyrogram,
                    progress_args=(
                        translator.get("UPLOADINGTHEFILE", filename=new_filename),
                        progress,
                        time.time(),
                        getvar("SLEEPSECS"),
                        self.client,
                        self.uniqueid,
                        markup,
                    ),
                )

            if rmsg is None:
                await progress.edit_text(translator.get("RENAMEUPLOADCANCELLEDBY_USER"))
            else:
                await progress.edit_text(translator.get("RENAMEUPLOADING_DONE"))

            try:
                size = await aos.path.getsize(dl_path)
                userin.count_upload(size)
                userin.updateuser(self.usermsg.from_user.id, uploaded=size)
            except Exception as e:
                renamelog.warning(f"Upload stats error: {str(e)}")

        except Exception as e:
            renamelog.error(f"Upload error: {str(e)}", exc_info=True)
            await progress.edit_text(translator.get("RENAMEERRORED"))
        finally:
            # Cleanup only the downloaded file, not the saved user thumbnail
            if dl_path and os.path.exists(dl_path):
                await rem_this(dl_path)


async def rem_this(path: str) -> None:
    """Safely remove file with comprehensive checks"""
    try:
        if path and isinstance(path, str) and os.path.exists(path):
            await aos.remove(path)
    except Exception as e:
        renamelog.warning(f"Error removing file {path}: {str(e)}")





