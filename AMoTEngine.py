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

# client_type = None -> When used for the AMoT Client
# client_type = 'Subscriber' -> When used for the AMoT Broker
client_type = 'Subscriber'


class AMoTEngine:
    def __init__(self):
        self.components = None
        self.attachments = None
        self.starter = None
        self.adaptability = None
        self.current_components = {}

    def deploy_components(self):
        adl_cfg = dict()
        adl_file = 'AMoTAdl.py'
        exec(open(adl_file).read(), adl_cfg)
        self.components = adl_cfg['Components']
        self.attachments = adl_cfg['Attachments']
        self.starter = adl_cfg['Starter']
        self.adaptability = adl_cfg['Adaptability']

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

    def run(self):
        global last_adaptation
        try:
            self.deploy_components()
            self.load_components()
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

                if client_type is 'Subscriber':
                    SubscriberHandler().notify_handler(amot_client_ip, amot_client_port)

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


class SubscriberHandler:
    def __init__(self):
        self.handler_sock = None

    def notify_handler(self, ip, port):

        try:
            self.handler_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.handler_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            handler_address = socket.getaddrinfo(ip, port)[0][-1]

            try:
                self.handler_sock.bind(handler_address)
                print('Starting up on {} port {}'.format(*handler_address))
                self.handler_sock.listen(1)
            except OSError as e:
                print('SubscriberHandler Bind Error: ', e)

        except OSError as e:
            print('SubscriberHandler Socket Error: ', e)

        while True:
            buffer_size = 536
            data = b''

            try:
                conn, client = self.handler_sock.accept()
                # print('Connected by', client)

                while True:
                    part = conn.recv(buffer_size)
                    data += part

                    if len(part) < buffer_size:
                        break

                message = pickle.loads(data)
                print('<Message> :: ' + message)
                conn.close()
            except OSError as e:
                print('Error when receiving data on the SubscriberHandler: ', e)


if __name__ == '__main__':
    AMoTEngine().run()
