
from create_queue import queue, queue_client
from main import client
from create_topics import topic

queue_attributes = queue_client.get_queue_attributes(
    QueueUrl=queue.url,
    AttributeNames=[
        'QueueArn'
    ]

)
# print(queue_attributes['Attributes']['QueueArn'])
response = client.subscribe(
    TopicArn=topic['TopicArn'],
    Protocol='sqs',
    Endpoint=queue_attributes['Attributes']['QueueArn'],
)
