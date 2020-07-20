from EvolutiveAdapter import EvolutiveAdapter


class AdaptationManager():
    # component_library = '/home/david/doutorado/2020-1/amot/adaptation-manager/library'

    def __init__(self):
        super().__init__()

    def run(self, *args):
        # REQUEST DECODE
        request = args[0]
        adaptation_type = request.topic
        message = request.message.decode('ascii')

        thing_id, components_hashes_str = message.split(' ')

        components_hashes = {}
        for component_hash in components_hashes_str.split(','):
            _comp, _hash = component_hash.split(':')
            components_hashes[_comp] = _hash


        # ADAPTATION
        components = {}

        if adaptation_type == b'Evolutive':
            components = EvolutiveAdapter(components_hashes).run()
            # return b'Entrei no Evolutive!'
        elif adaptation_type == b'Reactive':
            print('Entrei no Reactive')
        elif args[0] == b'Proactive':
            print('Entrei no Proactive')
        else:
            print('AdaptationManager :: Adaptation ' + adaptation_type + ' is not implemented by Adaptation Manager')

        # RESPONSE ENCODE

        data = '\x1c'.join(
            ['{0}\x1d{1}'.format(comp, components[comp]) for comp in components.keys()]
        )
        data = bytes(data, 'utf-8')
        return data