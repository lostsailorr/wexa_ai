import logging
from typing import Optional, Dict, Any, List
from neo4j import GraphDatabase, Driver, Session
from app.config import settings

logger = logging.getLogger("sentinelgraph.database")


class Neo4jConnection:
    _instance: Optional["Neo4jConnection"] = None
    _driver: Optional[Driver] = None
    _is_connected: bool = False
    _last_error: Optional[str] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Neo4jConnection, cls).__new__(cls)
        return cls._instance

    def initialize(self):
        """Initializes the Neo4j driver using CognoDB Bolt connection parameters."""
        uri = settings.COGNODB_URI
        user = settings.COGNODB_USER
        password = settings.COGNODB_PASSWORD

        if not password or uri == "bolt://localhost:7687" and not settings.DEBUG:
            self._is_connected = False
            self._last_error = "No database credentials provided. Operating in Fallback/Demo dataset mode."
            logger.warning(self._last_error)
            return

        try:
            logger.info(f"Connecting to CognoDB instance at {uri} as {user}...")
            self._driver = GraphDatabase.driver(
                uri,
                auth=(user, password),
                max_connection_lifetime=3600,
                max_connection_pool_size=50,
                connection_acquisition_timeout=15.0
            )
            # Verify connectivity with a lightweight ping
            with self._driver.session() as session:
                result = session.run("RETURN 1 AS ping")
                record = result.single()
                if record and record["ping"] == 1:
                    self._is_connected = True
                    self._last_error = None
                    logger.info("Successfully connected and authenticated with CognoDB!")
        except Exception as e:
            self._is_connected = False
            self._last_error = str(e)
            logger.error(f"Failed to connect to CognoDB: {e}. Falling back to demo mode.")

    def get_session(self) -> Optional[Session]:
        if self._driver and self._is_connected:
            return self._driver.session()
        return None

    def execute_query(self, query: str, parameters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Executes a parameterized Cypher query and returns a list of dictionaries."""
        if not self._is_connected or not self._driver:
            raise ConnectionError(f"Database unreachable: {self._last_error}")

        params = parameters or {}
        with self._driver.session() as session:
            result = session.run(query, params)
            return [record.data() for record in result]

    def check_health(self) -> Dict[str, Any]:
        """Runs a health check on the CognoDB connection."""
        if not self._driver:
            return {
                "status": "demo_fallback",
                "connected": False,
                "uri": settings.COGNODB_URI,
                "message": self._last_error or "Driver not initialized."
            }
        try:
            with self._driver.session() as session:
                res = session.run("RETURN 1 AS ping, datetime() AS server_time")
                rec = res.single()
                return {
                    "status": "healthy",
                    "connected": True,
                    "uri": settings.COGNODB_URI,
                    "server_time": str(rec["server_time"]) if rec else "unknown"
                }
        except Exception as e:
            self._is_connected = False
            self._last_error = str(e)
            return {
                "status": "error",
                "connected": False,
                "uri": settings.COGNODB_URI,
                "error": str(e)
            }

    def close(self):
        if self._driver:
            self._driver.close()
            self._driver = None
            self._is_connected = False


db = Neo4jConnection()
