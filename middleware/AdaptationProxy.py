from Component import Component
from AMoTEngine import Message

class AdaptationProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, adaptability, message, ip, port):
        message = Message(b'Adapt', adaptability, message)

        if message is None:
            return False

        return self.external().run(message, ip, port)
