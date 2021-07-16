import time

import datetime
import config as cfg
import sys

try:
    import adl as adl
    import appVars as appVars
except:
    # fooling the IDE
    pass

from AMoTAgent import AmotAgent


class AmotEngine:

    components = adl.Components
    attachments = adl.Attachments
    starter = adl.Starter
    adaptability = adl.Adaptability

    config = cfg

    ip = None

    _broker = cfg.broker
    _server = cfg.server
    _app_vars = cfg.app_vars
    _listen = {
        'timeout': None,
        'port': cfg.thing.get('listen_port')
    }

    current_components = {}

    last_adaptation = 0
    adaptation_executor = None
    subscriber = None

    def __init__(self, self_ip):
        self.ip = self_ip
        # load components
        for component in self.components:
            component_file = self.components.get(component)
            namespace = __import__('components.' + component_file)
            component_module = getattr(namespace, component_file)
            # component_module.__dict__['AmotEngine'] = self
            setattr(component_module, 'AmotEngine', self)
            setattr(component_module, 'appVars', appVars)
            component_instance = getattr(component_module, component)
            self.current_components[component] = component_instance()

        # # load versions
        # versions = open('versions.txt', 'r').read()
        # comps_versions = [parts.split('#') for parts in versions.split('\n')]
        # for (comp, ver) in comps_versions:
        #     self.components_versions[comp] = ver

        #setting subscriber
        if 'subscriber' in cfg.app_vars.get('mode'):
            self.subscriber = self.current_components['App']
            self.subscriber.subscribe()

    @staticmethod
    def publish(app, topic, message, context = {}):
        AmotAgent.app_context = context
        AmotEngine.attached(app).run(b'Publish', topic, bytes(cfg.thing['id'], 'ascii'), message)

    @staticmethod
    def subscribe(app, topic):
        AmotEngine.attached(app).run(b'Subscribe', topic, bytes(cfg.thing['id'], 'ascii'))

    @staticmethod
    def attached(component):
        class_name = component.__class__.__name__
        external_class_name = AmotEngine.attachments.get(class_name)
        external_class = AmotEngine.current_components[external_class_name]
        return external_class

    def run(self):
        if AmotEngine.last_adaptation == 0:
            AmotEngine.last_adaptation = time.time()

        while True:
            try:
                for component in self.starter:
                    # print('Engine running component ', component)
                    component_instance = self.current_components[component]
                    component_instance.run()

                if (
                    self.adaptability['type'] != ''
                    and (time.time() - self.last_adaptation) > self.adaptability['timeout']):
                    # it will adapt
                    # self.adaptation_executor.run()
                    updated = AmotAgent.adapt()
                    if updated:
                        self.reload_components()
                    self.last_adaptation = time.time()


            except OSError as e:
                print(e)
                self.restart_and_reconnect()

    def reload_components(self):
        del sys.modules['adl']
        del sys.modules['appVars']
        new_adl = __import__('adl')
        new_appVars = __import__('appVars')
        sys.modules['adl'] = new_adl
        sys.modules['appVars'] = new_appVars

        self.components = getattr(new_adl, 'Components')
        self.attachments = getattr(new_adl, 'Attachments')
        self.starter = getattr(new_adl, 'Starter')
        self.adaptability = getattr(new_adl, 'Adaptability')
        for module in [module for module in sys.modules.keys() if module[:11] == 'components.']:
            del sys.modules[module]

        for component in self.components:
            component_file = self.components.get(component)
            namespace = __import__('components.' + component_file)
            component_module = getattr(namespace, component_file)
            # component_module.__dict__['AmotEngine'] = self
            setattr(component_module, 'AmotEngine', self)
            setattr(component_module, 'appVars', new_appVars)
            component_instance = getattr(component_module, component)
            self.current_components[component] = component_instance()
        # gc.collect()




    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        try:
            machine.reset()
        except NameError:
            pass


