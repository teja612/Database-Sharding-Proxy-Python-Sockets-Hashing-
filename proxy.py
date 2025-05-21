import socket
from concurrent.futures import ThreadPoolExecutor

class ShardProxy:
    def __init__(self, shards=["localhost:9001", "localhost:9002"]):
        self.shards = shards
        self.pool = ThreadPoolExecutor(10)  # 10 threads
    
    def handle_connection(self, conn):
        user_id = int(conn.recv(1024).decode())
        shard = self.shards[user_id % len(self.shards)]
        conn.sendall(f"Route to {shard}".encode())
        conn.close()

    def start(self, port=9000):
        with socket.socket() as s:
            s.bind(('localhost', port))
            s.listen()
            while True:
                conn, _ = s.accept()
                self.pool.submit(self.handle_connection, conn)
