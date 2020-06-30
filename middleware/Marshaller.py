from AMoTEngine import Component, Message

class Marshaller(Component):
    def __init__(self):
        super().__init__()

    def run(self, *args):
        message = args[0]
        ip = None
        port = None
        if len(args) > 1:
            ip, port = args[1:3]
        if type(message) == bytes: # i.e., it is a serialize operation (is it?) #TODO
            message_obj = self.unserialize(message)
            return self.external().run(message_obj)
        elif type(message) == Message:
            serialized = self.serialize(message)
            return self.external().run(serialized, ip, port)


    def serialize(self, message_obj):
        serialized = b'Op:' + message_obj.op + b'\n'
        serialized += b'Topic:' + message_obj.topic + b'\n'
        if message_obj.subscriber_addr is not None:
            serialized += b'Addr:' + message_obj.subscriber_addr + b'\n'

        serialized += b'\n'
        serialized += message_obj.message
        return serialized

    def unserialize(self, data):
        print(data, 'aqui!!!!')
        attrs = {
            b'Op': None,
            b'Topic': None,
            b'Subscriber_addr': None,
            b'message': None,
        }

        attr = b''
        val = b''
        byte = 0
        while byte < len(data):
            c = data[byte]
            if c != 58: # ':'
                attr += bytes([c])
                byte += 1
                continue

            byte += 1
            c = data[byte]
            while c != 10: # '\n'
                val += bytes([c])
                byte += 1
                c = data[byte]
            # end of header line
            attrs[attr] = val
            attr = b''
            val = b''
            byte += 1
            c = data[byte]
            if c == 10: # '\n', i.e., it is the end of the header
                break
        attrs[b'message'] = b''
        byte += 1
        while byte < len(data):
            attrs[b'message'] += bytes([data[byte]])
            byte += 1

        # parts = str(data, 'ascii').split('\n')
        # for part in parts:
        #     attr, value = part.split(':', 1)
        #     attrs[attr] = value
        message_obj = Message(
            attrs[b'Op'],
            attrs[b'Topic'],
            attrs[b'message'],
            attrs[b'Subscriber_addr']
        )
        return message_obj