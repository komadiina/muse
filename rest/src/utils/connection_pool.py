import os
from typing import Union

from mysql.connector.pooling import MySQLConnectionPool, PooledMySQLConnection
from threading import Lock, Thread

class ConnectionPoolMeta(type):
    _instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls != cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
            return cls._instance

class ConnectionPool(metaclass=ConnectionPoolMeta):
    def __init__(self, max_connections: int = 32, verbose: bool = False):
        self.max_connections = max_connections

        self.db_username = os.getenv("DB_USERNAME")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_schema = os.getenv("MYSQL_SCHEMA")

        self.verbose = verbose

        self.pool = MySQLConnectionPool(pool_size=max_connections, pool_reset_session=True,
                                        pool_name=f"pool_{self.db_username}"[:64])
        instance = self

    def get_connection(self) -> Union[PooledMySQLConnection, None]:
        return self.pool.get_connection()

    def close_connection(self, connection: PooledMySQLConnection) -> None:
        connection.close()