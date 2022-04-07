import socket
import threading
import time

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = "192.168.0.134"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


# def handle_client(conn, addr):
#     print(f"[NEW CONNECTION] {addr} connected.")
#
#     connected = True
#     while connected:
#         msg_length = conn.recv(HEADER).decode(FORMAT)
#         if msg_length:
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False
#             else:
#                 print(f"[{addr}]{msg}")
#     conn.close()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]} connected.")
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}]{msg}")
    conn.close()


def start_server():
    server.listen()
    print(f"[LISTENING] server is listening {SERVER}\n")
    while True:
        conn, addr = server.accept()  # start a socket object when a new connection starts
        handle_client(conn, addr)


def background():
    while True:
        print("Running...")
        time.sleep(10)


if __name__ == '__main__':
    print("[STARTING] server is starting...")
    server_thread = threading.Thread(target=start_server, args=())
    server_thread.start()
    while True:
        print("Running...")
        time.sleep(10)

