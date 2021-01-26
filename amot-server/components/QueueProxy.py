
class QueueProxy():

    def __init__(self):
        super().__init__()

    def run(self, *args):
        message = None
        ip = AmotEngine._broker['host']
        port = AmotEngine._broker['port']

        if args[0] == b'Publish':
            message = {'op': args[0], 'topic': args[1], 'msg': args[2]}
        elif args[0] == b'Subscribe':
            ip_port = bytes(AmotEngine.ip, 'ascii') + b' ' + AmotEngine._listen['port']
            message = {'op': args[0], 'topic': args[1], 'msg': ip_port}
        elif args[0] == b'Unsubscribe':
            #TODO
            pass
        else:
            print('Notification engine :: Operation ' + args[0] + ' is not implemented by AMoT Engine')

        if message is None:
            return False

        return AmotEngine.attached(self).run(message, ip, port)



