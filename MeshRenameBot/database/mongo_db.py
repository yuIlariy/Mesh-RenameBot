import re
import os
import logging
from urllib.parse import urlparse
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError
from pymongo.database import Database

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MongoDB:
    """
    Base class for MongoDB access.
    Initializes a MongoClient, ensures it can connect, and selects a database.
    """

    def __init__(
        self,
        uri: str = None,
        db_name: str = None,
        *,
        connect_timeout_ms: int = 5000
    ) -> None:
        # 1. Determine MongoDB URI
        uri = uri or os.getenv("DATABASE_URL")
        if not uri:
            raise ValueError(
                "MongoDB URI must be provided as `uri` argument or via "
                "`DATABASE_URL` environment variable"
            )

        # 2. Initialize client and test connection
        try:
            self._client = MongoClient(uri, serverSelectionTimeoutMS=connect_timeout_ms)
            # Force a call to validate the connection
            self._client.admin.command("ping")
            logger.info("✅ Connected to MongoDB")
        except (ConnectionFailure, ConfigurationError) as e:
            logger.error("❌ Could not connect to MongoDB: %s", e)
            raise

        # 3. Determine database name
        if db_name:
            name = db_name
        else:
            # Try parsing it from the URI path (`mongodb://.../mydb`)
            parsed = urlparse(uri)
            name = parsed.path.lstrip("/") or os.getenv("DATABASE_NAME")

        if not name:
            raise ValueError(
                "Database name must be provided as `db_name` argument, "
                "embedded in the URI, or via `DATABASE_NAME` environment variable"
            )

        # 4. Select the database
        self.db: Database = self._client[name]
        logger.info("Using MongoDB database: %s", name)

    def get_client(self) -> MongoClient:
        """
        Returns the underlying MongoClient.
        """
        return self._client

    def get_db(self) -> Database:
        """
        Returns the selected Database instance.
        """
        return self.db

    def close(self) -> None:
        """
        Closes the MongoClient connection.
        """
        self._client.close()
        logger.info("MongoDB connection closed")

    # Context-manager support
    def __enter__(self) -> "MongoDB":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
