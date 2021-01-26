import config as cfg
# import adl as adl
import os
import socket

class AmotAgent:

    @staticmethod
    def send_receive(socket, data):
        buffer_size = 536
        response = b''
        try:
            socket.sendall(data)
            while True:
                part = socket.recv(buffer_size)
                response += part
                if len(part) < buffer_size:
                    break
            if response == b'0':
                return None
            elif response == b'':
                # TODO look for a better exception
                raise OSError
            return response
        except OSError as e:
            print('Cant send or receive data')
            socket.close()
            return False

    @staticmethod
    def thingStart():
        print('running agent')
        # connecting to server
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect(socket.getaddrinfo(cfg.server['host'], cfg.server['port'])[0][-1])
        except:
            return

        # clear directory
        files = os.listdir('components')
        for file in files:
            path = 'components/' + file
            try:
                f = open(path, "r")
                f.close()
                os.remove(path)
            except OSError:
               pass

        # listing components
        # components = [c for c in adl.Components.values()]
        # components.append('AMoTAgent')


        # sending data
        # msg = b'START\nThing:soueu\nComponents:' + b','.join([bytes(c, 'ascii') for c in components])
        msg = b'START\nThing:' + bytes(cfg.thing['id'], 'ascii')
        data = AmotAgent.send_receive(conn, msg)

        data = str(data, 'ascii')

        files = data.split('\x1c') # FILE SEPARATOR (28)
        for comp_content in files:
            compname, content = comp_content.split('\x1d') # GROUP SEPARATOR (29)
            # compname, compversion = compname_version.split('#')
            # self.adaptComponent(compname, compversion, content)
            # file = 'components/' + compname + '.py'
            file = compname + '.py'
            wr = open(file, 'w')
            wr.write(content)
            wr.close()
