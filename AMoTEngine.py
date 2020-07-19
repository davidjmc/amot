import time


import config as cfg
import adl as adl

from Executor import Executor


class AMoTEngine:
    def __init__(self):
        self.components = None
        self.components_versions = {}
        self.attachments = None
        self.starter = None
        self.adaptability = None
        self.thing_id = None
        self.last_adaptation = 0
        self.subscriber = None
        self.adaptation_executor = Executor()

        self.current_components = {}

        self.server_configs = cfg.Server
        self.subscriber_configs = cfg.Subscriber
        self.adaptation_configs = cfg.Adaptation
        self.thing_id = b'10'

        self.listen_configs = self.server_configs
        self.listen_configs['timeout'] = None

    def deploy_components(self):
        self.components = adl.Components
        self.attachments = adl.Attachments
        self.starter = adl.Starter
        self.adaptability = adl.Adaptability

    def load_components(self):
        # load components
        for component in self.components:
            component_file = self.components.get(component)
            component_instance = getattr(__import__(component_file), component)
            self.current_components[component] = component_instance().set_engine(self)

        # load versions
        versions = open('versions.txt', 'r').read()
        comps_versions = [parts.split('#') for parts in versions.split('\n')]
        for (comp, ver) in comps_versions:
            self.components_versions[comp] = ver

    def attached(self, component):
        class_name = component.__class__.__name__
        external_class_name = self.attachments.get(class_name)
        external_class = self.current_components[external_class_name]
        return external_class.set_engine(self)

    def set_component_configs(self):
        if 'subscriber' in cfg.Component:
            self.listen_configs = self.subscriber_configs
            self.subscriber = self.current_components['Subscriptor']
            self.subscriber.set_engine(self).run()

    def run(self):

        if self.last_adaptation == 0:
            self.last_adaptation = time.time()

        try:
            self.deploy_components()
            self.load_components()
            self.set_component_configs()

        except OSError as e:
            self.restart_and_reconnect()

        while True:

            try:
                for component in self.starter:
                    print('Engine running component ', component)
                    component_instance = self.current_components[component]
                    component_instance.run()
                if (
                    self.adaptability['kind'] is not None) and (
                    (time.time() - self.last_adaptation) >
                    self.adaptation_configs['timeout']):
                    self.adaptation_executor.set_engine(self).run()
                    self.last_adaptation = time.time()

            except OSError as e:
                self.restart_and_reconnect()


    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        # machine.reset()


class Message(object):
    def __init__(self, operation, topic, message, subscriber_addr = None):
        self.op = operation
        self.topic = topic
        self.subscriber_addr = subscriber_addr
        self.message = message

    def __str__(self):
        return '\n'.join([str(self.op), str(self.topic), str(self.subscriber_addr), str(self.message)])

if __name__ == '__main__':
    AMoTEngine().run()
