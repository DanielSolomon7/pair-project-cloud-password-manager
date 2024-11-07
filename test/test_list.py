from src.list import list_sm_secrets
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
def secrets_manager_client(aws_credentials):
    with mock_aws():
        secrets_manager = boto3.client("secretsmanager")
        yield secrets_manager

class TestList:

    def test_function_takes_a_sm_client_and_returns_a_string(self, secrets_manager_client):
        test_client = secrets_manager_client
        assert isinstance(list_sm_secrets(test_client), str)

    def test_function_lists_all_stored_secrets(self, secrets_manager_client):
        test_client = secrets_manager_client

        response1 = store_secret("user", "password", "i1", test_client)
        response2 = store_secret("user", "password", "i2", test_client)

        
        # test_client.create_secret(Name="identifier1",
        #                                     SecretString='{"username":"user1", "password":"password1"}')
        # test_client.create_secret(Name="identifier2",
        #                                     SecretString='{"username":"user2", "password":"password2"}')
    
        response = list_sm_secrets(test_client)

        assert response == "2 secret(s) available: [identifier1, identifier2]"

    # def test_function_returns_error_message(self,  secrets_manager_client):
    #     pass
