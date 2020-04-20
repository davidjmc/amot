import pickle

from AMoTEngine import Component, amot_broker_ip, amot_broker_port


class Requestor(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        invocation = args[0]
        data = pickle.dumps(invocation)
        package = {'Destination': amot_broker_ip, 'DPort': amot_broker_port, 'Payload': data}
        self.external().run(package)
