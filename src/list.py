from botocore.exceptions import ClientError


def list_sm_secrets(sm_client):
    """Lists the number of and names of the secrets that exist in the Secret Manager.

        Args:
        sm_client (boto3.client): the boto3 client to interact with the AWS API.

        Returns:
        A string informing with the number of secrets and a list of the names.
        """

    try:
        response = sm_client.list_secrets()
        secret_names = [secret["Name"] for secret in response["SecretList"]]
        return f"{len(secret_names)} secret(s) available: {secret_names}"
    except ClientError:
        pass
