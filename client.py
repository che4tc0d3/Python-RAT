# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_server:
    connection_server.connect((HOST, PORT))
    connection_server.send(b"Hello, world")
    data = connection_server.recv(1024)

print(f"Received {data!r}")
