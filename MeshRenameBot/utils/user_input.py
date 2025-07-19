import time
import asyncio
from typing import Union
from pyrogram import Client, types
import pyrogram

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
        self.track_users[e.from_user.id] = []
        start = time.time()
        val = None

        # Handle Message or CallbackQuery safely
        # Only delete after all editing or sending is done!
        if hasattr(e, "text") and e.text and not file:
            val = e.text
            if del_msg and isinstance(e, types.Message):
                try:
                    await e.delete()
                except pyrogram.errors.RPCError:
                    pass
            return val
        elif hasattr(e, "data") and e.data and not file:
            val = e.data
            # Don't delete before editing; generally, leave inline messages unless you want to remove the menu.
            if del_msg and isinstance(e, types.CallbackQuery) and hasattr(e, "message") and isinstance(e.message, types.Message):
                try:
                    await e.message.delete()
                except pyrogram.errors.RPCError:
                    pass
            return val
        elif file and getattr(e, "document", None) is not None:
            val = await e.download()
            if del_msg and isinstance(e, types.Message):
                try:
                    await e.delete()
                except pyrogram.errors.RPCError:
                    pass
            elif del_msg and isinstance(e, types.CallbackQuery) and hasattr(e, "message") and isinstance(e.message, types.Message):
                try:
                    await e.message.delete()
                except pyrogram.errors.RPCError:
                    pass
            return val

        msg_obj = None
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

        # Only delete after all processing is done
        if val is not None and del_msg and msg_obj is not None:
            if isinstance(msg_obj, types.Message):
                try:
                    await msg_obj.delete()
                except pyrogram.errors.RPCError:
                    pass
            elif isinstance(msg_obj, types.CallbackQuery) and hasattr(msg_obj, "message") and isinstance(msg_obj.message, types.Message):
                try:
                    await msg_obj.message.delete()
                except pyrogram.errors.RPCError:
                    pass

        return val

async def interactive_input(client: Client, msg: Union[types.Message, types.CallbackQuery]) -> None:
    if msg.from_user.id in userin.track_users.keys():
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
