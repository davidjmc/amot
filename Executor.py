import sys
from Component import Component

class Executor(Component):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def run(self):
        has_adaptation = None

        adaptation = self.engine.adaptability['kind']
        thing_data = None
        if adaptation == b'Evolutive':
            comp_versions = b','.join(
                [
                    bytes('{0}:{1}'.format(comp,self.engine.components_versions[comp]), 'ascii') for comp in self.engine.components_versions.keys()
                ]
            )
            thing_data = self.engine.thing_id + b' ' + comp_versions

        if thing_data is None:
            return

        data = self.engine.attached(self).run(
            adaptation, thing_data, self.engine.adaptation_configs['host'],
            self.engine.adaptation_configs['port'])


        if not data or type(data) is not bytes:
            return

        data = str(data, 'utf-8')
        files = data.split('\x1c') # FILE SEPARATOR (28)
        for comp_content in files:
            compname_version, content = comp_content.split('\x1d') # GROUP SEPARATOR (29)
            compname, compversion = compname_version.split('#')
            self.adaptComponent(compname, compversion, content)

    def adaptComponent(self, component, version, data):
        print('===== adapting {0} ====='.format(component))
        file = component + '.py'
        wr = open(file, 'w')
        wr.write(data)
        wr.close()
        self.reloadComponent(component, version)

    # https://stackoverflow.com/questions/30379893/replacing-an-imported-module-dependency
    def reloadComponent(self, file, version):
        print(file, version)
        del sys.modules[file]
        module = __import__(file)
        sys.modules[file] = module
        self.engine.components_versions[file] = version
        fp = open('versions.txt', 'w')

        i = 0
        for _file in self.engine.components_versions.keys():
            data = ("\n" if i != 0 else "") + _file + '#' + self.engine.components_versions[_file]
            fp.write(data)
            i += 1
        fp.close()

        component_instance = getattr(__import__(file), file)
        self.engine.current_components[file] = component_instance(self.engine)