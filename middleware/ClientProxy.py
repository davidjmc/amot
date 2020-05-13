from AMoTEngine import Component


class ClientProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        invocation = None

        if args[0] == b'Publish':
            message = {'Topic': args[1], 'Message': args[2]}
            invocation = {'Operation': args[0], 'Message': message}
        elif args[0] == b'Subscribe':
            message = {
                'Source': self.engine.subscriber_configs['host'],
                'SPort': self.engine.subscriber_configs['port'],
                'Topic': args[1]
            }
            invocation = {'Operation': args[0], 'Message': message}
        elif args[0] == b'Adapt':
            invocation = {'Operation': args[0], 'Topic': args[1]}
        else:
            print('Notification engine :: Operation ' + args[0].decode() + ' is not implemented by AMoT Engine')

        self.external().run(invocation)



