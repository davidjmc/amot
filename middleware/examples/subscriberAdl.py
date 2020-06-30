Components = {
    'App': 'App',
    'ServerRequestHandler': 'ServerRequestHandler',
    #'Invoker': 'Invoker',
    'Notifier': 'Notifier',

    #'ClientProxy': 'ClientProxy',
    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    #'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    #'ServerRequestHandler': 'Invoker',
    'ServerRequestHandler': 'Marshaller',
    #'Invoker': 'App',
    'Marshaller': 'Notifier',
    'Notifier': 'App',

    #'AMoTSubscriber': 'ClientProxy',
    'AMoTSubscriber': 'QueueProxy',
    #'ClientProxy': 'Requestor',
    'QueueProxy': 'Marshaller',
    #'Requestor': 'ClientRequestHandler'
    'Marshaller': 'ClientRequestHandler'
}

Roles = {
    'subscriber'
}

SubscriberConfigs = {
    'timeout': None,
    'topics': ['Hello'],
    'host': '192.168.0.102',
    'port': 60001
}

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000,
}

Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    'kind': None
}
