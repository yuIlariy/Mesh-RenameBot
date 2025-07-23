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

# 👑 Preload peer before bot starts handling messages
async def preload_known_peers(bot):
    track_channel = int(get_var("TRACE_CHANNEL"))

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

    excm = ExecutorManager()
    add_handlers(rbot)

    @rbot.on_start()
    async def on_bot_start(_: MeshRenameBot):
        await preload_known_peers(rbot)  # ✅ Works inside bot’s own event loop

    rbot.run()
