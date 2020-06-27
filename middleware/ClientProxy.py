from AMoTEngine import Component, Message


class ClientProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        request = None
        ip = self.engine.server_configs['host']
        port = self.engine.server_configs['port']

        if args[0] == b'Publish':
            request = Message(args[0], args[1], args[2])
        elif args[0] == b'Subscribe':
            ip_port = self.engine.subscriber_configs['host'] + b' ' + self.engine.subscriber_configs['port']
            request = Message(args[0], args[1], ip_port)
        elif args[0] == b'Notify':
            request = Message(args[0], args[1], args[2])
            ip = args[3]
            port = args[4]
        elif args[0] == b'Adapt':
            ip = args[3]
            port = args[4]
            request = Message(args[0], args[1], args[2])
        else:
            print('Notification engine :: Operation ' + args[0].decode() + ' is not implemented by AMoT Engine')

        return self.external().run(request, ip, port)



