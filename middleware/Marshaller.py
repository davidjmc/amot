import time

class Marshaller():
    def __init__(self):
        super().__init__()

    def run(self, *args):
        AmotEngine._times.append(('--mars0:', time.time()))
        message_obj, ip, port = args

        serialized = b'Op:' + message_obj['op'] + b'\n'
        serialized += b'Topic:' + message_obj['topic'] + b'\n'
        if message_obj.get('subs_addr') is not None:
            serialized += b'Addr:' + message_obj['subs_addr'] + b'\n'

        serialized += b'\n'
        serialized += message_obj['msg']

        AmotEngine._times.append(('--mars1:', time.time()))
        return AmotEngine.attached(self).run(serialized, ip, port)
