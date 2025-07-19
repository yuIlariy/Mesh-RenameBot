import time
import asyncio
from typing import Union
from pyrogram import Client, types

class userin:
    track_users = {}

    def __init__(self, client):
        self._client = client

    async def get_value(
        self,
        client: Client,
        e: Union[types.Message, types.CallbackQuery],
        file: bool = False,
        del_msg: bool = False
    ) -> Union[None, str]:
        # This function gets the new value to be set from the user in current context

        self.track_users[e.from_user.id] = []
        start = time.time()
        val = None

        # Handle Message or CallbackQuery safely
        if hasattr(e, "text") and e.text and not file:
            val = e.text
            if del_msg:
                await e.delete()
            return val
        elif hasattr(e, "data") and e.data and not file:
            val = e.data
            if del_msg:
                await e.delete()
            return val
        elif file and getattr(e, "document", None) is not None:
            val = await e.download()
            if del_msg:
                await e.delete()
            return val

        while True:
            if (time.time() - start) >= 20:
                break

            if len(self.track_users[e.from_user.id]) != 0:
                msg_obj = self.track_users[e.from_user.id].pop(0)

                # Handle ignore command
                if hasattr(msg_obj, "text") and msg_obj.text == "/ignore":
                    val = "ignore"
                    break

                if file:
                    if getattr(msg_obj, "document", None) is not None:
                        val = await msg_obj.download()
                        break
                elif hasattr(msg_obj, "text") and msg_obj.text:
                    val = msg_obj.text
                    break
                elif hasattr(msg_obj, "data") and msg_obj.data:
                    val = msg_obj.data
                    break

            await asyncio.sleep(1)

        if val is not None and del_msg and 'msg_obj' in locals():
            await msg_obj.delete()
        return val

async def interactive_input(client: Client, msg: Union[types.Message, types.CallbackQuery]) -> None:
    if msg.from_user.id in userin.track_users.keys():
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
