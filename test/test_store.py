from src.store import store_secret
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
def secrets_manager_client():
    with mock_aws():
        secrets_manager = boto3.client("secretsmanager")
        yield secrets_manager

class TestStore:

    def test_function_takes_user_id_and_password_as_string_and_secrets_client_and_returns_a_string(self, secrets_manager_client):
        test_id = "User"
        test_password = "Password"
        test_client = secrets_manager_client

        assert isinstance(store_secret( test_id, test_password, test_client),str)

    def test_function_creates_secret_when_valid_input_is_given(self, secrets_manager_client):
        test_id = "User"
        test_password = "Password"
        test_client = secrets_manager_client
        response = store_secret(test_id, test_password, test_client)
        expected = "Secret saved."

        assert response == expected
        assert test_client.get_secret_value(SecretId=test_id)['SecretString'] == '{"username":"User", "password":"Password"}'

    def test_function_returns_error_message(self,  secrets_manager_client):
        test_id = "User"
        test_password = "Password"
        test_client = secrets_manager_client
        response1 = store_secret(test_id, test_password, test_client)
        response2 = store_secret(test_id, test_password, test_client)
        expected = "User name already in use."

        assert response2 == expected
