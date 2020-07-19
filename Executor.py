import sys
import binascii
from hashlib import sha1
from hashlib import md5
from Component import Component

class Executor(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        has_adaptation = None

        adaptation = self.engine.adaptability['kind']
        thing_data = None
        if adaptation == b'Evolutive':
            comp_hashes = b','.join(
                [
                    bytes('{0}:'.format(comp), 'ascii') + self.engine.components_hashes[comp] for comp in self.engine.components_hashes.keys()
                ]
            )
            thing_data = self.engine.thing_id + b' ' + comp_hashes

        if thing_data is None:
            return

        data = self.adapt(
            adaptation, thing_data, self.engine.adaptation_configs['host'],
            self.engine.adaptation_configs['port'])


        if not data or type(data) is not bytes:
            return

        data = str(data, 'utf-8')
        files = data.split('\x1c') # FILE SEPARATOR (28)
        for comp_content in files:
            compname, content = comp_content.split('\x1d') # GROUP SEPARATOR (29)
            self.adaptComponent(compname, content)

    def adaptComponent(self, component, data):
        print('===== adapting {0} ====='.format(component))
        file = component + '.py'
        wr = open(file, 'w')
        wr.write(data)
        wr.close()
        self.reloadComponent(component)

    # https://stackoverflow.com/questions/30379893/replacing-an-imported-module-dependency
    def reloadComponent(self, file):
        del sys.modules[file]
        module = __import__(file)
        sys.modules[file] = module
        file_hash = binascii.hexlify(sha1(
                open('{0}.py'.format(file),'rb').read()
            ).digest())
        self.engine.components_hashes[file] = file_hash
        component_instance = getattr(__import__(file), file)
        self.engine.current_components[file] = component_instance().set_engine(self)