import logging
import asyncio
import math
import time
import random
import os
from typing import Union
from PIL import Image
from pyrogram import StopTransmission, Client, filters
from pyrogram.types import Message
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from aiofiles import os as aos
from ..database.user_db import UserDB
from ..translations import Translator

renamelog = logging.getLogger(__name__)

# 📦 Image Preparation
async def adjust_image(path: str) -> Union[str, None]:
    try:
        im = Image.open(path)
        im.convert("RGB").save(path, "JPEG", exif=b"")
        im.thumbnail((320, 320), Image.Resampling.LANCZOS)
        im.save(path, "JPEG", exif=b"")
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

    media = original_message.photo or original_message.video or original_message.document
    if not media:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    path = await original_message.download()
    if not path or not os.path.exists(path):
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    thumb_path = None
    if original_message.photo:
        thumb_path = await adjust_image(path)
    else:
        duration = await get_metadata_duration(path)
        thumb_path = await gen_ss(path, random.randint(2, duration))
        if thumb_path:
            thumb_path = await resize_img(thumb_path, 320)

    if thumb_path:
        UserDB().set_thumbnail(thumb_path, user_id)
        await msg.reply_text(translator.get("THUMB_SET_SUCCESS"), quote=True)
        try:
            os.remove(thumb_path)
        except Exception as e:
            renamelog.warning(f"Failed to remove temp thumbnail: {e}")
    else:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)

# ✅ PATCHED: Robust Get Thumbnail
async def handle_get_thumb(client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    renamelog.info("Getting thumbnail for user: %s", user_id)
    thumb_path = UserDB().get_thumbnail(user_id)

    if not thumb_path or not os.path.exists(thumb_path):
        await msg.reply_text(translator.get("THUMB_NOT_FOUND"), quote=True)
        return

    # Validation attempt before sending
    try:
        with Image.open(thumb_path) as img:
            img.verify()
        await msg.reply_photo(thumb_path, quote=True)
    except Exception as e:
        renamelog.error(f"[getthumb] Failed image verification/send: {e}")
        await msg.reply_text("⚠️ Thumbnail is invalid or corrupted.", quote=True)

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

    return ss_path if os.path.exists(ss_path) else None

# 🖼️ Resize Image
async def resize_img(path, width=None, height=None):
    try:
        img = Image.open(path)
        wei, hei = img.size
        wei = width if width is not None else wei
        hei = height if height is not None else hei
        img.thumbnail((wei, hei))
        img.save(path, "JPEG", exif=b"")
        return path
    except Exception as e:
        renamelog.error(f"Failed to resize image: {e}")
        return None

# 🧠 Metadata Duration Extractor
async def get_metadata_duration(file_path):
    try:
        metadata = extractMetadata(createParser(file_path))
        return metadata.get("duration", 3)
    except Exception as e:
        renamelog.warning(f"Failed to get duration: {e}")
        return 3

# 📌 Retrieve Thumbnail Logic
async def get_thumbnail(file_path, user_id=None, force_docs=False):
    renamelog.info(f"Retrieve thumbnail → file: {file_path} | user: {user_id} | force_docs: {force_docs}")

    user_thumb = None
    if user_id:
        user_thumb = UserDB().get_thumbnail(user_id)
        if force_docs and user_thumb:
            return user_thumb

    if user_thumb:
        return user_thumb

    try:
        duration = await get_metadata_duration(file_path)
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

