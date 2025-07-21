import re
import os
import logging
from urllib.parse import urlparse
from typing import AbstractSet
from pymongo import MongoClient
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MongoDB:
    """
    Base class for MongoDB access.
    - dburl: full MongoDB URI (e.g. mongodb+srv://...)
    - db_name: optional override; if omitted, we try:
        1. path of the URI (mongodb://host:port/dbname)
        2. env var DATABASE_NAME
        3. fallback to "TTKDB"
    """

    def __init__(self, dburl: str = None, db_name: str = None) -> None:
        # 1. Determine URI
        dburl = dburl or os.environ.get("DATABASE_URL")
        if not dburl:
            raise ValueError(
                "MongoDB URI must be provided via the `dburl` argument "
                "or the `DATABASE_URL` environment variable."
            )

        # 2. Connect & verify
        try:
            self._client = MongoClient(dburl, serverSelectionTimeoutMS=5000)
            # ping to fail early if credentials/host are wrong
            self._client.admin.command("ping")
            logger.info("✅ Connected to MongoDB")
        except PyMongoError as err:
            logger.error("❌ MongoDB connection failed: %s", err)
            raise

        # 3. Determine database name
        if db_name:
            name = db_name
        else:
            parsed = urlparse(dburl)
            name = parsed.path.lstrip("/")
            if not name:
                name = os.environ.get("DATABASE_NAME", "TTKDB")

        # 4. Select the database
        self._db = self._client[name]
        logger.info("Using MongoDB database: %s", name)

    def get_client(self) -> MongoClient:
        """Return the raw MongoClient."""
        return self._client

    def get_db(self):
        """Return the Database instance."""
        return self._db

    def close(self) -> None:
        """Close the client connection."""
        self._client.close()
        logger.info("MongoDB connection closed")
