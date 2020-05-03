from AMoTEngine import Component


class AMoTApp(Component):
    def __init__(self):
        super().__init__()
        self.count = 0

    def run(self, *args):
        print(args[0])
        pass
