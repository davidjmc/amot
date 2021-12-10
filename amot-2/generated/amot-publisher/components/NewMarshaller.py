from AMoTEngine import Amot

class Marshaller():
    def __init__(self):
        super().__init__()

    def run(self, invArg):
        def toBytes(data):
            if type(data) is bytes:
                return data
            if type(data) is str:
                return bytes(data, 'utf-8')
            if type(data) is list:
                return [toBytes(d) for d in data]

            raise Exception('data should be [bytes], [string] or [array]')

        invArg = {k: toBytes(v) for k, v in invArg.items()}

        op = invArg['OP']
        topics = invArg['TOPICS']
        msg = invArg['MSG']
        thing_id = invArg['THING_ID']

        # serialized = b'OP:' + op + b'\n'
        # serialized += b'TOPICS:' + b'\0x1F'.join(topics) + b'\n'
        # serialized += b'THING_ID:' + thing_id + b'\n'
        # serialized += b'\n'
        # serialized += msg

        serialized = b'Op:' + op + b'\n'
        serialized += b'Topic:' + topics[0] + b'\n'
        serialized += b'Thing:' + thing_id + b'\n'
        serialized += b'\n'
        serialized += msg

        invocation = {
            'DATA': serialized
        }

        return Amot.attached(self).run(invocation)

        return
        message_obj, ip, port = args

        serialized = b'Op:' + message_obj['op'] + b'\n'
        serialized += b'Topic:' + message_obj['topic'] + b'\n'
        serialized += b'Thing:' + message_obj['thing'] + b'\n'
        if message_obj.get('subs_addr') is not None:
            serialized += b'Addr:' + message_obj['subs_addr'] + b'\n'

        serialized += b'\n'
        serialized += message_obj['msg']

        return AmotEngine.attached(self).run(serialized, ip, port)
