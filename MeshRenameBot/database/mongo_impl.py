from .mongo_db import MongoDB
from ..core.get_config import get_var
import os, json
from typing import Union

class UserDB(MongoDB):
    shared_users = {}

    MODE_SAME_AS_SENT           = 0
    MODE_AS_DOCUMENT            = 1
    MODE_AS_GMEDIA              = 2
    MODE_RENAME_WITH_COMMAND    = 3
    MODE_RENAME_WITHOUT_COMMAND = 4

    def __init__(self, dburl: str = None):
        if dburl is None:
            dburl = os.environ.get("DATABASE_URL") or get_var("DATABASE_URL")
        super().__init__(dburl)
        # 🔍 Ensure index on user_id for lightning-fast lookups:
        self._db.mesh_rename.create_index("user_id", unique=True)

    def get_var(self, var: str, user_id: int) -> Union[None, str]:
        user_id = str(user_id)

        # 1. Try in‐memory cache
        cache = self.shared_users.get(user_id)
        if cache and var in cache:
            return cache[var]

        # 2. One round‐trip to Mongo (only fetch json_data)
        doc = self._db.mesh_rename.find_one(
            {"user_id": user_id},
            {"json_data": 1, "_id": 0}
        )
        if not doc or not doc.get("json_data"):
            return None

        data = json.loads(doc["json_data"])
        self.shared_users[user_id] = data   # cache full JSON for future
        return data.get(var)

    def set_var(self, var: str, value: Union[int, str], user_id: int) -> None:
        user_id = str(user_id)
        # Update the JSON in one upsert operation
        # Uses MongoDB aggregation pipeline to modify a nested JSON string
        # Simpler: pull existing JSON, mutate it in Python, then upsert
        doc = self._db.mesh_rename.find_one(
            {"user_id": user_id},
            {"json_data": 1}
        )

        if doc and doc.get("json_data"):
            data = json.loads(doc["json_data"])
        else:
            data = {}

        data[var] = value
        json_str = json.dumps(data)

        self._db.mesh_rename.update_one(
            {"user_id": user_id},
            {"$set": {
                "json_data": json_str
            }},
            upsert=True
        )
        self.shared_users[user_id] = data

    def get_mode(self, user_id: int) -> int:
        user_id = str(user_id)
        # Only fetch the file_choice field
        doc = self._db.mesh_rename.find_one(
            {"user_id": user_id},
            {"file_choice": 1, "_id": 0}
        )
        if doc and "file_choice" in doc:
            return doc["file_choice"]
        # initialize default if missing
        self.set_mode(self.MODE_SAME_AS_SENT, user_id)
        return self.MODE_SAME_AS_SENT

    def set_mode(self, mode: int, user_id: int) -> bool:
        user_id = str(user_id)
        self._db.mesh_rename.update_one(
            {"user_id": user_id},
            {"$set": {"file_choice": mode}},
            upsert=True
        )
        return True

    def get_thumbnail(self, user_id: int) -> Union[str, bool]:
        user_id = str(user_id)
        doc = self._db.mesh_rename.find_one(
            {"user_id": user_id},
            {"thumbnail": 1, "_id": 0}
        )
        thumb = doc.get("thumbnail") if doc else None
        if not thumb:
            return False

        folder = os.path.join(os.getcwd(), "userdata", user_id)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, "thumbnail.jpg")

        with open(path, "wb") as f:
            f.write(thumb)
        return path

    def set_thumbnail(self, thumbnail: bytes, user_id: int) -> bool:
        user_id = str(user_id)
        if isinstance(thumbnail, str):
            with open(thumbnail, "rb") as f:
                thumbnail = f.read()

        self._db.mesh_rename.update_one(
            {"user_id": user_id},
            {"$set": {"thumbnail": thumbnail}},
            upsert=True
        )
        return True
