import logging
import asyncio
import math
import time
import random
import os
from typing import Union
from PIL import Image
from pyrogram import Client, filters
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
        Image.open(path).load()  # Force validation
        return path
    except Exception as e:
        renamelog.error(f"[adjust_image] Failed: {e}")
        return None

# 🔧 Set Thumbnail
async def handle_set_thumb(client: Client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    original = msg.reply_to_message
    if not original or not (original.photo or original.video or original.document):
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    media = original.photo or original.video or original.document
    path = await original.download()
    if not path or not os.path.exists(path):
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    thumb_path = None
    if original.photo:
        thumb_path = await adjust_image(path)
    else:
        duration = await get_metadata_duration(path)
        if duration < 2:
            duration = 3
        ss_path = await gen_ss(path, random.randint(1, duration))
        thumb_path = await resize_img(ss_path, 320) if ss_path else None

    if thumb_path:
        try:
            UserDB().set_thumbnail(thumb_path, user_id)
            await msg.reply_text(translator.get("THUMB_SET_SUCCESS"), quote=True)
        except Exception as e:
            renamelog.error(f"[handle_set_thumb] Save failed: {e}")
            await msg.reply_text("❌ Failed to register thumbnail.", quote=True)

        try:
            os.remove(thumb_path)
        except Exception as e:
            renamelog.warning(f"[handle_set_thumb] Temp not cleaned: {e}")
    else:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)

# ✅ Get & Rebuild Thumbnail
async def handle_get_thumb(client: Client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    thumb_path = UserDB().get_thumbnail(user_id)
    if not thumb_path or not os.path.exists(thumb_path):
        await msg.reply_text(translator.get("THUMB_NOT_FOUND"), quote=True)
        return

    try:
        rebuilt = thumb_path.replace(".jpg", "_rebuilt.jpg")
        Image.open(thumb_path).convert("RGB").save(rebuilt, "JPEG", exif=b"")
        await msg.reply_photo(rebuilt, quote=True)
        os.remove(rebuilt)
    except Exception as e:
        renamelog.error(f"[handle_get_thumb] Send failed: {e}")
        await msg.reply_text("⚠️ Thumbnail is unreadable or unsupported.", quote=True)

# 🎬 Generate Screenshot
async def gen_ss(filepath: str, ts: int) -> Union[str, None]:
    dest = os.path.dirname(filepath)
    ss_name = f"{os.path.basename(filepath)}_{round(time.time())}.jpg"
    ss_path = os.path.join(dest, ss_name)

    cmd = [
        "ffmpeg", "-loglevel", "error", "-ss", str(ts),
        "-i", filepath, "-vframes", "1", "-q:v", "2", ss_path,
    ]

    try:
        subpr = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        await subpr.communicate()
        return ss_path if os.path.exists(ss_path) else None
    except Exception as e:
        renamelog.error(f"[gen_ss] Screenshot failed: {e}")
        return None

# 🖼️ Resize Image
async def resize_img(path: str, width: int = None, height: int = None) -> Union[str, None]:
    try:
        img = Image.open(path)
        wei, hei = img.size
        wei = width or wei
        hei = height or hei
        img.thumbnail((wei, hei))
        img.save(path, "JPEG", exif=b"")
        Image.open(path).load()
        return path
    except Exception as e:
        renamelog.error(f"[resize_img] Failed: {e}")
        return None

# 🧠 Metadata Duration Extractor
async def get_metadata_duration(file_path: str) -> int:
    try:
        parser = createParser(file_path)
        if not parser:
            return 3
        metadata = extractMetadata(parser)
        return int(metadata.get("duration").seconds) if metadata and metadata.has("duration") else 3
    except Exception as e:
        renamelog.warning(f"[get_metadata_duration] Fallback: {e}")
        return 3

# 📌 Retrieve Thumbnail Logic
async def get_thumbnail(file_path: str, user_id: int = None, force_docs: bool = False) -> Union[str, None]:
    renamelog.info(f"[get_thumbnail] Fetch → file: {file_path}, user: {user_id}, docs_mode: {force_docs}")

    user_thumb = UserDB().get_thumbnail(user_id) if user_id else None
    if force_docs and user_thumb:
        return user_thumb
    if user_thumb:
        return user_thumb

    try:
        duration = await get_metadata_duration(file_path)
        path = await gen_ss(file_path, random.randint(1, max(3, duration)))
        return await resize_img(path, 320) if path else None
    except Exception as e:
        renamelog.error(f"[get_thumbnail] Gen failed: {e}")
        return None

# 🧹 Clear Thumbnail
async def handle_clr_thumb(client: Client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    UserDB().set_thumbnail(None, user_id)
    await msg.reply_text(translator.get("THUMB_CLEARED"), quote=True)


