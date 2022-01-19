
from subscribe_sqs_to_sns import client
from create_queue import queue, queue_client
response = client.publish(
    TopicArn='string'
)

A = queue_client.receive_message(
    QueueUrl=queue.url
)


queue_client.delete_message(
    QueueUrl=queue.url,
    ReceiptHandle=A['Messages'][0]['ReceiptHandle']
)
