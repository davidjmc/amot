import time

class QueueProxy():

    def __init__(self):
        super().__init__()

    def run(self, *args):
        AmotEngine._times.append(('--proxy0:', time.time()))
        message = None
        ip = AmotEngine.server_configs['host']
        port = AmotEngine.server_configs['port']

        if args[0] == b'Publish':
            message = {'op': args[0], 'topic': args[1], 'msg': args[2]}
        elif args[0] == b'Subscribe':
            ip_port = AmotEngine.subscriber_configs['host'] + b' ' + AmotEngine.subscriber_configs['port']
            message = {'op': args[0], 'topic': args[1], 'msg': ip_port}
        elif args[0] == b'Unsubscribe':
            #TODO
            pass
        else:
            print('Notification engine :: Operation ' + args[0] + ' is not implemented by AMoT Engine')

        if message is None:
            return False

        AmotEngine._times.append(('--proxy1:', time.time()))
        return AmotEngine.attached(self).run(message, ip, port)



