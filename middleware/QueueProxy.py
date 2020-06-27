from AMoTEngine import Component, Message


class QueueProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        message = None
        ip = self.engine.server_configs['host']
        port = self.engine.server_configs['port']

        if args[0] == b'Publish':
            message = Message(args[0], args[1], args[2])
        elif args[0] == b'Subscribe':
            ip_port = self.engine.subscriber_configs['host'] + b' ' + self.engine.subscriber_configs['port']
            message = Message(args[0], args[1], None, ip_port)
        elif args[0] == b'Unsubscribe':
            #TODO
            pass
        else:
            print('Notification engine :: Operation ' + args[0] + ' is not implemented by AMoT Engine')

        if message is None:
            return False

        return self.external().run(message, ip, port)



