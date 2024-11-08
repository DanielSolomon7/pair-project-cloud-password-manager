import boto3
from botocore.exceptions import ClientError
from pprint import pprint


def store_secret(user_id, password, identifier, sm_client):
    """Takes a user_id, password, identifier_name, and creates a secret with these credentials.

        Args:
        user_id: the username for the secret.
        password: the password for the secret.
        identifier: the name for the secret.
        sm_client (boto3.client): the boto3 client to interact with the AWS API.

        Returns:
        A string informing that the secret has been deleted or an informative error
        message.
        """

    try:
        response = sm_client.create_secret(Name=identifier,
                                            SecretString='{"username":"% s", "password":"% s"}' %
                                            (user_id, password))
        return "Secret saved."

    except ClientError:
        return "User name already in use."
    
    except Exception:
        return "Invalid input. Input must have a minimum length of 1."

