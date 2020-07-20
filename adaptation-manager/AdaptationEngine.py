from Component import Component
from EvolutiveAdapter import EvolutiveAdapter


class AdaptationEngine(Component):
    # component_library = '/home/david/doutorado/2020-1/amot/adaptation-manager/library'

    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self, *args):
        # REQUEST DECODE
        message = args[0]
        adaptation_type = message['topic']
        message = message['msg'].decode('ascii')

        thing_id, components_versions_str = message.split(' ')

        components_versions = {}
        for component_hash in components_versions_str.split(','):
            _comp, _hash = component_hash.split(':')
            components_versions[_comp] = _hash


        # ADAPTATION
        components = {}

        if adaptation_type == b'Evolutive':
            components = EvolutiveAdapter(components_versions).run()
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