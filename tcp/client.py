from email import message
import socket

FORMAT = 'utf- 8'
HEADER = 64
DISCONNECT_MESSAGE = '!DISCONNECT'

SERVER = "localhost"
PORT = 5050
ADDR = (SERVER, PORT)


client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg: str):
    message = msg.encode(FORMAT)
    send_length = str(len(message)).encode(FORMAT)
    header = send_length + b' ' * (HEADER - len(send_length))
    client.send(header)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("김지호")
send("Hello Python")
send("Hello TCP")
send(DISCONNECT_MESSAGE)
