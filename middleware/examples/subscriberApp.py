from AMoTEngine import Component
from datetime import datetime


class App(Component):
    def __init__(self):
        super().__init__()
        self.count = 0

    def run(self, *args):
        package = args[0]
        print(datetime.now(), package.topic, package.message)
        pass
