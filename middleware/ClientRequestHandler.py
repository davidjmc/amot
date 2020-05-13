import socket

from AMoTEngine import Component


class ClientRequestHandler(Component):

    def __init__(self):
        super().__init__()
        self.sock = None
        self.server = None
        self.port = None
        self.addr = None
        self.data = None

    def run(self, *args):
        package = args[0]
        self.data = package['Payload']

        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server = package['Destination']
            self.port = package['DPort']
            if self.port == 0:
                self.port = 60000
            self.addr = socket.getaddrinfo(self.server, self.port)[0][-1]

            try:
                self.sock.connect(self.addr)
            except OSError as e:
                print('Error: ' + str(e) + 'Couldnt connect with socket-server')

        self.send()

    def send(self):
        self.sock.sendall(self.data)
        # self.sock.close()
