from typing import Union
from pyrogram.types.user_and_chats import user
from aiofiles import os as aos
from pyrogram.types.user_and_chats.user import User
from ..database.user_db import UserDB
from PIL import Image
import os
import asyncio
import logging
import time
import random
from ..database.user_db import UserDB
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pyrogram.types import Message
from ..translations import Translator

# TODO trans pending

renamelog = logging.getLogger(__name__)

# 📦 Image Preparation
async def adjust_image(path: str) -> Union[str, None]:
    try:
        im = Image.open(path)
        im.convert("RGB").save(path, "JPEG")
        im = Image.open(path)
        im.thumbnail((320, 320), Image.Resampling.LANCZOS)
        im.save(path, "JPEG")
        renamelog.info(f"Image adjusted at: {path}")
        return path
    except Exception as e:
        renamelog.error(f"Failed to adjust image: {e}")
        return None

# 🔧 Set Thumbnail
async def handle_set_thumb(client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    original_message = msg.reply_to_message
    if original_message is None:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    if original_message.photo is not None:
        path = await original_message.download()
        path = await adjust_image(path)
        if path is not None:
            UserDB().set_thumbnail(path, user_id)
            await msg.reply_text(translator.get("THUMB_SET_SUCCESS"), quote=True)

            try:
                await aos.remove(path)
            except Exception as e:
                renamelog.warning(f"Failed to remove temp thumbnail: {e}")
        else:
            await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
    else:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)

# 🎯 Get Thumbnail
async def handle_get_thumb(client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    renamelog.info("Getting thumbnail for user: %s", user_id)
    thumb_path = UserDB().get_thumbnail(user_id)

    if not thumb_path or not os.path.exists(thumb_path):
        await msg.reply_text(translator.get("THUMB_NOT_FOUND"), quote=True)
    else:
        await msg.reply_photo(thumb_path, quote=True)
        try:
            os.remove(thumb_path)
        except Exception as e:
            renamelog.warning(f"Failed to delete used thumbnail: {e}")

# 🎬 Generate Screenshot
async def gen_ss(filepath, ts, opfilepath=None):
    destination = os.path.dirname(filepath)
    ss_name = f"{os.path.basename(filepath)}_{round(time.time())}.jpg"
    ss_path = os.path.join(destination, ss_name)

    cmd = [
        "ffmpeg", "-loglevel", "error", "-ss", str(ts),
        "-i", str(filepath), "-vframes", "1", "-q:v", "2", ss_path,
    ]

    try:
        subpr = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        spipe, epipe = await subpr.communicate()
        renamelog.info(f"Screenshot stdout: {spipe.decode().strip()}")
        renamelog.info(f"Screenshot error: {epipe.decode().strip()}")
    except Exception as e:
        renamelog.error(f"Screenshot generation failed: {e}")
        return None

    return ss_path

# 🖼️ Resize Image
async def resize_img(path, width=None, height=None):
    try:
        img = Image.open(path)
        wei, hei = img.size
        wei = width if width is not None else wei
        hei = height if height is not None else hei
        img.thumbnail((wei, hei))
        img.save(path, "JPEG")
        return path
    except Exception as e:
        renamelog.error(f"Failed to resize image: {e}")
        return None

# 📌 Retrieve Thumbnail Logic
async def get_thumbnail(file_path, user_id=None, force_docs=False):
    print(file_path, "-", user_id, "-", force_docs)

    metadata = extractMetadata(createParser(file_path))
    duration = metadata.get("duration", 3)

    user_thumb = None
    if user_id:
        user_thumb = UserDB().get_thumbnail(user_id)

    if force_docs:
        return user_thumb if user_thumb else None

    if user_thumb:
        return user_thumb

    try:
        path = await gen_ss(file_path, random.randint(2, duration))
        path = await resize_img(path, 320)
        return path
    except Exception as e:
        renamelog.error(f"Error generating fallback thumbnail: {e}")
        return None

# 🧹 Clear Thumbnail
async def handle_clr_thumb(client, msg: Message):
    user_id = msg.from_user.id
    udb = UserDB()
    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)

    udb.set_thumbnail(None, user_id)
    await msg.reply_text(translator.get("THUMB_CLEARED"), quote=True)
