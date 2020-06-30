Components = {
    'Client': 'Client',
    'QueueProxy': 'QueueProxy',
    # 'ClientProxy': 'ClientProxy',
    # 'Requestor': 'Requestor',
    'Marshaller': 'Marshaller',
    'ClientRequestHandler': 'ClientRequestHandler',
    'AdaptationProxy': 'AdaptationProxy'
}

Attachments = {
    'Client': 'QueueProxy',
    'QueueProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler',

    'Executor': 'AdaptationProxy',
    'AdaptationProxy': 'Marshaller'
}


SubscriberConfigs = { }

Configs = {
    'serverHost': '192.168.0.102',
    'serverPort': 60000
}

Starter = {
    'Client'
}

Adaptability = {
    'kind': b'Evolutive'
    # 'kind': None
}
