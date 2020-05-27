from AMoTEngine import Component


class App(Component):
    def __init__(self):
        super().__init__()
        self.count = 0

    def run(self, *args):
        package = args[0]
        print(package.topic)
        print(package.message)
        pass
