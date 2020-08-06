import pickle

class Marshaller():
    def __init__(self):
        super().__init__()

    def run(self, *args):
        message_obj, ip, port = args

        # print('NEW MARSHALLER')
        print('pickle marshaller')

        serialized = pickle.dumps(message_obj)
        serialized = b'pkl' + serialized

        return AmotEngine.attached(self).run(serialized, ip, port)
