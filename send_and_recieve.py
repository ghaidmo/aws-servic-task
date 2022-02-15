
from create_queue import queue_client, queue
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

response = queue_client.send_message(
    QueueUrl=queue.url,
    MessageBody='Test Message',
    DelaySeconds=123

)
A = queue_client.receive_message(
    QueueUrl=queue.url



)
print(A['Messages'][0]['Body'])
queue_client.delete_message(
    QueueUrl=queue.url,
    ReceiptHandle=A['Messages'][0]['ReceiptHandle']
)
