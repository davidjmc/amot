class EvolutiveAnaliser():
    """docstring for EvolutiveAnaliser"""
    def __init__(self, local_versions, remote_versions):
        self.local_versions = local_versions
        self.remote_versions = remote_versions
        self.components_to_adapt = []

    def run(self):
        for comp in self.remote_versions.keys():
            if True or self.local_versions.get(comp) and float(self.local_versions[comp]) > float(self.remote_versions[comp]):
                print(self.local_versions[comp], ">", self.remote_versions[comp])
                self.components_to_adapt.append(comp)
        return self