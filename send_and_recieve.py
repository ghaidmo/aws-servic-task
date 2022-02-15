import boto3
from create_queue import sqs, client, queue
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

response = client.send_message(
    QueueUrl=queue.url,
    MessageBody='Test Message',
    DelaySeconds=123

)
A = client.receive_message(
    QueueUrl=queue.url



)
print(A['Messages'][0]['Body'])
client.delete_message(
    QueueUrl=queue.url,
    ReceiptHandle=A['Messages'][0]['ReceiptHandle']
)
