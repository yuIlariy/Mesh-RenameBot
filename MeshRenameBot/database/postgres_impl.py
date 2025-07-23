# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

import json
import os
import logging
from typing import Union

from ..core.get_config import get_var
from .postgres_db import DataBaseHandle

renamelog = logging.getLogger(__name__)


class UserDB:
    shared_users = {}

    MODE_SAME_AS_SENT = 0
    MODE_AS_DOCUMENT = 1
    MODE_AS_GMEDIA = 2
    MODE_RENAME_WITH_COMMAND = 3
    MODE_RENAME_WITHOUT_COMMAND = 4

    def __init__(self, dburl: str = None) -> None:
        if dburl is None:
            dburl = os.environ.get("DATABASE_URL") or get_var("DATABASE_URL")

        self.db = DataBaseHandle(dburl)

        cursor_pair = self.db.scur()
        if not cursor_pair:
            renamelog.error("Unable to initialize DB schema.")
            return
        cur, conn = cursor_pair

        table = """CREATE TABLE IF NOT EXISTS ttk_users(
            id SERIAL PRIMARY KEY NOT NULL,
            user_id BIGINT NOT NULL,
            json_data TEXT NULL,
            thumbnail BYTEA DEFAULT NULL,
            is_premium SMALLINT NOT NULL DEFAULT 0,
            tasks_count INTEGER NOT NULL DEFAULT 0,
            file_choice SMALLINT NOT NULL DEFAULT 0
        );"""
        
        try:
            cur.execute(table)
        except Exception as e:
            renamelog.warning(f"Table creation skipped or errored: {e}")

        self.db.ccur(cur, conn)

    def get_var(self, var: str, user_id: int) -> Union[None, str]:
        user_id = str(user_id)
        cached = self.shared_users.get(user_id)
        if cached:
            return cached.get(var)

        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return None
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT json_data FROM ttk_users WHERE user_id=%s;", (user_id,))
            user = cur.fetchone()
            if not user or not user.get("json_data"):
                return None
            jdata = json.loads(user["json_data"])
            self.shared_users[user_id] = jdata
            return jdata.get(var)
        finally:
            self.db.ccur(cur, conn)

    def set_var(self, var: str, value: Union[int, str], user_id: int) -> None:
        user_id = str(user_id)
        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT json_data FROM ttk_users WHERE user_id=%s;", (user_id,))
            row = cur.fetchone()

            jdata = {}
            if row and row.get("json_data"):
                jdata = json.loads(row["json_data"])
            jdata[var] = value
            self.shared_users[user_id] = jdata

            if row:
                cur.execute("UPDATE ttk_users SET json_data = %s WHERE user_id=%s;",
                            (json.dumps(jdata), user_id))
            else:
                cur.execute("INSERT INTO ttk_users(user_id, json_data) VALUES (%s, %s);",
                            (user_id, json.dumps(jdata)))
        finally:
            self.db.ccur(cur, conn)

    def get_all_users(self) -> list[int]:
        cursor_pair = self.db.scur()
        if not cursor_pair:
            return []
        cur, conn = cursor_pair

        try:
            # ✅ Only users who have telemetry set in their JSON
            cur.execute("SELECT user_id, json_data FROM ttk_users WHERE json_data IS NOT NULL;")
            rows = cur.fetchall()
            return [
                int(row[0]) for row in rows
                if row[1] and '"telemetry"' in row[1]
            ]
        finally:
            self.db.ccur(cur, conn)
        

    def get_thumbnail(self, user_id: int) -> Union[str, bool]:
        user_id = str(user_id)
        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return False
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT thumbnail FROM ttk_users WHERE user_id=%s;", (user_id,))
            row = cur.fetchone()
            if not row or row["thumbnail"] is None:
                return False

            path = os.path.join(os.getcwd(), 'userdata', user_id)
            os.makedirs(path, exist_ok=True)
            thumb_path = os.path.join(path, "thumbnail.jpg")

            with open(thumb_path, "wb") as f:
                f.write(row["thumbnail"])
            return thumb_path
        finally:
            self.db.ccur(cur, conn)

    def set_thumbnail(self, thumbnail: bytes, user_id: int) -> bool:
        user_id = str(user_id)
        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return False
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT 1 FROM ttk_users WHERE user_id=%s;", (user_id,))
            if cur.rowcount > 0:
                cur.execute("UPDATE ttk_users SET thumbnail=%s WHERE user_id=%s;",
                            (thumbnail, user_id))
            else:
                cur.execute("INSERT INTO ttk_users(user_id, json_data, thumbnail) VALUES (%s, '{}', %s);",
                            (user_id, thumbnail))
            return True
        finally:
            self.db.ccur(cur, conn)

    def set_mode(self, mode: int, user_id: int) -> None:
        user_id = str(user_id)
        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT 1 FROM ttk_users WHERE user_id=%s;", (user_id,))
            if cur.rowcount > 0:
                cur.execute("UPDATE ttk_users SET file_choice = %s WHERE user_id=%s;", (mode, user_id))
            else:
                cur.execute("INSERT INTO ttk_users(user_id, file_choice) VALUES (%s, %s);", (user_id, mode))
        finally:
            self.db.ccur(cur, conn)

    def get_mode(self, user_id: int) -> int:
        user_id = str(user_id)
        cursor_pair = self.db.scur(dictcur=True)
        if not cursor_pair:
            return self.MODE_SAME_AS_SENT
        cur, conn = cursor_pair

        try:
            cur.execute("SELECT file_choice FROM ttk_users WHERE user_id=%s;", (user_id,))
            row = cur.fetchone()
            if row:
                return row["file_choice"]
        finally:
            self.db.ccur(cur, conn)

        self.set_mode(self.MODE_SAME_AS_SENT, user_id)
        return self.MODE_SAME_AS_SENT
