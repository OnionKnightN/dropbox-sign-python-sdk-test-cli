from config import api_key,client_id,template_id

from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

from endpoints.account_endpoints import *
from endpoints.api_app_endpoints import *
from endpoints.bulk_send_endpoints import *
from endpoints.embedded_endpoints import *
from endpoints.oauth_endpoints import *
from endpoints.report_endpoints import *
from endpoints.signature_request_endpoints import *
from endpoints.team_endpoints import *
from endpoints.template_endpoints import *
from endpoints.unclaimed_draft_endpoints import *
import requests
import uuid
import base64


from pprint import pprint
from sys import exit
from textwrap import dedent

while True:

    print(dedent("""
    *********************************************************************************
    ***************************   Dropbox Sign Console App   ***************************
    *********************************************************************************

    Please choose which funitionality you would like to achieve on the Dropbox Sign Console App.

    Enter the letter corresponding to the action type. 

    A. Account Endpoints
    B. API App Endpoints
    C. Bulk Send Job Endpoints
    D. Embedded Endpoints
    E. Exit
    F. OAuth Endpoints
    G. Report Endpoints
    H. Signature Request Endpoints
    I. Team Endpoints
    J. Template Endpoints
    K. Unclaimed Draft Endpoints.
    L. Test Endpoints

    *********************************************************************************
    """))

    def test():

       # 1. Generate a UUID for the file
        file_uuid = str(uuid.uuid4())

        # 2. The original file path
        file_path = "/FOLDER_PATH/test.pdf"

        # 3. Encode the file path in Base64
        encoded_path = base64.b64encode(file_path.encode()).decode()

        # 4. Combine UUID and Base64-encoded file path into the final format
        final_file_path = f"file:/{file_uuid}@_@{encoded_path}"

        # Output the final file path
        print(f"Final File Path: {final_file_path}")
        

    action_type = input("Dropbox Sign Action Type > ")

    if action_type.lower() == "a":  
        account_endpoints()
    elif action_type == "b" or action_type == "B":
        api_app_endpoints()
    elif action_type == "c" or action_type == "C":
        bulk_send_endpoints()
    elif action_type == "d" or action_type == "D":
        embedded_endpoints()
    elif action_type == "E" or action_type == "e" or action_type == "Exit" or action_type == "exit":
        print(dedent("""
            You have exit the Dropbox Sign Console App.
            """))
        exit(1)
    elif action_type == "F" or action_type == "f":
        oauth_endpoints()
    elif action_type == "g" or action_type == "G":
        report_endpoints()
    elif action_type == "h" or action_type == "H":
        signature_request_endpoints()
    elif action_type == "i" or action_type == "I":
        team_endpoints()
    elif action_type == "j" or action_type == "J":
        template_endpoints()
    elif action_type == "k" or action_type == "K":
        unclaimed_draft_endpoints()
    elif action_type == "l" or action_type == "L":
        test()
    else:
        print(dedent("""
            Please enter a correct action by submitting the letter corresponding to the action.
            """))

