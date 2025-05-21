import sqlite3
from queue import Queue

class ConnectionPool:
    def __init__(self, shard_url, max_connections=5):
        self.pool = Queue(max_connections)
        for _ in range(max_connections):
            self.pool.put(sqlite3.connect(shard_url))
    
    def get_conn(self):
        return self.pool.get()
    
    def release_conn(self, conn):
        self.pool.put(conn)
