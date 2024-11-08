""" This whole file has been commented out for deployment """
# from src.password_manager import password_manager_func
# from src.list import list_sm_secrets
# from src.store import store_secret
# from moto import mock_aws
# import pytest
# import boto3
# import os
# import unittest
# from unittest.mock import patch


# @pytest.fixture()
# def aws_credentials():
#     os.environ["AWS_ACCESS_KEY_ID"] = 'test'
#     os.environ["AWS_SECRET_ACCESS_KEY"] = 'test'
#     os.environ["AWS_SECURITY_TOKEN"] = 'test'
#     os.environ["AWS_SESSION_TOKEN"] = 'test'
#     os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


# @pytest.fixture()
# def secrets_manager_client(aws_credentials):
#     with mock_aws():
#         secrets_manager = boto3.client("secretsmanager")
#         yield secrets_manager


# class TestPasswordManager:

#     # @patch('builtins.input', return_value="e")
#     # def test_function_allows_user_to_enter_a_secret(self, secrets_manager_client):
#     #     result = password_manager_func()
#     #     expected = "Secrets stored in local file: secret_secrets.txt"
#     #     self.assertEqual(result, expected)

#     def test_user_can_exit_function(self):
#         expected = print("\nThank you goodbye")
#         assert password_manager_func() == expected

#     # def test_function_recognises_invalid_input(self, capsys):
#     #     password_manager_func()
#     #     captured = capsys.readouterr()
#     #     assert captured.out == "\nInvalid input. Please try again..."

