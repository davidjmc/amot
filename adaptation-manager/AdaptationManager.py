from AMoTEngine import Component


class AdaptationManager(Component):

    def __init__(self):
        super().__init__()

    def run(self, *args):
        request = args[0]
        operation = request.op
        adaptation_type = request.topic
        message = request.message

        if adaptation_type == b'Evolutive':
            print('Entrei no Evolutive')
            return b'Entrei no Evolutive!'
        elif adaptation_type == b'Reactive':
            print('Entrei no Reactive')
        elif args[0] == b'Proactive':
            print('Entrei no Proactive')
        else:
            print('AdaptationManager :: Adaptation ' + adaptation_type + ' is not implemented by Adaptation Manager')