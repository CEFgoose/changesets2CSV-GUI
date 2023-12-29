import keyring
import requests
API_PATH = "api/v2/users/find"
BASE_URL= "https://maproulette.org/"


def get_single_user_id_from_api():
    key=keyring.get_password("maproulette",'')
    if key != None and key != '':
        response = requests.get(
            BASE_URL + API_PATH,
            headers={"apikey": key},
            params={"username": "VLD170"},
            # verify=VERIFY_CERT,
        )
        if response.json():
            return response.json()[0]["id"]
