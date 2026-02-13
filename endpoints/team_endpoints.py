from pprint import pprint
from config import api_key,client_id,template_id
from textwrap import dedent
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models

##############################################################################
######################### Team Endpoints Start ###############################
##############################################################################

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=api_key,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

def add_team_member():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        data = models.TeamAddMemberRequest(
            email_address="YOUR_TEAMMATE_EMAIL_ADDRESS",
        )

        try:
            response = api.team_add_member(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def create_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        data = models.TeamCreateRequest(
            name="New Team Name",
        )

        try:
            response = api.team_create(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def get_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        try:
            response = api.team_get()
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def list_sub_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        team_id = "YOUR_TEAM_ID"

        try:
            response = api.team_sub_teams(team_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def info_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        try:
            response = api.team_info()
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def update_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        data = models.TeamUpdateRequest(
            name="New Team Name",
        )

        try:
            response = api.team_update(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def delete_team():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        try:
            response = api.team_delete()
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def list_team_members():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        team_id = "YOUR_TEAM_ID"

        try:
            response = api.team_members(team_id)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
def remove_team_member():
    
    with ApiClient(configuration) as api_client:
        api = apis.TeamApi(api_client)

        data = models.TeamRemoveMemberRequest(
            email_address="YOUR_TEAMMATE_EMAIL_ADDRESS",
            new_owner_email_address="NEW_TEAMMATE_EMAIL_ADDRESS",
        )

        try:
            response = api.team_remove_member(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)
    
##############################################################################
####################### Team Endpoints End ###################################
##############################################################################

def team_endpoints():
    
    while True:

        print(dedent("""
        *********************************************************************************
        *****************************     Team Endpoints     ****************************
        *********************************************************************************

        Enter the letter corresponding to the action type. 

        A. Add Team Member
        B. Create Team
        C. Get Team 
        D. List Sub Team Info
        E. Exit
        F. Team Info
        G. Update Team
        H. Delete Team
        I. List Team Members
        J. Remove Team Member

        *********************************************************************************
        """))

        endpoint = input("Dropbox Sign Action > ")

        if endpoint == "A" or endpoint == "a":
            add_team_member()
        elif endpoint == "B" or endpoint == "b":
            create_team()
        elif endpoint == "C" or endpoint == "c":
            get_team()
        elif endpoint == "D" or endpoint == "d":
            list_sub_team()
        elif endpoint == "E" or endpoint == "e" or endpoint == "Exit" or endpoint == "exit":
            print(dedent("""
                You have exit the Dropbox Sign Console App.
                """))
            exit(1)
        elif endpoint == "F" or endpoint == "f":
            info_team()
        elif endpoint == "G" or endpoint == "g":
            update_team()
        elif endpoint == "H" or endpoint == "h":
            delete_team()
        elif endpoint == "I" or endpoint == "i":
            list_team_members()
        elif endpoint == "J" or endpoint == "j":
            remove_team_member()
        else:
            print(dedent("""
                Please enter a correct action by submitting the letter corresponding to the action.
                """))