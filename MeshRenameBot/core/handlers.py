from os import rename
from MeshRenameBot.core.get_config import get_var
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
import re
import time
import datetime
import psutil
import logging
import signal
import shutil
import asyncio
from ..maneuvers.ExecutorManager import ExecutorManager
from ..maneuvers.Rename import RenameManeuver
from ..utils.c_filter import filter_controller, filter_interact
from ..utils.user_input import interactive_input
from .thumb_manage import handle_set_thumb, handle_get_thumb, handle_clr_thumb
from .mode_select import upload_mode, mode_callback
from ..config import Commands
from ..translations import Translator, TRANSLATION_MAP
from ..database.user_db import UserDB
from .caption_manage import set_caption, del_caption
from ..mesh_bot import MeshRenameBot
from .change_locale import change_locale, set_locale
from pyrogram.enums import ParseMode
from MeshRenameBot.config import Config
from MeshRenameBot.utils.user_input import userin  # 🧠 Load your tracker class
from MeshRenameBot import config



renamelog = logging.getLogger(__name__)


def add_handlers(client: MeshRenameBot) -> None:
    """This function is responsible to manually register all the bot handlers.

    Args:
        client (pyrogram.Client): Initialized pyrogram client.
    """

    client.add_handler(MessageHandler(intercept_handler))
    client.add_handler(MessageHandler(interactive_input))
    client.add_handler(
        MessageHandler(start_handler, filters.regex(Commands.START, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(rename_handler, filters.regex(Commands.RENAME, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(
            rename_handler,
            filters.document | filters.video | filters.audio | filters.photo,
        )
    )
    client.add_handler(
        MessageHandler(
            filter_controller, filters.regex(Commands.FILTERS, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_set_thumb, filters.regex(Commands.SET_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_get_thumb, filters.regex(Commands.GET_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(
            handle_clr_thumb, filters.regex(Commands.CLR_THUMB, re.IGNORECASE)
        )
    )
    client.add_handler(
        MessageHandler(handle_queue, filters.regex(Commands.QUEUE, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(upload_mode, filters.regex(Commands.MODE, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(help_str, filters.regex(Commands.HELP, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(set_caption, filters.regex(Commands.SET_CAPTION, re.IGNORECASE))
    )
    client.add_handler(
        MessageHandler(change_locale, filters.regex(Commands.SET_LANG, re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(cancel_this, filters.regex("cancel", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(filter_interact, filters.regex("fltr", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(mode_callback, filters.regex("mode", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(
            mode_callback, filters.regex("command_mode", re.IGNORECASE)
        )
    )
    client.add_handler(
        CallbackQueryHandler(close_message, filters.regex("close", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(del_caption, filters.regex("delcaption", re.IGNORECASE))
    )
    client.add_handler(
        CallbackQueryHandler(set_locale, filters.regex("set_locale", re.IGNORECASE))
    )
    client.add_handler(
    MessageHandler(ping_handler, filters.regex(r"^/ping$", re.IGNORECASE))
    )
    client.add_handler(
    MessageHandler(status_handler, filters.regex(r"^/status$", re.IGNORECASE))
    )
    client.add_handler(
    MessageHandler(info_handler, filters.regex(r"^/info$", re.IGNORECASE))
    )
    client.add_handler(
    CallbackQueryHandler(info_callback, filters.regex("info", re.IGNORECASE))
    )
    client.add_handler(
    CallbackQueryHandler(home_callback, filters.regex("home", re.IGNORECASE))
    )
    client.add_handler(
    MessageHandler(stats_handler, filters.regex(r"^/stats$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
    )
    client.add_handler(
    MessageHandler(user_profile_handler, filters.regex(r"^/profile$", re.IGNORECASE))
    )
    client.add_handler(
    MessageHandler(top_users_handler, filters.regex(r"^/leaderboard$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
    )
    client.add_handler(
    MessageHandler(
        broadcast_handler,
        filters.regex(r"^/broadcast$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
    )

    
    signal.signal(signal.SIGINT, term_handler)
    signal.signal(signal.SIGTERM, term_handler)

BOT_START_TIME = time.time()

async def ping_handler(client: Client, msg: Message) -> None:
    import datetime
    start = time.time()
    reply = await msg.reply("Pinging...")
    end = time.time()

    latency = (end - start) * 1000
    uptime = str(datetime.timedelta(seconds=int(time.time() - BOT_START_TIME)))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    caption = (
        f"🏓 **Pong!** `{latency:.2f}ms`\n\n"
        f"⏱ Uptime: `{uptime}`\n"
        f"⚙️ CPU: `{cpu}%`  🚀 Memory: `{mem}%`\n\n"
        f"🚀 **Powered by** [NAm](https://t.me/xspes)"
    )

    await reply.delete()  # clean original "Pinging..." message
    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption
    )


@Client.on_message(filters.regex(r"^/stats$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
async def stats_handler(client: Client, msg: Message) -> None:
    import datetime, shutil, psutil
    from MeshRenameBot.database.user_db import UserDB  # ✅ fixed import

    # ⏱️ System metrics
    uptime = str(datetime.timedelta(seconds=int(time.time() - BOT_START_TIME)))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = shutil.disk_usage("/")
    total_disk = disk.total // (1024 ** 3)
    used_disk = disk.used // (1024 ** 3)
    free_disk = disk.free // (1024 ** 3)

    # 🧠 Global telemetry aggregation from DB
    total_users = 0
    total_renames = 0
    total_download = 0
    total_upload = 0

    for user_id in UserDB().get_all_users():
        data = UserDB().get_var("telemetry", user_id)
        if isinstance(data, dict):
            total_users += 1
            total_renames += data.get("rename", 0)
            total_download += data.get("download", 0)
            total_upload += data.get("upload", 0)

    # Format sizes
    download_gb = round(total_download / (1024 ** 3), 2)
    upload_gb = round(total_upload / (1024 ** 3), 2)

    caption = (
        f"📊 **Global Bot Stats**\n\n"
        f"👥 Total Users: `{total_users}`\n"
        f"📁 Files Renamed: `{total_renames}`\n"
        f"📥 Downloaded: `{download_gb} GB`\n"
        f"📤 Uploaded: `{upload_gb} GB`\n"
        f"🕒 Uptime: `{uptime}`\n"
        f"⚙️ CPU: `{cpu}%`  🚀 Memory: `{mem}%`\n"
        f"🗄️ Disk: `{used_disk} GB / {total_disk} GB`, free: `{free_disk} GB`\n\n"
        f"🚀 **Powered by** [NAm](https://t.me/xspes)"
    )

    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption
    )
    


#🌋 Broadcast Trial ☄️

from pyrogram.errors import FloodWait, FileReferenceExpired
from MeshRenameBot.database.user_db import UserDB


@Client.on_message(filters.regex(r"^/broadcast$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
async def broadcast_handler(client: Client, msg: Message) -> None:
    if not msg.reply_to_message:
        await msg.reply_text("⚠️ Reply to a message to broadcast it.", quote=True)
        return

    users = UserDB().get_all_users()
    success = 0
    failed = 0

    mention = f"[{msg.from_user.first_name}](tg://user?id={msg.from_user.id})"
    log_text = f"{mention} or `{msg.from_user.id}` ʜᴀꜱ ꜱᴛᴀʀᴛᴇᴅ ᴀ Bʀᴏᴀᴅᴄᴀꜱᴛ...🌌"

    # ✅ Use get_var to fetch LOG_CHANNEL dynamically
    log_channel = get_var("LOG_CHANNEL")

    await client.send_message(log_channel, log_text)
    try:
        await msg.reply_to_message.copy(chat_id=log_channel)
    except Exception as e:
        await client.send_message(log_channel, f"⚠️ Failed to log broadcast content: `{e}`")

    await msg.reply_text(f"📡 Broadcasting to `{len(users)}` users...", quote=True)

    for user_id in users:
        try:
            await msg.reply_to_message.copy(chat_id=user_id)
            success += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
            continue
        except FileReferenceExpired:
            failed += 1
        except Exception:
            failed += 1

    summary = f"📊 Broadcast finished by {mention}\n✅ Success: `{success}`\n❌ Failed: `{failed}`"
    await client.send_message(log_channel, summary)

    await msg.reply_text(f"✅ Broadcast Done!\n\nSuccess: `{success}`\nFailed: `{failed}`", quote=True)

#close trial 🌋

@Client.on_message(filters.regex(r"^/leaderboard$", re.IGNORECASE) & filters.user(Config.OWNER_ID[1]))
async def top_users_handler(client: Client, msg: Message) -> None:
    from MeshRenameBot.database.user_db import UserDB
    import datetime

    all_stats = []
    for user_id in UserDB().get_all_users():
        stats = UserDB().get_var("telemetry", user_id)
        if isinstance(stats, dict):
            upload_bytes = stats.get("upload", 0)
            upload_gb = round(upload_bytes / (1024 ** 3), 2)
            rename_count = stats.get("rename", 0)

            badge = (
                "👑" if upload_gb >= 1000 else
                "🥈" if upload_gb >= 500 else
                "🥉" if upload_gb >= 100 else
                "🔄"
            )

            all_stats.append((upload_gb, badge, rename_count, user_id))

    top = sorted(all_stats, reverse=True)[:10]

    caption = "**🏆 Top Uploaders**\n\n"
    for i, (upload_gb, badge, renames, user_id) in enumerate(top, 1):
        try:
            user = await client.get_users(user_id)
            if user.username:
                mention = f"@{user.username}"
            else:
                name = user.first_name or "User"
                mention = f"[{name}](tg://user?id={user_id})"
        except Exception:
            mention = f"[User](tg://user?id={user_id})"

        caption += (
            f"{i}. {badge} {mention}\n"
            f"   📤 Uploaded: `{upload_gb} GB` | 📁 Renamed: `{renames}`\n"
        )

    caption += "\n👑 Legends are crowned by upload volume. Keep renaming!"

    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption
    )
    

@Client.on_message(filters.regex(r"^/profile$", re.IGNORECASE))
async def user_profile_handler(client: Client, msg: Message) -> None:
    import datetime
    from MeshRenameBot.database.user_db import UserDB  # ✅ fixed import

    def get_upload_badge(upload_bytes: int) -> str:
        gb = upload_bytes / (1024 ** 3)
        if gb >= 1000:
            return "👑 Crowned King"
        elif gb >= 500:
            return "🥈 Medal Master"
        elif gb >= 100:
            return "🥉 Bronze Renamer"
        else:
            return "🔄 Rookie"

    user_id = msg.from_user.id
    user_mention = msg.from_user.mention or f"[User](tg://user?id={user_id})"

    stats = UserDB().get_var("telemetry", user_id)
    if not isinstance(stats, dict):
        stats = {}

    rename_count = stats.get("rename", 0)
    download_gb = round(stats.get("download", 0) / (1024 ** 3), 2)
    upload_gb_raw = stats.get("upload", 0)
    upload_gb = round(upload_gb_raw / (1024 ** 3), 2)
    badge = get_upload_badge(upload_gb_raw)

    last_active = datetime.datetime.fromtimestamp(
        stats.get("last_active", time.time())
    ).strftime("%Y-%m-%d %H:%M:%S")

    caption = (
        f"📊 **Your Usage Stats**\n\n"
        f"👤 User: {user_mention}\n"
        f"🆔 ID: `{user_id}`\n"
        f"📁 Files Renamed: `{rename_count}`\n"
        f"📥 Downloaded: `{download_gb} GB`\n"
        f"📤 Uploaded: `{upload_gb} GB`\n\n"
        f"🎖 Badge: `{badge}`\n\n"
        f"🕒 Last Active: `{last_active}`\n\n"
        f"🚀 **Powered by** [NAm](https://t.me/xspes)"
    )

    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption
    )
    

async def status_handler(client: Client, msg: Message) -> None:
    uptime = str(datetime.timedelta(seconds=int(time.time() - BOT_START_TIME)))
    from MeshRenameBot.utils.user_input import userin  # adjust path if needed
    total_users = len(userin.track_users)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = shutil.disk_usage("/")

    total_disk = disk.total // (1024 * 1024 * 1024)
    used_disk = disk.used // (1024 * 1024 * 1024)
    free_disk = disk.free // (1024 * 1024 * 1024)

    caption = (
        f"🛸 **Bot is Up and Running successfully**🗿\n\n"
        f"⏱ Uptime: `{uptime}`\n"
        f"⚙️ CPU Usage: `{cpu}%`\n"
        f"🚀 Memory Usage: `{mem}%`\n"
        f"🗄️ Disk Space: `{used_disk} GB / {total_disk} GB` free: `{free_disk} GB`\n\n"
        f"🚀 **Powered by** [NAm](https://t.me/xspes)"
    )

    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption
    )
    

@Client.on_message(filters.regex(r"^/info$", re.IGNORECASE))
async def info_handler(client, msg: Message):
    caption = (
        "📦 **Auto Rename Bot**\n"
        "🎯 **Version:** [1.3.8C](https://github.com/yuIlariy/Mesh-RenameBot)\n\n"
        "👨‍💻 **Developer:** [Yash Dk 🗿](https://github.com/yash-dk)\n"
        "🔧 **Maintainer:** [NAm 🗿](https://github.com/yuilariy)\n"
        "🛠️ **Source Code:** [Mesh-RenameBot](https://github.com/yuIlariy/Mesh-RenameBot)\n\n"
        "☁️ **Platform:** [AWS](https://aws.amazon.com)\n"
        "🐍 **Language:** [Python](https://www.python.org)\n"
        "🗄️ **Database:** [Postgres (Neon)](https://neon.tech)"
    )

    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=caption,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🏠 Home", callback_data="home")
            ]
        ])
    )


@Client.on_callback_query(filters.regex("info"))
async def info_callback(client, callback_query):
    await callback_query.message.edit_caption(
        caption=(
            "📦 **Auto Rename Bot**\n"
            "🎯 **Version:** [1.3.8C](https://github.com/yuIlariy/Mesh-RenameBot)\n\n"
            "👨‍💻 **Developer:** [Yash Dk 🗿](https://github.com/yash-dk)\n"
            "🔧 **Maintainer:** [NAm 🗿](https://github.com/yuilariy)\n"
            "🛠️ **Source Code:** [Mesh-RenameBot](https://github.com/yuIlariy/Mesh-RenameBot)\n\n"
            "☁️ **Platform:** [AWS](https://aws.amazon.com)\n"
            "🐍 **Language:** [Python](https://www.python.org)\n"
            "🗄️ **Database:** [Postgres (Neon)](https://neon.tech)"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Home", callback_data="home")]
        ])
    )

#🚨🚨
from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from MeshRenameBot import MeshRenameBot
from MeshRenameBot.database.users import UserDB
from MeshRenameBot.modules.translator import Translator


@Client.on_callback_query(filters.regex("home"))
async def home_callback(client, callback_query: CallbackQuery):
    user_locale = UserDB().get_var("locale", callback_query.from_user.id)
    await callback_query.message.edit_caption(
        caption=Translator(user_locale).get("START_MSG"),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Choose Language", callback_data="setlanguage")],
            [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
            [InlineKeyboardButton("🤩 Source code", url="https://github.com/yuIlariy/Mesh-RenameBot")],
            [InlineKeyboardButton("Updates📥", url="https://t.me/modstorexd"),
             InlineKeyboardButton("Support🚀", url="https://t.me/xspes")]
        ])
    )


async def start_handler(_: MeshRenameBot, msg: Message) -> None:
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    await msg.reply_photo(
        photo="https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg",
        caption=Translator(user_locale).get("START_MSG"),
        quote=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🌐 Choose Language", callback_data="setlanguage")],
            [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
            [InlineKeyboardButton("🤩 Source code", url="https://github.com/yuIlariy/Mesh-RenameBot")],
            [InlineKeyboardButton("Updates📥", url="https://t.me/modstorexd"),
             InlineKeyboardButton("Support🚀", url="https://t.me/xspes")]
        ])
    )


async def trigger_setlanguage(client: Client, callback_query: CallbackQuery):
    await client.send_message(
        chat_id=callback_query.from_user.id,
        text="/setlanguage"
    )
    await callback_query.answer()


def register_handlers(client: Client):
    client.add_handler(CallbackQueryHandler(home_callback, filters.regex("home")))
    client.add_handler(CallbackQueryHandler(trigger_setlanguage, filters.regex("setlanguage")))


#🚨🚨

async def rename_handler(client: MeshRenameBot, msg: Message) -> None:
    from MeshRenameBot.utils.user_input import userin

    command_mode = UserDB().get_var("command_mode", msg.from_user.id)
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    translator = Translator(user_locale)

    if command_mode == UserDB.MODE_RENAME_WITHOUT_COMMAND:
        if msg.media is None:
            return
        rep_msg = msg
    else:
        if msg.media:
            return
        rep_msg = msg.reply_to_message

    if rep_msg is None:
        await msg.reply_text(translator.get("REPLY_TO_MEDIA"), quote=True)
        return

    file_id = await client.get_file_id(rep_msg)
    if file_id is not None:
        userin.add_user(msg.from_user.id)
        userin.count_rename()

        # 🧮 Track download size + per-user update
        media = rep_msg.document or rep_msg.video or rep_msg.audio or rep_msg.photo
        size = media.file_size if media and hasattr(media, "file_size") else 0

        userin.count_download(size)
        userin.update_user(msg.from_user.id, rename=True, downloaded=size)

        await msg.reply_text(
            translator.get(
                "RENAME_ADDED_TO_QUEUE", dc_id=file_id.dc_id, media_id=file_id.media_id
            ),
            quote=True,
        )

    await client.send_track(
        translator.get(
            "TRACK_MESSAGE_ADDED_RENAME",
            username=msg.from_user.username,
            name=msg.from_user.first_name,
            user_id=msg.from_user.id,
        )
    )
    await asyncio.sleep(2)
    await ExecutorManager().create_maneuver(RenameManeuver(client, rep_msg, msg))


async def help_str(_: MeshRenameBot, msg: Message) -> None:
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    await msg.reply_text(
        Translator(user_locale).get(
            "HELP_STR",
            startcmd=Commands.START,
            renamecmd=Commands.RENAME,
            filterscmd=Commands.FILTERS,
            setthumbcmd=Commands.SET_THUMB,
            getthumbcmd=Commands.GET_THUMB,
            clrthumbcmd=Commands.CLR_THUMB,
            modecmd=Commands.MODE,
            queuecmd=Commands.QUEUE,
            setcaptioncmd=Commands.SET_CAPTION,
            helpcmd=Commands.HELP,
            pingcmd=Commands.PING,
            statuscmd=Commands.STATUS,
            infocmd=Commands.INFO,
            profilecmd=Commands.PROFILE,
            statscmd=Commands.STATS,
            broadcastcmd=Commands.BROADCAST,
            leaderboardcmd=Commands.LEADER_BOARD, 
            setlanguagecmd=Commands.SET_LANG,
        ),
        quote=True,
    )


def term_handler(signum: int, frame: int) -> None:
    ExecutorManager().stop()


async def cancel_this(_: MeshRenameBot, msg: CallbackQuery) -> None:
    data = str(msg.data).split(" ")
    ExecutorManager().canceled_uids.append(int(data[1]))
    user_locale = UserDB().get_var("locale", msg.from_user.id)
    await msg.answer(Translator(user_locale).get("CANCEL_MESSAGE"), show_alert=True)


async def handle_queue(_: MeshRenameBot, msg: Message) -> None:
    EM = ExecutorManager()
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    j = 0
    for i in EM.all_maneuvers_log:
        if i.is_pending:
            j += 1
    q_len = j

    j = 0
    for i in EM.all_maneuvers_log:
        if i.is_executing:
            j += 1
    currently_exec = j

    from_id = msg.from_user.id
    max_size = get_var("MAX_QUEUE_SIZE")

    fmsg = translator.get(
        "RENAME_QUEUE_STATUS",
        total_tasks=q_len,
        queue_capacity=max_size,
        current_task=currently_exec,
    )

    j = 1
    for i in EM.all_maneuvers_log:
        if i.sender_id == from_id:
            fmsg += translator.get(
                "RENAME_QUEUE_USER_STATUS",
                is_executing=i.is_executing,
                is_pending=i.is_pending,
                task_id=i._unique_id,
                task_number=j,
            )

        if i.is_pending:
            j += 1

    await msg.reply_text(fmsg)


async def intercept_handler(client, msg):
    if not msg.from_user:
        return

    user = msg.from_user
    user_id = user.id

    udb = UserDB()
    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)

    # ✅ Log only if "joined" key is missing
    if udb.get_var("joined", user_id) is None:
        log_text = (
            "🚀 **New User Started Rename Bot**\n\n"
            f"🆔 **User ID:** `{user.id}`\n"
            f"👤 **Username:** @{user.username if user.username else '—'}\n"
            f"📛 **Name:** [{user.first_name}](tg://user?id={user.id})\n"
            f"📂 **Time:** `{msg.date.strftime('%Y-%m-%d %H:%M:%S')}`\n\n"
            f"🚀 Started: {(await client.get_me()).mention}"
        )
        await client.send_message(get_var("LOG_CHANNEL"), log_text)

        # 🧠 Optionally mark user as joined
        udb.set_var("joined", True, user_id)

    # 🔐 Force-join logic
    forcejoin_id = get_var("FORCEJOIN_ID")
    join_username = str(get_var("FORCEJOIN")).strip()
    forcejoin_url = f"https://t.me/{join_username}"

    if forcejoin_id and join_username:
        try:
            user_state = await client.get_chat_member(forcejoin_id, user_id)
            if user_state.status == "kicked":
                await msg.reply_text(translator.get("USER_KICKED"), quote=True)
                return
        except Exception as err:
            if isinstance(err, UserNotParticipant):
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton(translator.get("JOIN_CHANNEL"), url=forcejoin_url)]
                ])
                await msg.reply_text(translator.get("USER_NOT_PARTICIPANT"), reply_markup=keyboard)
                return
            elif isinstance(err, ChatAdminRequired):
                renamelog.error("Bot must be admin in FORCEJOIN chat.")
                return
            elif isinstance(err, UsernameNotOccupied):
                renamelog.error("FORCEJOIN_ID refers to invalid or unoccupied chat.")
                return
            else:
                renamelog.exception(f"Unhandled error during FORCEJOIN check: {err}")
                return

    await msg.continue_propagation()
    

async def close_message(_: MeshRenameBot, msg: CallbackQuery) -> None:
    if msg.message.reply_to_message is not None:
        await msg.message.reply_to_message.delete()
    await msg.message.delete()
