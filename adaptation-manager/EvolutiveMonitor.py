import os


class EvolutiveMonitor:
    def __init__(self):
        self.component_library = {}

    def run(self):
        versions = open('library/versions.txt', 'r').read()
        comps_versions = [parts.split('#') for parts in versions.split('\n')]
        for (comp, ver) in comps_versions:
            self.component_library[comp] = ver
        # components = os.listdir('library/')
        # for comp_file in components:
        #     comp_name = comp_file.split('.py')[0]
        #     #self.component_library[comp_name] = md5(open('library/' + comp_file, 'rb').read()).hexdigest()
        #     self.component_library[comp_name] = binascii.hexlify(
        #         sha1(open('library/' + comp_file, 'rb').read()
        #             ).digest()).decode('ascii')
        return self
