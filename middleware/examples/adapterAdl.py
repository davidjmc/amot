Components = {
    'ServerRequestHandler': 'ServerRequestHandler',
    'Invoker': 'Invoker',
    'AdaptationManager': 'AdaptationManager',

    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Invoker',
    'Invoker': 'AdaptationManager',

    'AdaptationManager': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

SubscriberConfigs = { }

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60005,
}

Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    'kind': None
}
