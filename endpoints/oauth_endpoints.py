from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models


##############################################################################
####################### OAuth API Endpoints Start ############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def generate_oauth_token():

    with ApiClient(configuration) as api_client:
        api = apis.OAuthApi(api_client)

        data = models.OAuthTokenGenerateRequest(
            state="YOUR_CUSTOM_STATE",
            code="YOUR_AUTHORIZATION_CODE",
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )

        try:
            response = api.oauth_token_generate(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def refreash_oauth_token():

    with ApiClient(configuration) as api_client:
        api = apis.OAuthApi(api_client)

        data = models.OAuthTokenRefreshRequest(
            refresh_token="YOUR_REFRESH_TOKEN",
        )

        try:
            response = api.oauth_token_refresh(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)


##############################################################################
###################### OAuth API Endpoints End ###############################
##############################################################################

def oauth_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***************************   OAuth API Endpoints     ***************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Generate OAuth Token
        B. Refreash OAuth Token
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            generate_oauth_token()
        elif endpoint == "B" or endpoint == "b":
            refreash_oauth_token()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))
