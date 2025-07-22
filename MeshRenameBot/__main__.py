from .core.get_config import get_var
from .core.handlers import add_handlers
from .mesh_bot import MeshRenameBot
from .maneuvers.ExecutorManager import ExecutorManager
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

if __name__ == "__main__":
    from MeshRenameBot.utils.user_input import userin
    userin.load_stats()  # ✅ Load saved stats before bot runs

    rbot = MeshRenameBot("MeshRenameBot", get_var("API_ID"), get_var("API_HASH"),
                         bot_token=get_var("BOT_TOKEN"), workers=200)
    excm = ExecutorManager()
    add_handlers(rbot)
    rbot.run()
