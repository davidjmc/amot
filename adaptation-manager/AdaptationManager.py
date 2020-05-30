from AMoTEngine import Component


class AdaptationManager(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        print(args[0])
