import socket

import time

class ClientRequestHandler():

    def __init__(self):
        super().__init__()
        self.socks = {}

    def run(self, *args):
        data = args[0]
        server = args[1]
        port = args[2]

        # addr = socket.getaddrinfo(server, port)[0][-1]
        addr = b':'.join([bytes(server, 'ascii'), bytes([port & 0xff]), bytes([(port >> 8) & 0xff])])

        if self.socks.get(addr) is None:
            self.socks[addr] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port == 0:
                port = 60000

            try:

                self.socks[addr].connect(socket.getaddrinfo(server, port)[0][-1])

            except OSError as e:
                print('Error: ' + str(e) + 'Couldnt connect with socket-server')

        return self.send(addr, data)

    def send(self, addr, data):
        buffer_size = 536
        response = b''
        try:
            self.socks[addr].sendall(data)
            while True:
                part = self.socks[addr].recv(buffer_size)
                response += part
                if len(part) < buffer_size:
                    break
            # print('\t', response, '<=========CRH')
            if response == b'0':
                return True
            elif response == b'':
                # TODO look for a better exception
                raise OSError
            return response
        except OSError as e:
            print('Cant send data')
            self.socks[addr].close()
            self.socks[addr] = None
            return False