class EvolutiveExecutor(object):
    """docstring for EvolutiveExecutor"""
    def __init__(self, components, versions):
        self.components = components
        self.versions = versions
        self.data = {}

    def run(self):
        for component in self.components:
            if component == 'Marshaller':
                self.data['Marshaller#0.1'] = open('library/Marshaller.py', 'r').read()
            if component == 'Marshaller-dummy':
                self.data['Marshaller#0.2'] = open('library/Marshaller-dummy.py', 'r').read()
            # self.data[component + '#' + self.versions[component]] = open('library/{0}.py'.format(component), 'r').read()
        return self