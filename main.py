from urllib import response
import boto3
from os import getenv


LOCALSTACK_ENDPOINT_URL = getenv("AWS_ENDPOINT_URL")

client = (boto3.client("sns", endpoint_url=LOCALSTACK_ENDPOINT_URL).list_topics())
