Components = {
    'App': 'App',
    'Subscriptor': 'Subscriptor',
    'ServerRequestHandler': 'ServerRequestHandler',
    'Notifier': 'Notifier',

    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    'ClientRequestHandler': 'ClientRequestHandler',

    'AdaptationProxy': 'AdaptationProxy'
}

Attachments = {
    'ServerRequestHandler': 'Unmarshaller',
    'Unmarshaller': 'Notifier',
    'Notifier': 'App',

    'Subscriptor': 'QueueProxy',
    'QueueProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler',

    'Executor': 'AdaptationProxy',
    'AdaptationProxy': 'Marshaller'
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
    'kind': b'Evolutive'
}
