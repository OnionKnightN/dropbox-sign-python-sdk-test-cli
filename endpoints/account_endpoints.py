from config import api_key,client_id,template_id
from textwrap import dedent
from pprint import pprint
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
######################## Account Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def create_my_account():

    with ApiClient(configuration) as api_client:
        api = apis.AccountApi(api_client)

        data = models.AccountCreateRequest(
            email_address="YOUR_EMAIL_ADDRESS_HERE",
        )

        try:
            response = api.account_create(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)


def get_my_account():

    with ApiClient(configuration) as api_client:
        api = apis.AccountApi(api_client)

        try:
            response = api.account_get()
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def update_my_account():

    with ApiClient(configuration) as api_client:
        api = apis.AccountApi(api_client)

        data = models.AccountUpdateRequest(
            callback_url="https://www.example.com/callback",
        )

        try:
            response = api.account_update(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def verify_my_account():

    with ApiClient(configuration) as api_client:
        api = apis.AccountApi(api_client)

        data = models.AccountVerifyRequest(
            email_address="YOUR_EMAIL_ADDRESS_HERE",
        )

        try:
            response = api.account_verify(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)


##############################################################################
######################## Account Endpoints End ###############################
##############################################################################

def account_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***************************     Account Endpoints     ***************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Create Account
        B. Get My Account
        C. Update My Account
        D. Verify My Account
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Endpoint > ")

        if endpoint == "A" or endpoint == "a":
            create_my_account()
        elif endpoint == "B" or endpoint == "b":
            get_my_account()
        elif endpoint == "C" or endpoint == "c":
            update_my_account()
        elif endpoint == "D" or endpoint == "d":
            verify_my_account()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))