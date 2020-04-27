import pickle
import socket
import time

# Adaptation Check Interval
last_adaptation = 0
adaptation_interval = 1

# AMoT-Broker IP Address and Port
amot_broker_ip = '192.168.1.9'
amot_broker_port = 60000

# Own AMoT-Client IP Address and Port
amot_client_ip = '192.168.1.9'
amot_client_port = 60001


class AMoTEngine:
    def __init__(self):
        self.components = None
        self.attachments = None
        self.starter = None
        self.adaptability = None
        self.roles = None
        self.subscriber_configs = {}
        self.configs = {}
        self.current_components = {}
        self.server_cfg = {}

    def deploy_components(self):
        adl_cfg = dict()
        adl_file = 'AMoTAdl.py'
        exec(open(adl_file).read(), adl_cfg)
        self.components = adl_cfg['Components']
        self.attachments = adl_cfg['Attachments']
        self.starter = adl_cfg['Starter']
        self.adaptability = adl_cfg['Adaptability']
        self.roles = adl_cfg['Roles']
        self.subscriber_configs = adl_cfg['SubscriberConfigs']
        self.configs = adl_cfg['Configs']
        self.server_cfg['host'] = self.configs['serverHost']
        self.server_cfg['port'] = self.configs['serverPort']

    def load_components(self):
        for component in self.components:
            component_file = self.components.get(component)
            component_class = getattr(__import__(component_file), component)
            self.current_components[component] = component_class()

    def attached(self, component):
        class_name = component.__class__.__name__
        external_class_name = self.attachments.get(class_name)
        external_class = self.current_components[external_class_name]
        return external_class.set_engine(self)

    def check_roles(self):
        if 'subscriber' in self.roles:
            self.server_cfg['host'] = self.subscriber_configs['host']
            self.server_cfg['port'] = self.subscriber_configs['port']
            AMoTSubscriber().set_engine(self).run()

    def run(self):
        global last_adaptation
        try:
            self.deploy_components()
            self.load_components()
            self.check_roles()
            # self.connect()
        except OSError as e:
            self.restart_and_reconnect()

        while True:
            try:
                for component in self.starter:
                    component_class = self.current_components[component]
                    component_class.set_engine(self).run()

                    if self.adaptability['Type'] is not None:
                        if (time.time() - last_adaptation) > adaptation_interval:
                            last_adaptation = time.time()

            except OSError as e:
                self.restart_and_reconnect()

            time.sleep(1)

    @staticmethod
    def restart_and_reconnect():
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        # machine.reset()


class Component:
    def __init__(self):
        self.engine = None

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
        self.external().run('Publish', topic, message)

    def subscribe(self, topic):
        self.external().run('Subscribe', topic)


class AMoTSubscriber(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.subscribe(topic)

if __name__ == '__main__':
    AMoTEngine().run()
