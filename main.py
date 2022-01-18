from urllib import response
import boto3
from os import getenv

from websockets import client

LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

print(getenv('AWS_ACCESS_KEY_ID'))

print(boto3.client("sns", endpoint_url=LOCALSTACK_ENDPOINT_URL).list_topics())
