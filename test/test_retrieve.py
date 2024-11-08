from src.retrieve import retrieve_secret
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

class TestRetrieve:

    def test_function_takes_a_secret_name_and_sm_client_and_returns_a_string(self, secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"

        assert isinstance(retrieve_secret(test_secret_name, test_client),str)


    def test_function_retrieves_a_secret_and_stores_in_a_text_file(self, secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"
        test_client.create_secret(Name=test_secret_name, SecretString='{"username":"user1", "password":"password1"}')

        assert retrieve_secret(test_secret_name, test_client) == f"Secrets stored in local file: {test_secret_name}_secrets.txt"

    def test_function_handles_when_a_secret_name_that_does_not_exist_is_given(self,  secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = "name1"

        assert retrieve_secret(test_secret_name, test_client) == f"Secret {test_secret_name} does not exist."

    def test_function_handles_empty_input(self, secrets_manager_client):
        test_client = secrets_manager_client
        test_secret_name = ""

        assert retrieve_secret(test_secret_name, test_client) == "Invalid input. Input must have a minimum length of 1."