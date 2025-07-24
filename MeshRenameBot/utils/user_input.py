import time
import os
import asyncio
from typing import Union
from pyrogram import Client, types
from MeshRenameBot.database.user_db import UserDB  # ✅ Fixed import

class userin:
    track_users = {}
    total_users = set()
    total_renames = 0
    total_download_size = 0  # bytes
    total_upload_size = 0    # bytes

    def __init__(self, client):
        self._client = client  # ✅ Fixed constructor

    @classmethod
    def add_user(cls, user_id: int) -> None:
        cls.total_users.add(user_id)

    @classmethod
    def count_rename(cls) -> None:
        cls.total_renames += 1

    @classmethod
    def count_download(cls, size_in_bytes: int) -> None:
        cls.total_download_size += size_in_bytes

    @classmethod
    def count_upload(cls, size_in_bytes: int) -> None:
        cls.total_upload_size += size_in_bytes

    @classmethod
    def update_user(cls, user_id: int, rename=False, downloaded=0, uploaded=0) -> None:
        data = UserDB().get_var("telemetry", user_id) or {}
        data["rename"] = data.get("rename", 0) + (1 if rename else 0)
        data["download"] = data.get("download", 0) + downloaded
        data["upload"] = data.get("upload", 0) + uploaded
        data["last_active"] = int(time.time())
        UserDB().set_var("telemetry", data, user_id)

    async def get_value(
        self,
        client: Client,
        e: types.MessageEntity,
        file: bool = False,
        del_msg: bool = False
    ) -> Union[None, str]:
        self.track_users[e.from_user.id] = []
        start = time.time()
        val = None

        while True:
            if (time.time() - start) >= float('inf'):  # ⏱️ no timeout 😁
                break

            if len(self.track_users[e.from_user.id]) != 0:
                msg_obj = self.track_users[e.from_user.id].pop(0)

                if msg_obj.text == "/ignore":
                    val = "ignore"
                    break

                if file:
                    if msg_obj.document is not None:
                        val = await msg_obj.download()
                        break
                else:
                    val = msg_obj.text
                    break

            await asyncio.sleep(1)

        if val is not None and del_msg:
            await msg_obj.delete()

        self.track_users.pop(e.from_user.id, None)
        print("val is", val)
        return val

async def interactive_input(client: Client, msg: types.MessageEntity) -> None:
    if msg.from_user.id in userin.track_users:
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
