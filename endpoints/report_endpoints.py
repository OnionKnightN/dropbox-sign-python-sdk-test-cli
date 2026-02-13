from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
######################### Report Endpoints Start #############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def create_report():

    with ApiClient(configuration) as api_client:
        api = apis.ReportApi(api_client)

        data = models.ReportCreateRequest(
            start_date="09/01/2020",
            end_date="09/01/2020",
            report_type=["user_activity", "document_status"],
        )

        try:
            response = api.report_create(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)


##############################################################################
######################### Report Endpoints End ###############################
##############################################################################

def report_endpoints():

    while True:


        print(dedent("""
        *********************************************************************************
        ***************************     Report Endpoints     ****************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Create Report
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            create_report()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))