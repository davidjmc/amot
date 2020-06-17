import os
import time


class EvolutiveMonitor():
    def __init__(self):
        self.component_library = None

    def run(self):
        component_library = '/home/david/doutorado/2020-1/amot/adaptation-manager/library'
        before = self.files_to_timestamp(component_library)

        while True:
            print('Evolutive Monitor!')
            after = self.files_to_timestamp(component_library)

            added = [f for f in after if not f in before]

            removed = [f for f in before if not f in after]

            modified = []
            for f in before.keys():
                if not f in removed:
                    if os.path.getmtime(f) != before.get(f):
                        modified.append(f)

            if modified:
                print('SIM')

            if added:
                pass

            before = after

            time.sleep(30)

    @staticmethod
    def files_to_timestamp(path):
        files = [os.path.join(path, f) for f in os.listdir(
            path) if f.endswith('.py')]
        return dict([(f, os.path.getmtime(f)) for f in files])