from src.delete import delete_secret
from moto import mock_aws
import pytest
import boto3
import os


@pytest.fixture()
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = 'test'
    os.environ["AWS_SECRET_ACCESS_KEY"] = 'test'
    os.environ["AWS_SECURITY_TOKEN"] = 'test'
    os.environ["AWS_SESSION_TOKEN"] = 'test'
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

@pytest.fixture()
def secrets_manager_client(aws_credentials):
    with mock_aws():
        secrets_manager = boto3.client("secretsmanager")
        yield secrets_manager

class TestDelete:

    def test_function_takes_a_secret_name_and_sm_client_and_returns_a_string(self, secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"

        assert isinstance(delete_secret(test_secret_name, test_client),str)

    def test_function_deletes_a_secret_when_valid_name_given(self, secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"
        test_client.create_secret(Name=test_secret_name, SecretString='{"username":"user1", "password":"password1"}')

        assert delete_secret(test_secret_name, test_client) == "Deleted"

        list_of_secrets = test_client.list_secrets()
        secret_names = [secret["Name"] for secret in list_of_secrets["SecretList"]]
        assert len(secret_names) == 0

    def test_function_returns_error_message_when_invalid_name_given(self,  secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"
        assert delete_secret(test_secret_name, test_client) == f"Secret name invalid - secret {test_secret_name} does not exist."

