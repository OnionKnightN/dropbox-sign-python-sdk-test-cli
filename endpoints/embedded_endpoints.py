from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models


##############################################################################
####################### Embedded Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)


def get_edit_url():

    with ApiClient(configuration) as api_client:
        api = apis.EmbeddedApi(api_client)

        data = models.EmbeddedEditUrlRequest(
            cc_roles=['CC1', 'CC2', 'CC4'],
            merge_fields=[],
        )

        template_id = "YOUR_TEMPLATE_ID"

        try:
            response = api.embedded_edit_url(template_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def get_sign_url():

    with ApiClient(configuration) as api_client:
        api = apis.EmbeddedApi(api_client)

        signature_id = "YOUR_SIGNATURE_ID"

        try:
            response = api.embedded_sign_url(signature_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

##############################################################################
####################### Embedded Endpoints End ###############################
##############################################################################

def embedded_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***************************    Embedded  Endpoints    ***************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Get Edit URL
        B. Get Sign URL
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            get_edit_url()
        elif endpoint == "B" or endpoint == "b":
            get_sign_url()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))