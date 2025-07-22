import time
import asyncio
import json
import os
from typing import Union
from pyrogram import Client, types


class userin:
    track_users = {}
    total_users = set()
    total_renames = 0
    total_download_size = 0  # bytes
    total_upload_size = 0    # bytes

    STATS_FILE = "bot_stats.json"

    def __init__(self, client):
        self._client = client

    @classmethod
    def add_user(cls, user_id: int) -> None:
        cls.total_users.add(user_id)
        cls.save_stats()

    @classmethod
    def count_rename(cls) -> None:
        cls.total_renames += 1
        cls.save_stats()

    @classmethod
    def count_download(cls, size_in_bytes: int) -> None:
        cls.total_download_size += size_in_bytes
        cls.save_stats()

    @classmethod
    def count_upload(cls, size_in_bytes: int) -> None:
        cls.total_upload_size += size_in_bytes
        cls.save_stats()

    @classmethod
    def save_stats(cls) -> None:
        try:
            with open(cls.STATS_FILE, "w") as f:
                json.dump({
                    "users": list(cls.total_users),
                    "renames": cls.total_renames,
                    "download": cls.total_download_size,
                    "upload": cls.total_upload_size
                }, f)
        except Exception as e:
            print(f"[ERROR] Failed to save stats: {e}")

    @classmethod
    def load_stats(cls) -> None:
        if os.path.exists(cls.STATS_FILE):
            try:
                with open(cls.STATS_FILE, "r") as f:
                    data = json.load(f)
                    cls.total_users = set(data.get("users", []))
                    cls.total_renames = data.get("renames", 0)
                    cls.total_download_size = data.get("download", 0)
                    cls.total_upload_size = data.get("upload", 0)
            except Exception as e:
                print(f"[ERROR] Failed to load stats: {e}")

    async def get_value(self, client: Client, e: types.MessageEntity, file: bool = False, del_msg: bool = False) -> Union[None, str]:
        self.track_users[e.from_user.id] = []
        start = time.time()
        val = None

        while True:
            if (time.time() - start) >= 1e10:
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

        self.track_users.pop(e.from_user.id)
        print("val is", val)
        return val


async def interactive_input(client: Client, msg: types.MessageEntity) -> None:
    if msg.from_user.id in userin.track_users.keys():
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
