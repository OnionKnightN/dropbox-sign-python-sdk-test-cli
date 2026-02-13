from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
######################## API APP Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)


def create_api_app():

    with ApiClient(configuration) as api_client:
        api = apis.ApiAppApi(api_client)

        oauth = models.SubOAuth(
            callback_url="https://example.com/oauth",
            scopes=["basic_account_info","request_signature"],
        )

        white_labeling_options = models.SubWhiteLabelingOptions(
            primary_button_color="#00b3e6",
            primary_button_text_color="#ffffff",
        )

        custom_logo_file = open('./docs/dropbox_sign_logo.jpeg', 'rb')

        data = models.ApiAppCreateRequest(
            name="My Production App OpenAPI 3",
            domains=["example.com"],
            oauth=oauth,
            white_labeling_options=white_labeling_options,
            custom_logo_file=custom_logo_file,
        )

        try:
            response = api.api_app_create(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def delete_api_app():

    with ApiClient(configuration) as api_client:
        api = apis.ApiAppApi(api_client)

        client_id = "YOUR_CLIENT_ID_HERE"

        try:
            response = api.api_app_delete(client_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def get_api_app():

    with ApiClient(configuration) as api_client:
        api = apis.ApiAppApi(api_client)

        client_id = "YOUR_CLIENT_ID_HERE"

        try:
            response = api.api_app_get(client_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def list_api_app():

    with ApiClient(configuration) as api_client:
        api = apis.ApiAppApi(api_client)

        page = 1
        page_size = 2

        try:
            response = api.api_app_list(
                page=page,
                page_size=page_size,
            )
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def update_api_app():

    with ApiClient(configuration) as api_client:
        api = apis.ApiAppApi(api_client)

        white_labeling_options = models.SubWhiteLabelingOptions(
            primary_button_color="#00b3e6",
            primary_button_text_color="#ffffff",
        )

       
        custom_logo_file = open('./docs/hellosign_logo.png', 'rb')

        data = models.ApiAppUpdateRequest(
            domains = ["python.com","testing.com"]
        )

        client_id = "YOUR_CLIENT_ID_HERE"

        try:
            response = api.api_app_update(client_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

##############################################################################
######################## API APP Endpoints End ###############################
##############################################################################

def api_app_endpoints():
    
    while True:

        print(dedent("""
        *********************************************************************************
        ***************************     API App Endpoints     ***************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Create API App
        B. Delete API App
        C. Get API App
        D. List API App
        E. Exit
        F. Update API App

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            create_api_app()
        elif endpoint == "B" or endpoint == "b":
            delete_api_app()
        elif endpoint == "C" or endpoint == "c":
            get_api_app()
        elif endpoint == "D" or endpoint == "d":
            list_api_app()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        elif endpoint == "F" or endpoint == "f":
            update_api_app()
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))
