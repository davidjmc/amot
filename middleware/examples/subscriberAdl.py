Components = {
    'App': 'LoggerSubscriber',
    'Subscriptor': 'Subscriptor',
    'ServerRequestHandler': 'ServerRequestHandler',
    'Notifier': 'Notifier',

    'QueueProxy': 'QueueProxy',
    'Marshaller': 'Marshaller',
    'Unmarshaller': 'Unmarshaller',
    'ClientRequestHandler': 'ClientRequestHandler',
}

Attachments = {
    'ServerRequestHandler': 'Unmarshaller',
    'Unmarshaller': 'Notifier',
    'Notifier': 'App',

    # 'Subscriptor': 'QueueProxy',
    'App': 'QueueProxy',
    'QueueProxy': 'Marshaller',
    'Marshaller': 'ClientRequestHandler'
}


Starter = {
    'ServerRequestHandler'
}

Adaptability = {
    # 'kind': b'Evolutive'
    'kind': None
}
