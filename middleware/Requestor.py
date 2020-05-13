import pickle

from AMoTEngine import Component


class Requestor(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        invocation = args[0]
        data = pickle.dumps(invocation)
        package = {
            'Destination': self.engine.configs['serverHost'],
            'DPort': self.engine.configs['serverPort'],
            'Payload': data
        }
        self.external().run(package)
