from AMoTEngine import Component


class AdaptationManager(Component):
    # component_library = '/home/david/doutorado/2020-1/amot/adaptation-manager/library'

    def __init__(self):
        super().__init__()
        self.component_library = '/libray'

    def run(self, *args):
        request = args[0]
        adaptation_type = request.topic
        message = request.message

        if adaptation_type == b'Evolutive':
            EvolutiveMonitor(self).run()
            # EvolutiveAnalizer().run()
            # EvolutivePlanner().run()
            # EvolutiveExecutor().run()
            return b'Entrei no Evolutive!'
        elif adaptation_type == b'Reactive':
            print('Entrei no Reactive')
        elif args[0] == b'Proactive':
            print('Entrei no Proactive')
        else:
            print('AdaptationManager :: Adaptation ' + adaptation_type + ' is not implemented by Adaptation Manager')