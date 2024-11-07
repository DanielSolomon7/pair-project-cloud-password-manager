import boto3
import json
from botocore.exceptions import ClientError
from pprint import pprint


def retrieve_secret(secret_name, sm_client):
    try:
        response = sm_client.get_secret_value(SecretId=secret_name)
        with open(f"{secret_name}_secrets.txt","w", encoding="utf-8") as file:
            secrets_json = response["SecretString"]
            secrets_dict= json.loads(secrets_json)
            file.write(f"Name: {secret_name}\nPassword: {secrets_dict['password']}\nUsername: {secrets_dict['username']}")
            return f"Secrets stored in local file: {secret_name}_secrets.txt"

    except ClientError:
        return f"Secret {secret_name} does not exist."
