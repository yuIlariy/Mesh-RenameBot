from .core.get_config import get_var
from .core.handlers import add_handlers
from .mesh_bot import MeshRenameBot
from .maneuvers.ExecutorManager import ExecutorManager
from pyrogram.errors import FloodWait
import asyncio
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

# 👑 Preload channel peer before bot runs
async def preload_known_peers(bot):
    track_channel = int(get_var("TRACE_CHANNEL"))  # 💡 Value from env/config

    try:
        chat = await bot.get_chat(track_channel)
        print(f"✅ Preloaded peer: {chat.title} ({chat.id})")
    except FloodWait as fw:
        print(f"⏳ FloodWait: sleeping {fw.value}s...")
        await asyncio.sleep(fw.value)
        await preload_known_peers(bot)
    except Exception as e:
        print(f"❌ Failed to preload TRACE_CHANNEL `{track_channel}`:\n{e}")

if __name__ == "__main__":
    rbot = MeshRenameBot(
        "MeshRenameBot",
        get_var("API_ID"),
        get_var("API_HASH"),
        bot_token=get_var("BOT_TOKEN"),
        workers=200
    )

    async def start_bot():
        await rbot.start()
        await preload_known_peers(rbot)  # 🔐 Register channel peer
        add_handlers(rbot)
        rbot.run()

    asyncio.run(start_bot())
