import time
import asyncio
from typing import Union
from pyrogram import Client, types
from pyrogram.types import Message, CallbackQuery

# 🗂 Global dictionary to track user input
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
        # 🛡️ Validate input type
        if not hasattr(e, "from_user") or not hasattr(e.from_user, "id"):
            raise TypeError(
                f"Invalid input to get_value: expected Message or CallbackQuery with 'from_user.id', got {type(e)}"
            )

        user_id = e.from_user.id
        val = None
        start = time.time()

        while time.time() - start < 20:
            if track_users.get(user_id):
                msg_obj = track_users[user_id].pop(0)

                if msg_obj.text == "/ignore":
                    val = "ignore"
                    break

                if file and msg_obj.document:
                    val = await msg_obj.download()
                    break
                elif msg_obj.text:
                    val = msg_obj.text
                    break

            await asyncio.sleep(1)

        if val is not None and del_msg:
            try:
                await msg_obj.delete()
            except Exception:
                pass

        track_users.pop(user_id, None)
        print("val is", val)
        return val

# 📥 Standalone input listener — to be imported directly
async def interactive_input(client: Client, msg: Message) -> None:
    user_id = msg.from_user.id

    if user_id in track_users:
        track_users[user_id].append(msg)
    else:
        track_users[user_id] = [msg]

    # 🧩 Optional: Use only in middleware/filter chains
    if hasattr(msg, "continue_propagation"):
        msg.continue_propagation()
