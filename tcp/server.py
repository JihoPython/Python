import socket
import threading

from utils import logger, COLOR


FORMAT = 'utf-8'
HEADER = 64

DISCONNECT_MESSAGE = '!DISCONNECT'

SERVER = "localhost"
PORT = 5050
ADDR = (SERVER, PORT)

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn: socket.socket, addr):
    logger.info(f"New Connection - {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)


            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("sokcet disconnected.".encode(FORMAT))
            else:
                conn.send("Message Received.".encode(FORMAT))

            logger.info(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    logger.info(f"Server is listening on {SERVER}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        logger.info(f"Active Connections - {threading.active_count() - 1}")

logger.info("Server is starting...")
start()
