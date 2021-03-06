import socket
import threading
from flaskapp.models import *
import time


class MainApp():
    def __init__(self, Debug_mode):
        SERVER = socket.gethostbyname(socket.gethostname())
        PORT = 5050
        self.HEADER = 64
        self.ADDR = (SERVER, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.debug_mode = Debug_mode
        self.myusername = Friends.query.filter_by(SERVER).first()["username"]

    def __handle_client(self, conn, addr):
        if self.debug_mode:
            print(f"[NEW CONNECTION] {addr[0]} connected.")
        msg_length = conn.recv(self.HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            # Add new msg to db
            from_username = Friends.query.filter_by(ip=addr[0]).first()  # Get the username from the IP that sends to
            new_msg = Messages(timestamp=int(time.time()), from_name=from_username["username"], to_name=self.myusername)
            db.session.add(new_msg)
            db.session.commit()

            if self.debug_mode:
                print(f"[{addr}]{msg}")
        conn.close()

    def start_server(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()  # start a socket object when a new connection starts
            self.__handle_client(conn, addr)

    def send(self, target_ip, target_port, msg):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))
        message = msg.encode("utf-8")
        msg_length = len(message)
        send_length = str(msg_length).encode("utf-8")
        send_length += b' ' * (self.HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

    def run(self):
        server_thread = threading.Thread(target=self.start_server, args=())
        server_thread.start()


class Friend:
    def __init__(self, Name, IP, MessageList):
        self.name = Name
        self.ip = IP
        self.messageList = MessageList
        self.blocked = False

    def update_ip(self):
        self.ip = "0.0.0.0"

    def block(self):
        self.blocked = True


class Message:
    def __init__(self, From, To, Content, Timestamp, IsSent):
        self._from = From
        self.to = To
        self.content = Content
        self.timestamp = Timestamp
        self.isSent = IsSent
