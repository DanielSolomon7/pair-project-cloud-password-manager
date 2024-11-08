import boto3
import json
from botocore.exceptions import ClientError
from pprint import pprint


def retrieve_secret(secret_name, sm_client):
    """Looks for the given secret name, and if exists, retrieves the password and username of
        the secret, and stores the name, password, and username in a local txt file.

        Args:
        secret_name: the name of the secret to retreive.
        sm_client (boto3.client): the boto3 client to interact with the AWS API.

        Returns:
        A string informing that the secrets have been saved in a txt file or an informative error
        message.
        """

    try:
        response = sm_client.get_secret_value(SecretId=secret_name)
        with open(f"{secret_name}_secrets.txt","w", encoding="utf-8") as file:
            secrets_json = response["SecretString"]
            secrets_dict= json.loads(secrets_json)
            file.write(f"Name: {secret_name}\nPassword: {secrets_dict['password']}\nUsername: {secrets_dict['username']}")
            return f"Secrets stored in local file: {secret_name}_secrets.txt"

    except ClientError:
        return f"Secret {secret_name} does not exist."
    
    except Exception:
        return "Invalid input. Input must have a minimum length of 1."
