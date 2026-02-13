from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
###################### Requesting Endpoints Start ############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def create_unclaimed_draft():
    
    with ApiClient(configuration) as api_client:
        api = apis.UnclaimedDraftApi(api_client)

        signer_1 = models.SubUnclaimedDraftSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack",
            order=0,
        )

        signer_2 = models.SubUnclaimedDraftSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Alice",
            order=1,
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=False,
            default_type="draw",
        )

        field_options = models.SubFieldOptions(
            date_format="DD - MM - YYYY",
        )

        data = models.UnclaimedDraftCreateRequest(
            subject="The NDA we talked about",
            type="request_signature",
            message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
            signers=[signer_1, signer_2],
            cc_email_addresses=[
                "CC_EMAIL_ADDRESS",
                "CC_EMAIL_ADDRESS",
            ],
            file_url=["YOUR_FILE_URL"],
            metadata={
                "custom_id": 1234,
                "custom_text": "NDA #9",
            },
            signing_options=signing_options,
            field_options=field_options,
            test_mode=True,
        )

        try:
            response = api.unclaimed_draft_create(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def create_embedded_unclaimed_draft():
    
    with ApiClient(configuration) as api_client:
        api = apis.UnclaimedDraftApi(api_client)

        signer_1 = models.SubUnclaimedDraftSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack",
        )

        data = models.UnclaimedDraftCreateEmbeddedRequest(
            client_id=client_id,
            file_url=["YOUR_FILE_URL"],
            requester_email_address="YOUR_REQUESTER_EMAIL_ADDRESS",
            signers=[signer_1],
            subject="[Test] NDA with Dropbox Sign]",
            title="[Test]",
            test_mode=True,
        )

        try:
            response = api.unclaimed_draft_create_embedded(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def create_embedded_unclaimed_draft_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.UnclaimedDraftApi(api_client)

        signer_1 = models.SubUnclaimedDraftTemplateSigner(
            role="ExampleRole",
            name="George",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
        )

        cc_1 = models.SubCC(
            role="ExampleCCRole",
            email_address="YOUR_CC_EMAIL_ADDRESS",
        )

        data = models.UnclaimedDraftCreateEmbeddedWithTemplateRequest(
            client_id=client_id,
            template_ids=["YOUR_TEMPLATE_ID"],
            requester_email_address="YOUR_REQUESTER_EMAIL_ADDRESS",
            signers=[signer_1],
            ccs=[cc_1],
            test_mode=True,
        )

        try:
            response = api.unclaimed_draft_create_embedded_with_template(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def edit_resend_unclaimed_draft():
    
    with ApiClient(configuration) as api_client:
        api = apis.UnclaimedDraftApi(api_client)

        data = models.UnclaimedDraftEditAndResendRequest(
            client_id=client_id,
            test_mode=True,
        )

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.unclaimed_draft_edit_and_resend(signature_request_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
##############################################################################
#################### Requesting Endpoints End ################################
##############################################################################

def unclaimed_draft_endpoints():

    while True:

        print(dedent("""
        *********************************************************************************
        ***********************     Unclaimed Draft Endpoints     ***********************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Create Unclaimed Draft
        B. Create Embedded Unclaimed Draft
        C. Create Embedded Unclaimed Draft with Template
        D. Edit and resend unclaimed Draft
        E. Exit

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            create_unclaimed_draft()
        elif endpoint == "B" or endpoint == "b":
            create_embedded_unclaimed_draft()
        elif endpoint == "C" or endpoint == "c":
            create_embedded_unclaimed_draft_template()
        elif endpoint == "D" or endpoint == "d":
            edit_resend_unclaimed_draft()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))