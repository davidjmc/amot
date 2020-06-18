import os
# import time
from hashlib import md5


class EvolutiveMonitor:
    def __init__(self):
        self.component_library = {}

    def run(self):
        components = os.listdir('library/')
        for comp_file in components:
            comp_name = comp_file.split('.py')[0]
            self.component_library[comp_name] = md5(open('library/' + comp_file, 'rb').read()).hexdigest()
        return self
