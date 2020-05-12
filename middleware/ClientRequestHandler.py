import socket

from AMoTEngine import Component


class ClientRequestHandler(Component):

    def __init__(self):
        super().__init__()
        self.sock = None
        self.server = None
        self.port = None
        self.data = None

    def run(self, *args):
        package = args[0]
        self.data = package['Payload']

        if self.sock is None:
            self.server = package['Destination']
            self.port = package['DPort']
            if self.port == 0:
                self.port = 60000

            try:
                self.connect()
            except OSError as e:
                print('Error: ' + str(e) + 'Couldnt connect with socket-server')

        self.send()

    def connect(self):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(self.server, self.port)[0][-1]
        self.sock.connect(addr)

    def send(self):
        print(self.data)
        self.sock.sendall(self.data)
        # self.sock.close()
