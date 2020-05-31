import socket, select

from AMoTEngine import Component


class ServerRequestHandler(Component):
    def __init__(self):
        super().__init__()
        self.server_sock = None
        self.address = None
        self.connection = None
        self.message = None
        self.sources = []
        self.destinations = []
        self.messages_queues = {}

    def run(self, *args):
        try:
            if self.server_sock is None:
                self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                timeout = self.engine.listen_configs['timeout']
                if timeout is not None:
                    timeout = timeout / 1000.0
                self.server_sock.settimeout(timeout)
                self.address = socket.getaddrinfo(self.engine.listen_configs['host'],
                                                  self.engine.listen_configs['port'])[0][-1]

                try:
                    self.server_sock.bind(self.address)
                    print('[ Starting up on {} port {} ] >'.format(*self.address))
                    self.server_sock.listen(5)
                    self.sources = [self.server_sock]

                except OSError as e:
                    print('ServerRequestHandler Bind Error: ', e)

        except OSError as e:
            print('ServerRequestHandler Socket Error: ', e)

        # print('sources b4:', self.sources)
        # print('select')
        readable, writeable, exceptional = select.select(self.sources, [], [])
        # print('readable now: ', readable)
        for s in readable:
            if s is self.server_sock:
                try:
                    connection, device = self.server_sock.accept()
                    self.server_sock.setblocking(False)
                    self.sources.append(connection)
                    readable.append(connection)
                except OSError as e:
                    print('Error when receiving data on the ServerRequestHandler: ', e)
            elif s:
                buffer_size = 536
                data = b''
                try:
                    while True:
                        part = s.recv(buffer_size)
                        data += part
                        if len(part) < buffer_size:
                            break
                except OSError as e:
                    self.sources.remove(s)
                    continue

                if data:
                    self.message = data
                    self.external().run(self.message)
                else:
                    self.sources.remove(s)

        # print('sources then:', self.sources)
        # print('-----')

        # self.receive()


# import socket
#
# from AMoTEngine import Component
#
#
# class ServerRequestHandler(Component):
#     def __init__(self):
#         super().__init__()
#         self.sock = None
#         self.server_sock = None
#         self.address = None
#         self.connection = None
#         self.message = None
#
#     def run(self, *args):
#         try:
#             if self.server_sock is None:
#                 self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#                 self.server_sock.settimeout(self.engine.listen_cfg['timeout'])
#                 self.address = socket.getaddrinfo(self.engine.listen_cfg['host'],
#                                                   self.engine.listen_cfg['port'])[0][-1]
#
#                 try:
#                     self.server_sock.bind(self.address)
#                     print('<Starting up on {} port {}'.format(*self.address))
#                     self.server_sock.listen(5)
#                 except OSError as e:
#                     print('ServerRequestHandler Bind Error: ', e)
#
#             print(self.server_sock)
#
#         except OSError as e:
#             print('ServerRequestHandler Socket Error: ', e)
#
#         self.receive()
#         self.external().run(self.message)
#
#     def receive(self):
#         buffer_size = 536
#         data = b''
#         try:
#             self.connection, client = self.server_sock.accept()
#             # print('Connected by', client)
#             while True:
#                 part = self.connection.recv(buffer_size)
#                 data += part
#                 if len(part) < buffer_size:
#                     break
#             self.message = data
#         except OSError as e:
#             print('Error when receiving data on the ServerRequestHandler: ', e)
