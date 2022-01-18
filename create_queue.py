
import boto3
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")
sqs = boto3.resource('sqs', endpoint_url=LOCALSTACK_ENDPOINT_URL)

client = boto3.client(
    "sqs", endpoint_url=LOCALSTACK_ENDPOINT_URL)

response = client.create_queue(
    QueueName='MyQueue'
)
queue = sqs.get_queue_by_name(
    QueueName='MyQueue'
)
print(queue)
