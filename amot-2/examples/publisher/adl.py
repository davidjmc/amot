adl = {
    'components': {
        # ClassName: FileName
        'QueueProxy': 'QueueProxy',
        'Marshaller': 'Marshaller',
        'ClientRequestHandler': 'ClientRequestHandler'
    },
    'attachments': {
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