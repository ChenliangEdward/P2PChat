import socket
import threading
import sqlite3
import time


class MainApp:
    def __init__(self, Debug_mode):
        SERVER = socket.gethostbyname(socket.gethostname())
        PORT = 5050
        self.HEADER = 64
        self.ADDR = (SERVER, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.debug_mode = Debug_mode
        self.con = sqlite3.connect("main.db")
        self.cur = self.con.cursor()

    def __insert_message(self, msg, from_user, to_user):
        timestamp = str(time.time())
        self.cur.execute(f"INSERT INTO messages VALUES ({timestamp},{from_user},{to_user},{msg})")

    def __handle_client(self, conn, addr):
        if self.debug_mode:
            print(f"[NEW CONNECTION] {addr[0]} connected.")

        msg_length = conn.recv(self.HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")

            self.__insert_message(msg, addr[0], self.ADDR[0])
            self.con.commit()
            if self.debug_mode:
                print(f"[{addr}]{msg}")
        conn.close()

    def start_server(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()  # start a socket object when a new connection starts
            self.__handle_client(conn, addr)

    def send(self, target_ip, target_port):
        msg = input(">>> ")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))

        message = msg.encode("utf-8")
        msg_length = len(message)
        send_length = str(msg_length).encode("utf-8")
        send_length += b' ' * (self.HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

        self.__insert_message(msg, self.ADDR[0], target_ip)
        self.con.commit()

    def run(self):
        print("Start Listening...")
        server_thread = threading.Thread(target=self.start_server, args=())
        server_thread.start()
