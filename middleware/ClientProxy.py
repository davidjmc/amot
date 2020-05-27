from AMoTEngine import Component


class ClientProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        request = None

        if args[0] == b'Publish':
            request = self.Request(args[0], args[1], args[2])
        elif args[0] == b'Subscribe':
            request = self.Request(args[0], args[1], self.engine.subscriber_configs['host'],
                                   self.engine.subscriber_configs['port'])
        elif request.op == b'Adapt':
            invocation = {'Operation': args[0], 'Topic': args[1]}
        else:
            print('Notification engine :: Operation ' + args[0].decode() + ' is not implemented by AMoT Engine')

        self.external().run(request)



