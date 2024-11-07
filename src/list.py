import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def list_sm_secrets(sm_client):

    try:
        response = sm_client.list_secrets()
        pprint(response)
    except ClientError:
        pass

    return ""