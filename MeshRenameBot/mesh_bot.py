from pyrogram import Client, types
from pyrogram.file_id import FileId
from pyrogram.errors import FloodWait
import logging
import asyncio
from datetime import datetime
import pytz
import random
from MeshRenameBot.core.get_config import get_var

renamelog = logging.getLogger(__name__)


class MeshRenameBot(Client):
    async def start(self):
        await super().start()

        try:
            me = await self.get_me()
            bot_mention = me.mention  # clickable mention via tg://user?id=...

            tz = pytz.timezone("Africa/Nairobi")
            now = datetime.now(tz)

            # Restart message for log channel
            restart_msg = (
                f"🌋 **{bot_mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n"
                f"📅 **Dᴀᴛᴇ** : {now.strftime('%d %B, %Y')}\n"
                f"⏰ **Tɪᴍᴇ** : {now.strftime('%I:%M:%S %p')}\n"
                f"🌐 **Tɪᴍᴇᴢᴏɴᴇ** : Africa/Nairobi\n\n"
                "🉐 **Vᴇʀsɪᴏɴ** : v4.3.8 (Layer 951)"
            )

            # Owner message with rotating greeting
            greetings = [
                "🚀 Bot’s back in action!",
                "🧩 Patch mode activated!",
                "🦾 Systems online!",
                "🎯 Ready to rename and roll!",
                "📦 Deployment complete!"
            ]
            owner_msg = (
                f"👑 **Your bot {bot_mention} just woke up!**\n\n"
                f"📅 **Dᴀᴛᴇ** : {now.strftime('%d %B, %Y')}\n"
                f"⏰ **Tɪᴍᴇ** : {now.strftime('%I:%M:%S %p')}\n"
                f"🌐 **Tɪᴍᴇᴢᴏɴᴇ** : Africa/Nairobi\n\n"
                f"{random.choice(greetings)}\n"
                "🉐 **Vᴇʀsɪᴏɴ** : v4.3.8 (Layer 951)\n\n"
                "`🫡 All systems go, Capitán.`"
            )

            # Send to log channel
            log_channel = get_var("LOG_CHANNEL")
            if log_channel:
                await self.send_message(int(log_channel), restart_msg, disable_web_page_preview=True)

            # Send to owner
            owner_raw = get_var("OWNER_ID")
            owner_id = int(owner_raw) if isinstance(owner_raw, str) else owner_raw
            await self.send_message(owner_id, owner_msg, disable_web_page_preview=True)

            # Trace ping message + sticker
            track_channel = int(get_var("TRACE_CHANNEL"))
            trace_text = (
                f"🪆 **Trace Ping Received**\n\n"
                f"🧭 Bot `{me.username}` is online and synced.\n"
                f"📅 {now.strftime('%d %B, %Y')} | ⏰ {now.strftime('%I:%M:%S %p')}\n"
                "`📡 Monitoring tasks and rename queue.`"
            )
            try:
                await self.send_message(track_channel, trace_text, disable_web_page_preview=True)
                await self.send_sticker(track_channel, "CAACAgIAAxkBAAEPK01ooa7l8E2oJqUYzkUflC7PprKbeQACn2kAAi2ssEiHpvbh9SGYazYE")
            except Exception:
                renamelog.exception("Failed to send trace ping or sticker.")

        except Exception:
            renamelog.exception("Failed to send restart message to LOG_CHANNEL or OWNER_ID.")

        # Preload TRACE_CHANNEL
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


