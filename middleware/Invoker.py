import pickle

from AMoTEngine import Component


class Invoker(Component):
    def __init__(self):
        super().__init__()

    def run(self, *args):
        data = args[0]
        if data is None:
            return
        invocation = pickle.loads(data)
        self.external().run(invocation)
