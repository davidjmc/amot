Components = {
    'AMoTApp': 'AMoTApp',
    'ServerRequestHandler': 'ServerRequestHandler',
    'Invoker': 'Invoker',

    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Invoker',
    'Invoker': 'AMoTApp',
    
    'AMoTSubscriber': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

Roles = {
    'subscriber'
}

SubscriberConfigs = {
    'timeout': None,
    'topics': ['Hello'],
    'host': '192.168.1.9',
    'port': 60001
}

Configs = {
    'serverHost': '192.168.1.9',
    'serverPort': 60000,
}

Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    'Type': None
}
