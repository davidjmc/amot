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


Starter = {
    'Client'
}

Adaptability = {
    'kind': b'Evolutive'
    # 'kind': None
}
