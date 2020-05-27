import pickle

from AMoTEngine import Component


class Requestor(Component):

    def __init__(self):
        super().__init__()
        self.pkg = None

    def run(self, *args):
        request = args[0]

        self.pkg = request.op
        self.pkg += b' ' + request.topic
        message = [m for m in request.args]
        self.pkg += b' ' + b' '.join(message)

        # data = pickle.dumps(invocation)

        package = {
            'Destination': self.engine.server_config['serverHost'],
            'DPort': self.engine.server_config['serverPort'],
            'Payload': self.pkg
        }

        self.external().run(package)
