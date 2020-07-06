from AMoTEngine import Component, Message

class Marshaller(Component):
    def __init__(self):
        super().__init__()

    def run(self, *args):
        message_obj = args[0]
        ip, port = args[1:3]

        serialized = b'Op:' + message_obj.op + b'\n'
        serialized += b'Topic:' + message_obj.topic + b'\n'
        if message_obj.subscriber_addr is not None:
            serialized += b'Addr:' + message_obj.subscriber_addr + b'\n'

        serialized += b'\n'
        serialized += message_obj.message

        return self.external().run(serialized, ip, port)
