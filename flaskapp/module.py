import socket
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
    def send(self, ip):
        # send message to IP

class Client:
    def __init__(self, ThisIP, ThisAccountNumber, ThisPassword):
        self.thisIP = ThisIP
        self.accountNumber = ThisAccountNumber
        self.thisPassword = ThisPassword
        self.s = socket.socket()

    def authenticate(self):
        if self.accountNumber == self.thisPassword:
            return True

    def listening(self):


    def update(self):