# Database-Sharding-Proxy-Python-Sockets-Hashing-
How to Run the Project
1. Start SQLite Shards
bash
# Terminal 1
sqlite3 shard_1.db "CREATE TABLE users (id INT, name TEXT);"
nc -l 9001  # Simulate shard server

# Terminal 2
sqlite3 shard_2.db "CREATE TABLE users (id INT, name TEXT);"
nc -l 9002
2. Start Proxy
python
proxy = ShardProxy(shards=["localhost:9001", "localhost:9002"])
proxy.start(port=9000)
3. Test Routing
bash
echo "123" | nc localhost 9000  # Routes to shard_1 (123 % 2 = 1)
