from Component import Component

class Marshaller(Component):
    def __init__(self):
        super().__init__()

    def run(self, *args):
        message_obj, ip, port = args

        print('NEW MARSHALLER')

        serialized = b'Op:' + message_obj['op'] + b'\n'
        serialized += b'Topic:' + message_obj['topic'] + b'\n'
        if message_obj.get('subs_addr') is not None:
            serialized += b'Addr:' + message_obj['subs_addr'] + b'\n'

        serialized += b'\n'
        serialized += message_obj['msg']

        return self.external().run(serialized, ip, port)
