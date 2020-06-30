from EvolutiveMonitor import EvolutiveMonitor
from EvolutiveAnaliser import EvolutiveAnaliser
from EvolutiveExecutor import EvolutiveExecutor

class EvolutiveAdapter(object):
    """docstring for EvolutiveAdapter"""
    def __init__(self, thing_versions):
        self.thing_versions = thing_versions

    def run(self):
        monitor = EvolutiveMonitor().run()
        analiser = EvolutiveAnaliser(monitor.component_library, self.thing_versions).run()
        # TODO EvolutivePlanner
        executor = EvolutiveExecutor(analiser.components_to_adapt).run()

        # print(self.thing_versions)
        # print(monitor.component_library)
        # print(analiser.components_to_adapt)
        # print(executor.data)
        return executor.data
