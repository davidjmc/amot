Components = {
    'ServerRequestHandler': 'ServerRequestHandler',
    'Invoker': 'Invoker',
    'QueueServer': 'QueueServer',
    
    'ClientProxy': 'ClientProxy',
    'Requestor': 'Requestor',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Invoker',
    'Invoker': 'QueueServer',

    'QueueServer': 'ClientProxy',
    'ClientProxy': 'Requestor',
    'Requestor': 'ClientRequestHandler'
}

Roles = {
    'server'
}

SubscriberConfigs = { }

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
