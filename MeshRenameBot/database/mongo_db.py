import re
import os
import logging
from urllib.parse import urlparse
from typing import AbstractSet
from pymongo import MongoClient, errors

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MongoDB:
    """
    Base class for MongoDB access.
    - dburl: full MongoDB URI (e.g. mongodb+srv://...)
    - db_name: optional override for the database name; 
               if omitted, tries to parse it from the URI path or falls back to 'TTKDB'.
    """

    def __init__(self, dburl: str = None, db_name: str = None) -> None:
        # 1. Determine URI
        dburl = dburl or os.getenv("DATABASE_URL")
        if not dburl:
            raise ValueError(
                "MongoDB URI must be provided via the `dburl` argument "
                "or the `DATABASE_URL` environment variable."
            )

        # 2. Connect and verify
        try:
            self._client = MongoClient(dburl, serverSelectionTimeoutMS=5000)
            self._client.admin.command("ping")
            logger.info("✅ Connected to MongoDB")
        except errors.PyMongoError as err:
            logger.error("❌ MongoDB connection failed: %s", err)
            raise

        # 3. Determine database name
        if db_name:
            name = db_name
        else:
            parsed = urlparse(dburl)
            name = parsed.path.lstrip("/")
            if not name:
                name = os.getenv("DATABASE_NAME", "TTKDB")

        # 4. Select the database
        self._db = self._client[name]
        logger.info("Using MongoDB database: %s", name)

    def get_client(self) -> MongoClient:
        """Return the underlying MongoClient."""
        return self._client

    def get_db(self):
        """Return the selected Database instance."""
        return self._db

    def close(self) -> None:
        """Close the MongoClient connection."""
        self._client.close()
        logger.info("MongoDB connection closed")

    # Context‐manager support
    def __enter__(self) -> "MongoDB":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
