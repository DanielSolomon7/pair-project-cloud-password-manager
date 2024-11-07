from src.password_manager import password_manager_func
from src.list import list_sm_secrets
from src.store import store_secret
from moto import mock_aws
import pytest
import boto3
import os


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

class TestPasswordManager:

    def test_function_(self, secrets_manager_client):
        pass

    def test_function_(self, secrets_manager_client):
        pass

    def test_function_(self,  secrets_manager_client):
        pass

