import time
import asyncio
from typing import Union
from pyrogram import Client
from pyrogram.types import Message, CallbackQuery

# 🗂 Shared input tracker across users
track_users = {}

class userin:
    def __init__(self, client: Client):
        self._client = client

    async def get_value(
        self,
        e: Union[Message, CallbackQuery],
        file: bool = False,
        del_msg: bool = False
    ) -> Union[None, str]:
        if not hasattr(e, "from_user") or not hasattr(e.from_user, "id"):
            raise TypeError(
                f"Invalid input: expected Message or CallbackQuery with 'from_user.id', got {type(e)}"
            )

        user_id = e.from_user.id
        val = None
        msg_obj = None

        # 🔥 Pre-check for messages already queued
        user_queue = track_users.get(user_id, [])
        if user_queue:
            msg_obj = user_queue.pop(0)
        else:
            # ⏳ Wait if nothing is queued yet
            start = time.time()
            while time.time() - start < 20:
                user_queue = track_users.get(user_id, [])
                if user_queue:
                    msg_obj = user_queue.pop(0)
                    break
                await asyncio.sleep(1)

        if msg_obj:
            if msg_obj.text == "/ignore":
                val = "ignore"
            elif file and msg_obj.document:
                val = await msg_obj.download()
            elif msg_obj.text:
                val = msg_obj.text

            if val is not None and del_msg:
                try:
                    await msg_obj.delete()
                except Exception:
                    pass

        track_users.pop(user_id, None)
        print("val is", val)
        return val

# 📥 External listener that queues incoming messages immediately
async def interactive_input(client: Client, msg: Message) -> None:
    user_id = msg.from_user.id
    track_users.setdefault(user_id, []).append(msg)

    if hasattr(msg, "continue_propagation"):
        msg.continue_propagation()
