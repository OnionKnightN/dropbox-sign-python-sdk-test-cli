from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
####################### BulkSend Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)


def get_bulk_send_job():

    with ApiClient(configuration) as api_client:
        api = apis.BulkSendJobApi(api_client)

        bulk_send_job_id = "YOUR_BULK_SEND_JOB_ID"

        try:
            response = api.bulk_send_job_get(bulk_send_job_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def list_bulk_send_job():

    with ApiClient(configuration) as api_client:
        api = apis.BulkSendJobApi(api_client)

        page = 1
        page_size = 20

        try:
            response = api.bulk_send_job_list(
                page=page,
                page_size=page_size,
            )
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)


##############################################################################
#######################  BulkSend Endpoints End ##############################
##############################################################################

def bulk_send_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***************************    Bulk Send Endpoints    ***************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Get Bulk Send Job
        B. List Bulk Send Job
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            get_bulk_send_job()
        elif endpoint == "B" or endpoint == "b":
            list_bulk_send_job()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))