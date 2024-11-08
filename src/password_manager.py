from botocore.exceptions import ClientError
from src.retrieve import retrieve_secret
from src.delete import delete_secret
from src.list import list_sm_secrets
from src.store import store_secret
from pprint import pprint
import boto3


def password_manager_func():
    """ Purpose: Python script that users can run to use the application. """

    sm_client = boto3.client("secretsmanager")
    running = True
    while running:
        user_choice = input("\nPlease specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:")
        if user_choice == "e":
            user_decision_identifier = input("\nPlease enter secret identifier: ")
            user_id = input("\nUser Id: ")
            password = input("\nPassword:")
            print(store_secret(user_id, password, user_decision_identifier, sm_client))
        elif user_choice == "l":
            print(list_sm_secrets(sm_client))
        elif user_choice == "r":
            user_decision_identifier = input("\nPlease enter specified secret to retrieve here: ")
            print(retrieve_secret(user_decision_identifier, sm_client))
        elif user_choice == "d":
            user_decision_identifier = input("\nPlease enter specified secret to delete here: ")
            print(delete_secret(user_decision_identifier, sm_client))
        elif user_choice == "x":
            running = False
            break
        else:
            print("\nInvalid input. Please try again...")

    return print("\nThank you goodbye")


password_manager_func()
