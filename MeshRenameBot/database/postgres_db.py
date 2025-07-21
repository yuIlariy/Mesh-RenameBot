# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

import logging
import time
from typing import Optional

import psycopg2
import psycopg2.extras
from psycopg2.pool import SimpleConnectionPool

renamelog = logging.getLogger(__name__)

class DataBaseHandle:
    _pool: Optional[SimpleConnectionPool] = None

    def __init__(self, dburl: str = None, minconn: int = 1, maxconn: int = 10) -> None:
        """Initialize the connection pool.

        Args:
            dburl (str, optional): The database URI to connect to.
            minconn (int): Minimum connections to maintain in the pool.
            maxconn (int): Maximum connections allowed in the pool.
        """
        if not dburl:
            renamelog.warning("Database URL is not provided.")
            self._block = True
            return

        self._dburl = dburl
        self._block = False

        try:
            if not DataBaseHandle._pool:
                DataBaseHandle._pool = SimpleConnectionPool(
                    minconn, maxconn, dsn=self._dburl, sslmode='require'
                )
                renamelog.info("Connection pool established.")
        except psycopg2.Error as e:
            renamelog.error(f"Failed to initialize connection pool: {e}")
            self._block = True

    def scur(self, dictcur: bool = False) -> Optional[psycopg2.extensions.cursor]:
        """Acquire a cursor from the pool.

        Args:
            dictcur (bool): Use DictCursor if True.

        Returns:
            Optional[cursor]: A cursor object or None if connection fails.
        """
        if self._block or not DataBaseHandle._pool:
            return None

        for attempt in range(5):
            try:
                conn = DataBaseHandle._pool.getconn()
                if dictcur:
                    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                else:
                    cur = conn.cursor()
                return cur, conn
            except psycopg2.InterfaceError as e:
                renamelog.warning(f"Cursor acquisition failed (attempt {attempt}): {e}")
                time.sleep(1)
        return None

    def ccur(self, cursor: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection) -> None:
        """Commit and close the cursor, release the connection back to the pool.

        Args:
            cursor: The cursor to close.
            conn: The connection to release.
        """
        if cursor and conn:
            try:
                cursor.close()
                conn.commit()
                DataBaseHandle._pool.putconn(conn)
            except psycopg2.Error as e:
                renamelog.error(f"Error releasing connection: {e}")
                DataBaseHandle._pool.putconn(conn, close=True)

    def close_pool(self):
        """Closes all connections in the pool."""
        if DataBaseHandle._pool:
            DataBaseHandle._pool.closeall()
            renamelog.info("All connections in pool closed.")
