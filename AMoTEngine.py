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

        time_i = 0
        while True:
            self._times.append(('--total0:', time.time()))
            try:
                for component in self.starter:
                    # print('Engine running component ', component)
                    component_instance = self.current_components[component]
                    self._times.append(('--compApp0:', time.time()))
                    component_instance.run()
                    self._times.append(('--compApp1:', time.time()))
                if (
                    self.adaptability['kind'] is not None) and (
                    (time.time() - self.last_adaptation) >
                    self.adaptation_configs['timeout']):
                    self._times.append(('--adapt0:', time.time()))
                    self.adaptation_executor.run()
                    self.last_adaptation = time.time()
                    self._times.append(('--adapt1:', time.time()))


            except OSError as e:
                self.restart_and_reconnect()

            self._times.append(('--total1:', time.time()))

            time_i = int(time_i) + 1
            time_i = str(time_i)
            if 'subscriber' in cfg.Component:
                midApp = [t[1] for t in self._times if t[0][:8] == '--midApp']
                print('#' + time_i + ' midApp: ', midApp[1] - midApp[0])

                app = [t[1] for t in self._times if t[0][:5] == '--app']
                print('#' + time_i + ' app: ', app[1] - app[0])

                adapt = [t[1] for t in self._times if t[0][:7] == '--adapt']
                if len(adapt) == 2:
                    print('#' + time_i + ' adapt: ', adapt[1] - adapt[0])

                net = [t[1] for t in self._times if t[0][:5] == '--net']

                print('--')
                print('#' + time_i + ' MID_COMP_APP: ', 1000 * ((midApp[1] - midApp[0]) - (app[1] - app[0])))
                if len(adapt) == 2:
                    print('#' + time_i + ' MID_COMP_ADAPT: ', 1000 * ((adapt[1] - adapt[0]) - (net[1] - net[0])))
                print('--')
                print('--')

            if 'publisher' in cfg.Component:
                total = [t[1] for t in self._times if t[0][:7] == '--total']
                print('#' + time_i + ' total: ', total[1] - total[0])

                compApp = [t[1] for t in self._times if t[0][:9] == '--compApp']
                print('#' + time_i + ' compApp: ', compApp[1] - compApp[0])

                app = [t[1] for t in self._times if t[0][:5] == '--app']
                print('#' + time_i + ' app: ', app[1] - app[0])

                proxy = [t[1] for t in self._times if t[0][:7] == '--proxy']
                print('#' + time_i + ' proxy: ', proxy[1] - proxy[0])

                mars = [t[1] for t in self._times if t[0][:6] == '--mars']
                print('#' + time_i + ' mars: ', mars[1] - mars[0])

                crh = [t[1] for t in self._times if t[0][:5] == '--crh']
                print('#' + time_i + ' crh: ', crh[1] - crh[0])

                net = [t[1] for t in self._times if t[0][:5] == '--net']
                if len(net) == 2:
                    print('#' + time_i + ' net: ', net[1] - net[0])
                elif len(net) == 4:
                    print('#' + time_i + ' net: ', net[1] - net[0])
                    print('#' + time_i + ' net: ', net[3] - net[2])

                adapt = [t[1] for t in self._times if t[0][:7] == '--adapt']
                if len(adapt) == 2:
                    print('#' + time_i + ' adapt: ', adapt[1] - adapt[0])

                print('--')
                print('#' + time_i + ' MID: ', 1000 * ((compApp[1] - compApp[0]) - (app[1] - app[0])))
                print('#' + time_i + ' MID_COMP_APP: ', 1000 * ((compApp[1] - compApp[0]) - (app[1] - app[0]) - (net[1] - net[0])))
                print('#' + time_i + ' MQTT_EQUIV: ', 1000 * ((proxy[1] - proxy[0]) + (mars[1] - mars[0]) + (crh[1] - crh[0])))
                if len(adapt) == 2:
                    print('#' + time_i + ' MID_COMP_ADAPT: ', 1000 * ((adapt[1] - adapt[0]) - (net[3] - net[2])))
                print('--')
                print('--')
                # print(self._times)

            self._times = []


    @staticmethod
    def restart_and_reconnect():
        import time
        print('Failed to connect to AMoT broker, Reconnecting...')
        time.sleep(10)
        # machine.reset()


if __name__ == '__main__':
    AmotEngine().run()
