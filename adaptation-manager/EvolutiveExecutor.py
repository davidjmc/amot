class EvolutiveExecutor(object):
    """docstring for EvolutiveExecutor"""
    def __init__(self, components):
        self.components = components
        self.data = {}

    def run(self):
        for component in self.components:
            self.data[component] = open('library/{0}.py'.format(component), 'r').read()
        return self