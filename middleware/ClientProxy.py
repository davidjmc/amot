from AMoTEngine import Component, amot_client_ip, amot_client_port


class ClientProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        invocation = None

        if args[0] is 'Publish':
            message = {'Topic': args[1], 'Message': args[2]}
            invocation = {'Operation': args[0], 'Message': message}
        elif args[0] is 'Subscribe':
            message = {'Source': amot_client_ip, 'SPort': amot_client_port, 'Topic': args[1]}
            invocation = {'Operation': args[0], 'Message': message}
        elif args[0] is 'Adapt':
            invocation = {'Operation': args[0], 'Topic': args[1]}
        else:
            print('Notification engine :: Operation ' + args[0]['Operation'] + 'is not implemented by AMoT Engine')

        self.external().run(invocation)



