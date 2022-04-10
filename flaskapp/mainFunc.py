import socket
import threading


class MainApp():
    def __init__(self, Debug_mode):
        SERVER = socket.gethostbyname(socket.gethostname())
        PORT = 5050
        self.HEADER = 64
        self.ADDR = (SERVER, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.debug_mode = Debug_mode

    def __handle_client(self, conn, addr):
        if self.debug_mode:
            print(f"[NEW CONNECTION] {addr[0]} connected.")
        msg_length = conn.recv(self.HEADER).decode("utf-8")
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")

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

    def run(self):
        server_thread = threading.Thread(target=self.start_server, args=())
        server_thread.start()
