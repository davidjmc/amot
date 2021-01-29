Components = {
    'AMoTClient': 'AMoTClient2',
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
    'Requestor': 'ClientRequestHandler',

    'AMoTClient': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

Roles = {
    'publisher',
    'subscriber'
}

SubscriberConfigs = {
    'timeout': 5000,
    'topics': ['Hello'],
    'host': '192.168.0.102',
    'port': 60002,
    'component': 'AMoTSubscriber'
}

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000,
}

Starter = {
    'AMoTClient', 'ServerRequestHandler'
}

Adaptability = {
    'Type': None
}