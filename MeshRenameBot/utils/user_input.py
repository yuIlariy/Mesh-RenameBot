import time
import asyncio
from typing import Union
from pyrogram import Client, types

# 🌐 Shared user tracking dictionary
track_users = {}

class userin:
    def __init__(self, client: Client):
        self._client = client

    async def get_value(
        self,
        e: types.Message,
        file: bool = False,
        del_msg: bool = False
    ) -> Union[None, str]:
        user_id = e.from_user.id
        track_users[user_id] = []
        start = time.time()
        val = None

        while True:
            if (time.time() - start) >= 20:
                break

            if track_users[user_id]:
                msg_obj = track_users[user_id].pop(0)

                if msg_obj.text == "/ignore":
                    val = "ignore"
                    break

                if file and msg_obj.document:
                    val = await msg_obj.download()
                    break
                else:
                    val = msg_obj.text
                    break

            await asyncio.sleep(1)

        if val is not None and del_msg:
            await msg_obj.delete()

        track_users.pop(user_id, None)
        print("val is", val)
        return val

# 🚀 Standalone input listener for importing directly
async def interactive_input(client: Client, msg: types.Message) -> None:
    user_id = msg.from_user.id

    if user_id in track_users:
        track_users[user_id].append(msg)
    else:
        track_users[user_id] = [msg]

    # Optional: only works inside a filter or middleware context
    if hasattr(msg, "continue_propagation"):
        msg.continue_propagation()
