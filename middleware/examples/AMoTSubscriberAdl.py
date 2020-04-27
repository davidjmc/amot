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
    'timeout': 5000,
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
    'Type': None
}