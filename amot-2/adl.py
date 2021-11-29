adl = {
    'components': {
        'QueueProxy': 'QueueProxy',
        'Marshaller': 'Marshaller',
        'ClientRequestHandler': 'ClientRequestHandler'
    },
    'attachments': {
        'App':'QueueProxy',
        'QueueProxy':'Marshaller',
        'Marshaller':'ClientRequestHandler'
    },
    'configuration': {
        'start': 'QueueProxy',
        'adaptability': {
            'type': 'evolutive',
            'timeout': 420
        },
        'scalability': {}
    }
}