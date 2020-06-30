Components = {
    'App': 'App',
    'Subscriptor': 'Subscriptor',
    'ServerRequestHandler': 'ServerRequestHandler',
    #'Invoker': 'Invoker',
    'Notifier': 'Notifier',

    #'ClientProxy': 'ClientProxy',
    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    #'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    #'ServerRequestHandler': 'Invoker',
    'ServerRequestHandler': 'Unmarshaller',
    #'Invoker': 'App',
    'Unmarshaller': 'Notifier',
    'Notifier': 'App',
    #'ServerRequestHandler->Marshaller->Notifier->App',

    #'AMoTSubscriber': 'ClientProxy',
    'Subscriptor': 'QueueProxy',
    #'ClientProxy': 'Requestor',
    'QueueProxy': 'Marshaller',
    #'Requestor': 'ClientRequestHandler'
    'Marshaller': 'ClientRequestHandler'
    #'Subscriptor->QueueProxy->Marshaller->ClientRequestHandler'
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
