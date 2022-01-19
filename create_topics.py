import boto3
from os import getenv
LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")


client = boto3.client(
    "sns", endpoint_url=LOCALSTACK_ENDPOINT_URL)

topic = client.create_topic(
    Name='MyTopic'
)

topics_list = client.list_topics()
for i in topics_list['Topics']:
    print(i)
