import boto3
from create_queue import sqs, client, queue
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

client = boto3.client(
    "sqs", endpoint_url=LOCALSTACK_ENDPOINT_URL)


response = client.send_message(
    QueueUrl=queue.url,
    MessageBody='Test Message',
    DelaySeconds=123

)
A = client.receive_message(
    QueueUrl=queue.url



)
print(A)
response = client.delete_message(
    QueueUrl='http://localhost:4566/000000000000/MyQueue',
    ReceiptHandle='msrctrjxsafaypqmgtjoeavwarmnouumrryqlkmmnlcjiggwtxsciukpdirkegyggshulyjtwyeuyisbmujqxzbghmczcmezrbxxmohtsczjqmugjtvmzzcnivzezxtanuvibqnrlojzlhpnhbgzegkbccbrswkwoobzazsxnubxegolwiubqzutj'
)
