from Component import Component
from AMoTEngine import Message

class NotifierProxy(Component):

    def __init__(self):
        super().__init__()

    def run(self, topic, message, address):
        message = Message(b'Notify', topic, message)
        (ip, port) = address

        if message is None:
            return False

        return self.external().run(message, ip, port)
