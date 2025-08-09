from typing import Union, Optional
from pyrogram.types.user_and_chats.user import User
from aiofiles import os as aos
import aiofiles
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

renamelog = logging.getLogger(__name__)


async def adjust_image(path: str) -> Optional[str]:
    try:
        im = Image.open(path)
        im.convert("RGB").save(path, "JPEG")
        im = Image.open(path)
        im.thumbnail((320, 320), Image.Resampling.LANCZOS)
        im.save(path, "JPEG")
        return path
    except Exception as e:
        renamelog.error(f"Error adjusting image: {e}")
        return None

# --- FIX START: New asynchronous copy function ---
async def async_copy_file(src: str, dest: str):
    """Asynchronously copies a file from source to destination."""
    async with aiofiles.open(src, mode='rb') as infile:
        async with aiofiles.open(dest, mode='wb') as outfile:
            while True:
                chunk = await infile.read(65536)  # Read in 64KB chunks
                if not chunk:
                    break
                await outfile.write(chunk)
# --- FIX END ---


async def handle_set_thumb(client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    original_message = msg.reply_to_message
    if original_message is None or not original_message.photo:
        await msg.reply_text(translator.get("THUMB_REPLY_TO_MEDIA"), quote=True)
        return

    old_thumb_path = UserDB().get_thumbnail(user_id)
    if old_thumb_path and os.path.exists(old_thumb_path):
        try:
            await aos.remove(old_thumb_path)
        except Exception as e:
            renamelog.warning(f"Failed to remove old thumbnail: {e}")
    
    download_path = None
    try:
        download_path = await original_message.download(
            file_name=f"downloads/{user_id}_{random.randint(1000, 9999)}.jpg"
        )
        
        adjusted_path = await adjust_image(download_path)

        if adjusted_path is None:
            await msg.reply_text("Could not adjust the image.", quote=True) # Fallback message
            return

        user_data_dir = os.path.join("userdata", str(user_id))
        await aos.makedirs(user_data_dir, exist_ok=True)
        permanent_path = os.path.join(user_data_dir, "thumbnail.jpg")

        # --- FIX START: Use the new async_copy_file function ---
        await async_copy_file(adjusted_path, permanent_path)
        # --- FIX END ---

        UserDB().set_thumbnail(permanent_path, msg.from_user.id)
        
        await msg.reply_text(translator.get("THUMB_SET_SUCCESS"), quote=True)

    except Exception as e:
        renamelog.exception(f"Failed to set thumbnail: {e}")
        await msg.reply_text("Failed to set thumbnail. Please try again.", quote=True)
    finally:
        if download_path and os.path.exists(download_path):
            try:
                await aos.remove(download_path)
            except Exception as e:
                renamelog.warning(f"Failed to remove temporary thumbnail file: {e}")


async def handle_get_thumb(client, msg: Message):
    user_id = msg.from_user.id
    user_locale = UserDB().get_var("locale", user_id)
    translator = Translator(user_locale)

    renamelog.info("Getting Thumbnail")
    thumb_path = UserDB().get_thumbnail(msg.from_user.id)
    
    if thumb_path and os.path.exists(thumb_path):
        await msg.reply_photo(thumb_path, quote=True)
    else:
        await msg.reply(translator.get("THUMB_NOT_FOUND"), quote=True)


async def gen_ss(filepath, ts, opfilepath=None):
    source = filepath
    destination = os.path.dirname(source)
    ss_name = str(os.path.basename(source)) + "_" + str(round(time.time())) + ".jpg"
    ss_path = os.path.join(destination, ss_name)

    cmd = [
        "ffmpeg",
        "-loglevel",
        "error",
        "-ss",
        str(ts),
        "-i",
        str(source),
        "-vframes",
        "1",
        "-q:v",
        "2",
        str(ss_path),
    ]

    subpr = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    spipe, epipe = await subpr.communicate()
    epipe = epipe.decode().strip()
    spipe = spipe.decode().strip()
    renamelog.info("Stdout Pipe :- {}".format(spipe))
    renamelog.info("Error Pipe :- {}".format(epipe))

    return ss_path


async def resize_img(path, width=None, height=None):
    img = Image.open(path)
    wei, hei = img.size

    wei = width if width is not None else wei
    hei = height if height is not None else hei

    img.thumbnail((wei, hei))

    img.save(path, "JPEG")
    return path


async def get_thumbnail(file_path, user_id=None, force_docs=False):
    print(file_path, "-", user_id, "-", force_docs)
    metadata = extractMetadata(createParser(file_path))
    try:
        duration = metadata.get("duration")
    except:
        duration = 3

    if user_id is not None:
        user_thumb = UserDB().get_thumbnail(user_id)
        if force_docs:
            if user_thumb:
                if os.path.exists(user_thumb):
                    return user_thumb
                else:
                    return None
            else:
                return None
        else:
            if user_thumb:
                if os.path.exists(user_thumb):
                    return user_thumb
                else:
                    path = await gen_ss(file_path, random.randint(2, duration.seconds))
                    path = await resize_img(path, 320)
                    return path
            else:
                path = await gen_ss(file_path, random.randint(2, duration.seconds))
                path = await resize_img(path, 320)
                return path
    else:
        if force_docs:
            return None

        path = await gen_ss(file_path, random.randint(2, duration.seconds))
        path = await resize_img(path, 320)
        return path


async def handle_clr_thumb(client, msg):
    user_id = msg.from_user.id
    udb = UserDB()
    user_locale = udb.get_var("locale", user_id)
    translator = Translator(user_locale)
    
    thumb_path = udb.get_thumbnail(user_id)
    if thumb_path and os.path.exists(thumb_path):
        try:
            await aos.remove(thumb_path)
            renamelog.info(f"Removed thumbnail for user {user_id}")
        except Exception as e:
            renamelog.warning(f"Failed to remove thumbnail file for user {user_id}: {e}")
    
    udb.set_thumbnail(None, msg.from_user.id)
    await msg.reply_text(translator.get("THUMB_CLEARED"), quote=True)



