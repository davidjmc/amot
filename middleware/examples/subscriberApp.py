from AMoTEngine import Component
from datetime import datetime


class App(Component):
    def __init__(self):
        super().__init__()
        self.count = 0

    def run(self, topic, message):
        print(':::T1:::', datetime.now().timestamp())
        print('Recebido: "{0}" em "{1}"'.format(message, topic))
        # print(datetime.now(), package.topic, package.message)
        pass
