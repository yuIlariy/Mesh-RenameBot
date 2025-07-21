from .mongo_db import MongoDB
from ..core.get_config import get_var
import os, datetime, json
from typing import Union

class UserDB(MongoDB):
    shared_users = {}

    def __init__(self, dburl=None):
        if dburl is None:
            dburl = os.environ.get("DATABASE_URL", None)
            if dburl is None:
                dburl = get_var("DATABASE_URL")
        super().__init__(dburl)

    def get_var(self, var: str, user_id: int) -> Union[None, str]:
        user_id = str(user_id)
        db = self._db
        users = db.mesh_rename

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            user = res[0]
            jdata = json.loads(user["json_data"])
            return jdata.get(var)
        else:
            return None

    def set_var(self, var: str, value: Union[int, str], user_id: int) -> None:
        user_id = str(user_id)
        db = self._db
        users = db.mesh_rename

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            user = res[0]
            jdata = json.loads(user["json_data"])
            jdata[var] = value
            users.update_one({"_id": user["_id"]}, {"$set": {"json_data": json.dumps(jdata)}})
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
        db = self._db
        users = db.mesh_rename

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            row = res[0]
            if row["thumbnail"] is None:
                return False
            else:
                path = os.path.join(os.getcwd(), 'userdata', user_id)
                os.makedirs(path, exist_ok=True)
                thumb_path = os.path.join(path, "thumbnail.jpg")
                with open(thumb_path, "wb") as rfile:
                    rfile.write(row["thumbnail"])
                return thumb_path
        else:
            return False

    def set_thumbnail(self, thumbnail: bytes, user_id: int) -> bool:
        user_id = str(user_id)
        db = self._db
        users = db.mesh_rename

        if isinstance(thumbnail, str):
            with open(thumbnail, "rb") as f:
                thumbnail = f.read()

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            users.update_one({"user_id": user_id}, {"$set": {"thumbnail": thumbnail}})
        else:
            users.insert_one({
                "user_id": user_id,
                "thumbnail": thumbnail,
                "json_data": json.dumps({}),
                "file_choice": 0
            })

        return True

    MODE_SAME_AS_SENT = 0
    MODE_AS_DOCUMENT = 1
    MODE_AS_GMEDIA = 2

    def set_mode(self, mode: int, user_id: int) -> None:
        user_id = str(user_id)
        db = self._db
        users = db.mesh_rename

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            users.update_one({"user_id": user_id}, {"$set": {"file_choice": mode}})
        else:
            users.insert_one({
                "user_id": user_id,
                "file_choice": mode,
                "thumbnail": None,
                "json_data": json.dumps({})
            })

    def get_mode(self, user_id: int) -> int:
        user_id = str(user_id)
        db = self._db
        users = db.mesh_rename

        res = list(users.find({"user_id": user_id}))
        if len(res) > 0:
            row = res[0]
