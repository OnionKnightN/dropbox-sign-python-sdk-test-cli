from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
import shutil
import os 
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
####################### Template Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def add_template_user():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        data = models.TemplateAddUserRequest(
            email_address="YOUR_EMAIL_ADDRESS",
        )

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_add_user(template_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def remove_template_user():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        data = models.TemplateRemoveUserRequest(
            email_address="YOUR_EMAIL_ADDRESS",
        )

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_remove_user(template_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def create_embedded_template_draft():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        role_1 = models.SubTemplateRole(
            name="Client",
            order=0,
        )

        role_2 = models.SubTemplateRole(
            name="Witness",
            order=1,
        )

        merge_field_1 = models.SubMergeField(
            name="Full Name",
            type="text",
        )

        merge_field_2 = models.SubMergeField(
            name="Is Registered?",
            type="checkbox",
        )

        field_options = models.SubFieldOptions(
            date_format="DD - MM - YYYY",
        )

        data = models.TemplateCreateEmbeddedDraftRequest(
            client_id=client_id,
            file_url=["YOUR_FILE_URL"],
            title="Test Template",
            subject="Please sign this document",
            message="For your approval",
            signer_roles=[role_1, role_2],
            cc_roles=["Manager","Customer"],
            merge_fields=[merge_field_1, merge_field_2],
            field_options=field_options,
            test_mode=True,
        )

        try:
            response = api.template_create_embedded_draft(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def delete_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_delete(template_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def get_template_files():
    
    # Get Template Files Endpoint 
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_files(template_id)
            pprint(response)
            os.popen("cp " + response.name + " " + "/FOLDER_PATH/Dropbox Sign Testing (1 page).pdf") 
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

    # Get Template Files as Data Uri Endpoint 
    """with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_files_as_data_uri(template_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)"""

    # Get Get Template Files as File Url Endpoint 
    """with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_files_as_file_url(template_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)"""

    
def update_template_files():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        data = models.TemplateUpdateFilesRequest(
            file_url=["YOUR_FILE_URL"],
        )

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_update_files(template_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def get_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.template_get(template_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def list_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.TemplateApi(api_client)

        account_id = "YOUR_ACCOUNT_ID"

        try:
            response = api.template_list(
                account_id=account_id,
            )
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    

##############################################################################
##################### Template Endpoints End #################################
##############################################################################

def template_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***************************     Template Endpoints     **************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Add Template User
        B. Remove Template User
        C. Create Emebedded Template Draft
        D. Delete Template
        E. Exit
        F. Get Template Files
        G. Update Template Files
        H. Get Template info
        I. List Template

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            add_template_user()
        elif endpoint == "B" or endpoint == "b":
            remove_template_user()
        elif endpoint == "C" or endpoint == "c":
            create_embedded_template_draft()
        elif endpoint == "D" or endpoint == "d":
            delete_template()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        elif endpoint == "F" or endpoint == "f":
            get_template_files()
        elif endpoint == "G" or endpoint == "g":
            update_template_files()
        elif endpoint == "H" or endpoint == "h":
            get_template()
        elif endpoint == "I" or endpoint == "i":
            list_template()
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))