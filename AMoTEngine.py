import time

import datetime
import config as cfg
import adl as adl


class AmotEngine:

    _times = []
    components = adl.Components
    components['Executor'] = 'Executor'
    attachments = adl.Attachments
    starter = adl.Starter
    adaptability = adl.Adaptability

    config = cfg

    server_configs = listen_configs = cfg.Server
    subscriber_configs = cfg.Subscriber
    adaptation_configs = cfg.Adaptation
    listen_configs['timeout'] = None

    components_versions = {}
    current_components = {}

    thing_id = b'10'

    last_adaptation = 0
    adaptation_executor = None
    subscriber = None

    def __init__(self):
        # load components
        for component in self.components:
            component_file = self.components.get(component)
            imported = __import__(component_file)
            imported.__dict__['AmotEngine'] = self
            component_instance = getattr(imported, component)
            self.current_components[component] = component_instance()

        self.adaptation_executor = self.current_components['Executor']

        # load versions
        versions = open('versions.txt', 'r').read()
        comps_versions = [parts.split('#') for parts in versions.split('\n')]
        for (comp, ver) in comps_versions:
            self.components_versions[comp] = ver

        #setting subscriber
        if 'subscriber' in cfg.Component:
            self.listen_configs = self.subscriber_configs
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

        # try:
        #     self.load_components()
        #     self.set_component_configs()

        # except OSError as e:
        #     self.restart_and_reconnect()

        while True:
            try:
                for component in self.starter:
                    # print('Engine running component ', component)
                    component_instance = self.current_components[component]
                    component_instance.run()
                if (
                    self.adaptability['kind'] is not None
                    and (time.time() - self.last_adaptation) >
                    self.adaptation_configs['timeout']):
                    # it will adapt
                    self.adaptation_executor.run()
                    self.last_adaptation = time.time()


            except OSError as e:
                self.restart_and_reconnect()


    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        # machine.reset()


if __name__ == '__main__':
    AmotEngine().run()
