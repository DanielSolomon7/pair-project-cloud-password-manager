import boto3
import json
from botocore.exceptions import ClientError
from pprint import pprint


def delete_secret(secret_name, sm_client):
    
    list_of_secrets = sm_client.list_secrets()
    secret_names = [secret["Name"] for secret in list_of_secrets["SecretList"]]

    if secret_name in secret_names:
        response = sm_client.delete_secret(SecretId=secret_name,
                                             ForceDeleteWithoutRecovery=True)
        return "Deleted"

    else:
        return f"Secret name invalid - secret {secret_name} does not exist."