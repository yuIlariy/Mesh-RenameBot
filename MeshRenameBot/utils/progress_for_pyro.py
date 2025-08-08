import logging
import asyncio
import math
import time
from pyrogram import StopTransmission
from .human_format import human_readable_bytes, human_readable_timedelta
from ..core.get_config import get_var
from ..maneuvers.ExecutorManager import ExecutorManager

renamelog = logging.getLogger(__name__)


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start,
    time_out,
    client,
    uid,
    markup=None
):
    now = time.time()
    diff = now - start

    if diff < 1:
        return

    eo = ExecutorManager()
    if uid in eo.canceled_uids:
        raise StopTransmission()

    if round(diff % time_out) == 0 or current == total:
        percentage = current * 100 / total
        elapsed_time = round(diff)
        speed = current / elapsed_time
        time_to_completion = round((total - current) / speed)
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = human_readable_timedelta(elapsed_time)
        estimated_total_time = human_readable_timedelta(estimated_total_time)

        completed = human_readable_bytes(current)
        total_size = human_readable_bytes(total)
        speed_display = human_readable_bytes(speed)
        eta_display = estimated_total_time if estimated_total_time != '' else "0 seconds"
        percent_display = round(percentage, 2)

        speed_icon = "🚀" if speed >= 8 * 1024 * 1024 else "🚨"

        # Auto-colored emoji bar
        total_segments = 10
        filled = math.floor((percentage / 100) * total_segments)
        empty = total_segments - filled

        if percentage < 34:
            bar_emoji = "🔴"
        elif percentage < 67:
            bar_emoji = "🟡"
        else:
            bar_emoji = "🟢"

        emoji_bar = bar_emoji * filled + "⬜" * empty

        tmp = f"""{ud_type}\n
📊 {emoji_bar} {percent_display}%
<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣

┃    🗂️ ᴄᴏᴍᴘʟᴇᴛᴇᴅ: {completed}
┃    📦 ᴛᴏᴛᴀʟ ꜱɪᴢᴇ: {total_size}
┃    🔋 ꜱᴛᴀᴛᴜꜱ: {percent_display}%
┃    {speed_icon} ꜱᴘᴇᴇᴅ: {speed_display}/s
┃    ⏰ ᴇᴛᴀ: {eta_display}

╰━━━━━━━━━━━━━━━━➣
</b>"""

        try:
            if not message.photo:
                await message.edit_text(
                    text=tmp,
                    reply_markup=markup
                )
            else:
                await message.edit_caption(
                    caption=tmp,
                    reply_markup=markup
                )
            await asyncio.sleep(1)
        except:
            pass



