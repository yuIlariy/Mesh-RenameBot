from .mongo_db import MongoDB
from ..core.get_config import get_var
import os, datetime, json
from typing import Union

class UserDB(MongoDB):
    shared_users = {}

    # Mode constants (including the one you were missing)
    MODE_SAME_AS_SENT = 0
    MODE_AS_DOCUMENT = 1
    MODE_AS_GMEDIA = 2
    MODE_RENAME_WITH_COMMAND = 3

    def __init__(self, dburl=None):
        if dburl is None:
            dburl = os.environ.get("DATABASE_URL", None)
            if dburl is None:
                dburl = get_var("DATABASE_URL")
        super().__init__(dburl)

    def get_var(self, var: str, user_id: int) -> Union[None, str]:
        user_id = str(user_id)
        users = self._db.mesh_rename

        # fetch into a list so we can use len() instead of count()
        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            jdata = json.loads(docs[0]["json_data"])
            return jdata.get(var)
        return None

    def set_var(self, var: str, value: Union[int, str], user_id: int) -> None:
        user_id = str(user_id)
        users = self._db.mesh_rename

        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            doc = docs[0]
            jdata = json.loads(doc["json_data"])
            jdata[var] = value
            users.update_one(
                {"_id": doc["_id"]},
                {"$set": {"json_data": json.dumps(jdata)}}
            )
        else:
            jdata = {var: value}
            users.insert_one({
                "user_id": user_id,
                "json_data": json.dumps(jdata),
                "file_choice": 0,
                "thumbnail": None
            })

    def get_thumbnail(self, user_id: int) -> Union[str, bool]:
        user_id = str(user_id)
        users = self._db.mesh_rename

        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            thumb = docs[0].get("thumbnail")
            if not thumb:
                return False

            # ensure userdata/<user_id>/ exists
            base = os.path.join(os.getcwd(), "userdata", user_id)
            os.makedirs(base, exist_ok=True)

            thumb_path = os.path.join(base, "thumbnail.jpg")
            with open(thumb_path, "wb") as f:
                f.write(thumb)
            return thumb_path

        return False

    def set_thumbnail(self, thumbnail: bytes, user_id: int) -> bool:
        user_id = str(user_id)
        users = self._db.mesh_rename

        if isinstance(thumbnail, str):
            with open(thumbnail, "rb") as f:
                thumbnail = f.read()

        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            users.update_one(
                {"user_id": user_id},
                {"$set": {"thumbnail": thumbnail}}
            )
        else:
            users.insert_one({
                "user_id": user_id,
                "thumbnail": thumbnail,
                "json_data": json.dumps({}),
                "file_choice": 0
            })

        return True

    def set_mode(self, mode: int, user_id: int) -> bool:
        user_id = str(user_id)
        users = self._db.mesh_rename

        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            users.update_one(
                {"user_id": user_id},
                {"$set": {"file_choice": mode}}
            )
        else:
            users.insert_one({
                "user_id": user_id,
                "file_choice": mode,
                "thumbnail": None,
                "json_data": json.dumps({})
            })
        return True

    def get_mode(self, user_id: int) -> int:
        user_id = str(user_id)
        users = self._db.mesh_rename

        docs = list(users.find({"user_id": user_id}))
        if len(docs) > 0:
            return docs[0].get("file_choice", self.MODE_SAME_AS_SENT)
        return self.MODE_SAME_AS_SENT
