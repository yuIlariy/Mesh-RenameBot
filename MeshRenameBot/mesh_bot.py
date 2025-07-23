from pyrogram import Client, types
from pyrogram.file_id import FileId
from pyrogram.errors import FloodWait
import logging
import asyncio
from MeshRenameBot.core.get_config import get_var

renamelog = logging.getLogger(__name__)


class MeshRenameBot(Client):
    async def start(self):
        await super().start()

        track_channel = int(get_var("TRACE_CHANNEL"))
        try:
            chat = await self.get_chat(track_channel)
            print(f"✅ Preloaded peer: {chat.title} ({chat.id})")
        except FloodWait as fw:
            print(f"⏳ FloodWait: sleeping {fw.value}s...")
            await asyncio.sleep(fw.value)
            await self.get_chat(track_channel)
        except Exception as e:
            print(f"❌ Failed to preload TRACE_CHANNEL `{track_channel}`:\n{e}")

    async def get_file_id(self, message):
        available_media = (
            "audio", "document", "photo", "sticker", "animation", "video",
            "voice", "video_note", "new_chat_photo"
        )

        if isinstance(message, types.Message):
            for kind in available_media:
                media = getattr(message, kind, None)
                if media is not None:
                    break
            else:
                return None
        else:
            media = message

        file_id_str = media if isinstance(media, str) else media.file_id
        return FileId.decode(file_id_str)

    async def send_track(self, text_mess):
        track_channel = get_var("TRACE_CHANNEL")
        if track_channel != 0:
            try:
                await self.send_message(track_channel, text_mess)
            except Exception:
                renamelog.exception("Make Sure to enter the Track Channel ID correctly.")
