import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def list_sm_secrets(sm_client):
    try:
        response = sm_client.list_secrets()
        secret_names = [secret["Name"] for secret in response["SecretList"]]
        return f"{len(secret_names)} secret(s) available: {secret_names}"
    except ClientError:
        pass
