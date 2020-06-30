Components = {
    'ServerRequestHandler': 'ServerRequestHandler',
    'Marshaller': 'Marshaller',
    'Invoker': 'Invoker',
    'QueueServer': 'QueueServer',

    'ClientProxy': 'ClientProxy',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    'ClientRequestHandler': 'ClientRequestHandler'
}

Attachments = {
    'ServerRequestHandler': 'Unmarshaller',
    'Unmarshaller': 'QueueServer',

    'QueueServer': 'ClientProxy',
    'ClientProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler'

    # 'ServerRequestHandler->Marshaller->QueueServer',
    # 'QueueServer->ClientProxy->Marshaller->ClientRequestHandler'
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
    'kind': None
}
