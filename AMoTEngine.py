import time


import AMoTConfig as cfg
import AMoTAdl as adl


class AMoTEngine:
    def __init__(self):
        self.server_config = cfg.ServerConfigs
        self.components = None
        self.attachments = None
        self.starter = None
        self.adaptability = None
        self.roles = None
        self.subscriber_configs = {}
        self.configs = {}
        self.current_components = {}
        self.listen_cfg = {}
        self.adaptation_configs = {}

    def set_configuration(self):
        pass
        # import AMoTConfig as cfg

        # old version - up to amot v2
        # amot_cfg = dict()
        # cfg_file = 'AMoTConfig.py'
        # exec(open(cfg_file).read(), amot_cfg)
        # self.roles = amot_cfg['Roles']
        # self.subscriber_configs = amot_cfg['SubscriberConfigs']
        # self.configs = amot_cfg['ServerConfigs']
        # self.adaptation_configs = amot_cfg['Adaptation']
        # # improve this -> how?
        # self.listen_cfg['host'] = self.configs['serverHost']
        # self.listen_cfg['port'] = self.configs['serverPort']
        # self.listen_cfg['timeout'] = None

    def deploy_components(self):
        # new version
        self.components = adl.Components
        self.attachments = adl.Attachments
        self.starter = adl.Starter
        self.adaptability = adl.Adaptability

        # old version - up to AMoT v2
        # adl_cfg = dict()
        # adl_file = 'AMoTAdl.py'
        # exec(open(adl_file).read(), adl_cfg)
        # self.components = adl_cfg['Components']
        # self.attachments = adl_cfg['Attachments']
        # self.starter = adl_cfg['Starter']
        # self.adaptability = adl_cfg['Adaptability']

    def load_components(self):
        for component in self.components:
            component_file = self.components.get(component)
            component_instance = getattr(__import__(component_file), component)
            self.current_components[component] = component_instance().set_engine(self)

    def attached(self, component):
        class_name = component.__class__.__name__
        external_class_name = self.attachments.get(class_name)
        external_class = self.current_components[external_class_name]
        return external_class.set_engine(self)

    # def check_roles(self):
    #     if 'subscriber' in self.roles:
    #         self.listen_cfg['host'] = self.subscriber_configs['host']
    #         self.listen_cfg['port'] = self.subscriber_configs['port']
    #         if self.subscriber_configs['timeout'] is not None:
    #             self.listen_cfg['timeout'] = self.subscriber_configs['timeout'] / 1000.0
    #         AMoTSubscriber().set_engine(self).run()

    def run(self):
        last_adaptation = 0
        try:
            self.set_configuration()
            self.deploy_components()
            self.load_components()
            # self.check_roles()
            # self.connect()
            if cfg.Component is 'Subscriber':
                self.listen_cfg['host'] = self.subscriber_configs['host']
                self.listen_cfg['port'] = self.subscriber_configs['port']
                if self.subscriber_configs['timeout'] is not None:
                    self.listen_cfg['timeout'] = self.subscriber_configs['timeout'] / 1000.0
                AMoTSubscriber().set_engine(self).run()

        except OSError as e:
            self.restart_and_reconnect()

        while True:
            print(cfg.Adaptation)
            try:
                for component in self.starter:
                    # print('Engine running component ', component)
                    component_instance = self.current_components[component]
                    component_instance.run()

                    if self.adaptability['Type'] is not None:
                        self.adaptation_configs = cfg.Adaptation
                        if (time.time() - last_adaptation) > cfg.Adaptation['timeout']:
                            # starts adaptation
                            last_adaptation = time.time()

            except OSError as e:
                self.restart_and_reconnect()

            # time.sleep(1)

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
        def __init__(self,  operation, topic, *args):
            self.op = operation
            self.topic = topic
            self.args = [m for m in args]

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


class AMoTSubscriber(Component):
    def __init__(self):
        super().__init__()

    def run(self):
        for topic in self.engine.subscriber_configs['topics']:
            self.subscribe(topic)


if __name__ == '__main__':
    AMoTEngine().run()
