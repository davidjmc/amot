import time
from hashlib import md5


import config as cfg
import adl as adl


class AMoTEngine:
    def __init__(self):
        self.components = None
        self.components_hashes = {}
        self.attachments = None
        self.starter = None
        self.adaptability = None
        self.thing_id = None
        self.last_adaptation = 0
        self.subscriber = AMoTSubscriber()
        self.adaptation_agent = AdaptationAgent()

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
        for component in self.components:
            component_file = self.components.get(component)
            file_hash = md5(
                open('{0}.py'.format(component_file),'rb').read()
            ).hexdigest()
            self.components_hashes[component_file] = file_hash
            component_instance = getattr(__import__(component_file), component)
            self.current_components[component] = component_instance().set_engine(self)

    def attached(self, component):
        class_name = component.__class__.__name__
        external_class_name = self.attachments.get(class_name)
        external_class = self.current_components[external_class_name]
        return external_class.set_engine(self)

    def set_component_configs(self):
        if 'subscriber' in cfg.Component:
            self.listen_configs = self.subscriber_configs
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
                    self.adaptation_agent.set_engine(self).run()
                    self.last_adaptation = time.time()

            except OSError as e:
                self.restart_and_reconnect()


    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        # machine.reset()


class Component:

    def __init__(self):
        self.engine = None

    class Request(object):
        def __init__(self,  operation, topic, message):
            self.op = operation
            self.topic = topic
            self.message = message

    def set_engine(self, engine):
        self.engine = engine
        return self

    def get_engine(self):
        return self.engine

    def run(self, *args):
        pass

    def external(self):
        return self.engine.attached(self)

    def publish(self, topic, message):
        self.external().run(b'Publish', topic, message)

    def subscribe(self, topic):
        self.external().run(b'Subscribe', topic)

    def notify(self, topic, message, ip, port):
        return self.external().run(b'Notify', topic, message, ip, port)

    def adapt(self, adaptability, message, ip, port):
        return self.external().run(b'Adapt', adaptability, message, ip, port)


class AMoTSubscriber(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.subscribe(topic)


class AdaptationAgent(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        has_adaptation = None

        adaptation = self.engine.adaptability['kind']
        thing = self.engine.thing_id
        has_adaptation = self.adapt(
            adaptation, thing, self.engine.adaptation_configs['host'],
            self.engine.adaptation_configs['port'])

        print(has_adaptation)



if __name__ == '__main__':
    AMoTEngine().run()
