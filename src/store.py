import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def store_secret(user_id, password, sm_client):
    try:
        response = sm_client.create_secret(Name=user_id,
                                            SecretString='{"username":"% s", "password":"% s"}' %
                                            (user_id, password))
        return "Secret saved."

    except ClientError:
        return "User name already in use."

