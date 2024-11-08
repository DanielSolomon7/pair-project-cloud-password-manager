

def delete_secret(secret_name, sm_client):

    """Looks for the given secret name, and if exists, deletes the secret.

        Args:
        secret_name: the name of the secret to delete.
        sm_client (boto3.client): the boto3 client to interact with the AWS API.

        Returns:
        A string informing that the secret has been deleted or an informative error
        message.
        """

    list_of_secrets = sm_client.list_secrets()
    secret_names = [secret["Name"] for secret in list_of_secrets["SecretList"]]

    if secret_name in secret_names:
        sm_client.delete_secret(SecretId=secret_name,
                                            ForceDeleteWithoutRecovery=True)
        return "Deleted"

    else:
        return f"Secret name invalid - secret {secret_name} does not exist."