from pprint import pprint
import shutil
import os 
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models


##############################################################################
################### Signature Request Endpoints Start ########################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def embedded_bulk_with_template():

    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_list_1_signer = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            name="George",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            pin="d79a3td",
        )

        signer_list_1_custom_fields = models.SubBulkSignerListCustomField(
            name="company",
            value="ABC Corp",
        )

        signer_list_1 = models.SubBulkSignerList(
            signers=[signer_list_1_signer],
            custom_fields=[signer_list_1_custom_fields],
        )

        signer_list_2_signer = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            name="Mary",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            pin="gd9as5b",
        )

        signer_list_2_custom_fields = models.SubBulkSignerListCustomField(
            name="company",
            value="123 LLC",
        )

        signer_list_2 = models.SubBulkSignerList(
            signers=[signer_list_2_signer],
            custom_fields=[signer_list_2_custom_fields],
        )

        cc_1 = models.SubCC(
            role="ExampleCCRole",
            email_address="YOUR_CC_EMAIL_ADDRESS",
        )

        data = models.SignatureRequestBulkCreateEmbeddedWithTemplateRequest(
            client_id=client_id,
            template_ids=["YOUR_TEMPLATE_ID"],
            subject="OpenSDK embedded",
            message="Glad we could come to an agreement.",
            signer_list=[signer_list_1, signer_list_2],
            ccs=[cc_1],
            test_mode=True,
        )

        try:
            response = api.signature_request_bulk_create_embedded_with_template(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def bulk_with_template():

    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_list_1_signer = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            name="George",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            pin="d79a3td",
        )

        signer_list_1_custom_fields = models.SubBulkSignerListCustomField(
            name="company",
            value="ABC Corp",
        )

        signer_list_1 = models.SubBulkSignerList(
            signers=[signer_list_1_signer],
            custom_fields=[signer_list_1_custom_fields],
        )

        signer_list_2_signer = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            name="Mary",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            pin="gd9as5b",
        )

        signer_list_2_custom_fields = models.SubBulkSignerListCustomField(
            name="company",
            value="123 LLC",
        )

        signer_list_2 = models.SubBulkSignerList(
            signers=[signer_list_2_signer],
            custom_fields=[signer_list_2_custom_fields],
        )

        cc_1 = models.SubCC(
            role="ExampleCCRole",
            email_address="YOUR_CC_EMAIL_ADDRESS",
        )

        data = models.SignatureRequestBulkSendWithTemplateRequest(
            template_ids=["YOUR_TEMPLATE_ID"],
            subject="Purchase Order OpenSDK Non-embedded",
            message="Glad we could come to an agreement.",
            signer_list=[signer_list_1, signer_list_2],
            ccs=[cc_1],
            test_mode=True,
        )

        try:
            response = api.signature_request_bulk_send_with_template(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def cancel_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_cancel(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def create_embedded_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_1 = models.SubSignatureRequestSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack\u200b Doe"
        )

        signer_2 = models.SubSignatureRequestSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jill"
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=True,
            default_type="draw",
        )

        data = models.SignatureRequestCreateEmbeddedRequest(
            client_id=client_id,
            title="NDA with Acme Co.",
            subject="The NDA we talked about",
            message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
            signers=[signer_1, signer_2],
            cc_email_addresses=["YOUR_CC_EMAIL_ADDRESS", "YOUR_CC_EMAIL_ADDRESS"],
            file_url=["FILE_URL_1"],
            signing_options=signing_options,
            test_mode=True,
        )

        try:
            response = api.signature_request_create_embedded(data)
            
            # Extract the signatures array
            signatures = response['signature_request']['signatures']

            # Extract signature_id values
            signature_ids = [signature['signature_id'] for signature in signatures]

            # Print the signature_ids
            pprint(signature_ids[0])
            pprint(signature_ids[1])

        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def create_embedded_siganture_request_with_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_1 = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack",
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=True,
            default_type="draw",
        )

        data = models.SignatureRequestCreateEmbeddedWithTemplateRequest(
            client_id=client_id,
            template_ids=["YOUR_TEMPLATE_ID"],
            subject="Purchase Order",
            message="Glad we could come to an agreement.",
            signers=[signer_1],
            signing_options=signing_options,
            test_mode=True,
            populate_auto_fill_fields=True
        )

        try:
            response = api.signature_request_create_embedded_with_template(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

def download_siganture_request():


    # Download Files Endpoint 
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_files(signature_request_id)
            print(response.name)
            os.popen("cp " + response.name + " " + "/FOLDER_PATH/Dropbox Sign Testing (1 page).pdf") 

        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

    # Download Files as Data Uri
    """with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_files_as_data_uri(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)"""


    #Download Files as File Url
    """with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_files_as_file_url(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)"""


def get_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_get(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def list_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        account_id = None
        page = 1
        
        try:
            response = api.signature_request_list(
                account_id=account_id,
                page=page,
            )

            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e) 

def release_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_release_hold(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def send_reminder():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        data = models.SignatureRequestRemindRequest(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
        )

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_remind(signature_request_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def remove_siganture_access():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_remove(signature_request_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def send_siganture_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_1 = models.SubSignatureRequestSigner(
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack",
            order=0,
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=True,
            default_type="draw",
        )

        field_options = models.SubFieldOptions(
            date_format="DD - MM - YYYY",
        )

        first_name = models.SubCustomField(
            name="first_name",
            value="John"
        )

        is_registered = models.SubCustomField(
            name="is_registered",
            value="1"
        )

        form_fields_per_document_signature = models.SubFormFieldsPerDocumentSignature(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "signature1",
            type = "signature",
            x = 50,
            y = 70,
            width = 60,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )

        form_fields_per_document_intials = models.SubFormFieldsPerDocumentInitials(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "initials1",
            type = "initials",
            x = 50,
            y = 120,
            width = 60,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )

        form_fields_per_document_date_signed = models.SubFormFieldsPerDocumentDateSigned(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "date_signed1",
            type = "date_signed",
            x = 50,
            y = 170,
            width = 60,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )


        form_fields_per_document_text = models.SubFormFieldsPerDocumentText(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "text1",
            type = "text",
            x = 50,
            y = 220,
            width = 60,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )

        form_fields_per_document_text_merge = models.SubFormFieldsPerDocumentTextMerge(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "first_name",
            type = "text-merge",
            x = 50,
            y = 270,
            width = 60,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )


        form_fields_per_document_checkbox = models.SubFormFieldsPerDocumentCheckbox(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "checkbox1",
            type = "checkbox",
            x = 50,
            y = 320,
            width = 16,
            height = 16,
            required = True,
            signer = "0",
            page = 1
        )

       

        form_fields_per_document_checkbox_merge = models.SubFormFieldsPerDocumentCheckboxMerge(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "is_registered",
            type = "checkbox-merge",
            x = 50,
            y = 370,
            width = 16,
            height = 16,
            required = True,
            signer = "0",
            page = 1
        )


        form_fields_per_document_dropdown = models.SubFormFieldsPerDocumentDropdown(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "dropdown1",
            type = "dropdown",
            options = ["Option 1","Option 2"],
            content = "Option 2",
            x = 50,
            y = 420,
            width = 80,
            height = 30,
            required = True,
            signer = "0",
            page = 1
        )

        form_fields_per_document_hyperlink = models.SubFormFieldsPerDocumentHyperlink(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "hyperlink1",
            type = "hyperlink",
            content = "Click me!",
            content_url = "http://example.com",
            x = 50,
            y = 470,
            width = 60,
            height = 30,
            page = 1
        )

        form_fields_per_document_radio1 = models.SubFormFieldsPerDocumentRadio(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "radio1",
            type = "radio",
            x = 50,
            y = 500,
            width = 16,
            height = 16,
            group = "RadioItemGroup1",
            checked = "1",
            signer = "0",
            page = 1

        )

        form_fields_per_document_radio2 = models.SubFormFieldsPerDocumentRadio(
            document_index = 0,
            api_id = "YOUR_API_ID",
            name = "radio1",
            type = "radio",
            x = 100,
            y = 500,
            width = 16,
            height = 16,
            group = "RadioItemGroup1",
            checked = "0",
            signer = "0",
            page = 1
        )

        form_field_group_value = models.SubFormFieldGroup(
            group_id = "RadioItemGroup1",
            group_label = "Radio Item Group 1",
            requirement = "require_0-1"
        )


        document = open("/FOLDER_PATH/Dropbox Sign Testing (1 page).pdf", "rb")

        data = models.SignatureRequestSendRequest(
            title="NDA with Acme Co.",
            subject="The NDA we talked about final",
            message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
            signers=[signer_1],
            file= [document],
            form_field_groups = [form_field_group_value],
            metadata={
                "custom_id": 1234,
                "custom_text": "NDA #9",
            },  
            signing_options=signing_options,
            field_options=field_options,
            test_mode=True,
            custom_fields = [first_name,is_registered],
            form_fields_per_document= [
                form_fields_per_document_signature,
                form_fields_per_document_intials,
                form_fields_per_document_text,
                form_fields_per_document_text_merge,
                form_fields_per_document_checkbox,
                form_fields_per_document_checkbox_merge,
                form_fields_per_document_date_signed,
                form_fields_per_document_dropdown,
                form_fields_per_document_hyperlink,
                form_fields_per_document_radio1,
                form_fields_per_document_radio2
            ]

        )

        try:
            response = api.signature_request_send(data)
            document.close()
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
            document.close()

    
def send_siganture_request_with_template():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        signer_1 = models.SubSignatureRequestTemplateSigner(
            role="ExampleRole",
            email_address="YOUR_SIGNER_EMAIL_ADDRESS",
            name="Jack"
        )

        cc_1 = models.SubCC(
            role="ExampleCCRole",
            email_address="YOUR_CC_EMAIL_ADDRESS",
        )

        custom_field_1 = models.SubCustomField(
            name="company",
            value="$20,000",
            editor="ExampleRole",
            required=True
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=False,
            default_type="draw",
        )

        data = models.SignatureRequestSendWithTemplateRequest(
            template_ids=["YOUR_TEMPLATE_ID"],
            subject="Purchase Order",
            message="Glad we could come to an agreement.",
            signers=[signer_1],
            #ccs=[cc_1],
            #custom_fields=[custom_field_1],
            signing_options=signing_options,
            test_mode=True,
            client_id="YOUR_CLIENT_ID"
        )

        try:
            response = api.signature_request_send_with_template(data)
            pprint(response["signature_request"]["signature_request_id"])

            api = apis.SignatureRequestApi(api_client)
            signature_request_id = response["signature_request"]["signature_request_id"]
            response2 = api.signature_request_get(signature_request_id)
            pprint(response2)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def update_signature_request():
    
    with ApiClient(configuration) as api_client:
        api = apis.SignatureRequestApi(api_client)

        data = models.SignatureRequestUpdateRequest(
            email_address = "YOUR_SIGNER_EMAIL_ADDRESS",
            signature_id = "YOUR_SIGNATURE_ID",
            name = "Alice"
        )

        signature_request_id = "YOUR_SIGNATURE_REQUEST_ID"

        try:
            response = api.signature_request_update(signature_request_id, data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
##############################################################################
################# Signature Request Endpoints End ############################
##############################################################################

def signature_request_endpoints():

    while True:


        print(dedent("""
        *********************************************************************************
        **********************     Signature Request Endpoints     **********************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Embedded Bulk with Template
        B. Bulk with Template
        C. Cancel Signature Request
        D. Create Embedded Signature Request
        E. Exit
        F. Create Embedded Signature Request with Template
        G. Download Signature Request File
        H. Get Signature Request Info
        I. List Siganture Request
        J. Release Siganture Request
        K. Send Reminder Signature Request
        L. Remove Siganture Request Access 
        M. Send Signature Request 
        N. Send with Template
        O. Update Signature Request

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            embedded_bulk_with_template()
        elif endpoint == "B" or endpoint == "b":
            bulk_with_template()
        elif endpoint == "C" or endpoint == "c":
            cancel_siganture_request()
        elif endpoint == "D" or endpoint == "d":
            create_embedded_siganture_request()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        elif endpoint == "F" or endpoint == "f":
            create_embedded_siganture_request_with_template()
        elif endpoint == "G" or endpoint == "g":
            download_siganture_request()
        elif endpoint == "H" or endpoint == "h":
            get_siganture_request()
        elif endpoint == "I" or endpoint == "i":
            list_siganture_request()
        elif endpoint == "J" or endpoint == "j":
            release_siganture_request()
        elif endpoint == "K" or endpoint == "k":
            send_reminder()
        elif endpoint == "L" or endpoint == "l":
            remove_siganture_access()
        elif endpoint == "M" or endpoint == "m":
            send_siganture_request()
        elif endpoint == "N" or endpoint == "n":
            send_siganture_request_with_template()
        elif endpoint == "O" or endpoint == "o":
            update_signature_request()
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))