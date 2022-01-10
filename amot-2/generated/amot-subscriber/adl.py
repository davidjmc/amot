adl = {
    'components': {
        'QueueProxy': 'NewQueueProxy', 'Marshaller': 'NewMarshaller', 'ClientRequestHandler': 'NewClientRequestHandler'
    },
    'attachments': {
        'QueueProxy':'Marshaller','Marshaller':'ClientRequestHandler'
    },
    'configuration': {
        'start': 'QueueProxy',
        'ataptability': {
            'type': 'evolutive',
            'timeout': 5
        },
        'otherConfigs': {}
    }
}