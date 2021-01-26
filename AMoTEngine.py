import time

import datetime
import config as cfg
import adl as adl

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
    def publish(app, topic, message):
        AmotEngine.attached(app).run(b'Publish', topic, message)

    @staticmethod
    def subscribe(app, topic):
        AmotEngine.attached(app).run(b'Subscribe', topic)

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
                    self.adaptability['type'] is not None
                    and (time.time() - self.last_adaptation) >
                    self.adaptation_configs['timeout']):
                    # it will adapt
                    # self.adaptation_executor.run()
                    AmotAgent.adapt()
                    self.last_adaptation = time.time()


            except OSError as e:
                self.restart_and_reconnect()


    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        try:
            machine.reset()
        except NameError:
            pass

