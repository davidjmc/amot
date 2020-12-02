class EvolutiveExecutor(object):
    """docstring for EvolutiveExecutor"""
    def __init__(self, components, versions):
        self.components = components
        self.versions = versions
        self.data = {}

    def run(self):
        for component in self.components:
            self.data[component + '#' + self.versions[component]] = open('library/{0}.py'.format(component), 'r').read()
        return self