'''
5paisa API documentation : https://xstream.5paisa.com/

Access Token [POST] [JSON]
The API endpoint is designed to generate access token for a client with help
of Request Token obtained from OAuth Login.

To generate the access token, partner/client needs to provide AppKey in the
header of the payload whereas UserID and encryptionKey needs to be passed in
body. The successful API call will provide the partner an access token which
is valid throughout a day. Access token is used to call all further APIs.

payload head < AppKey
payload body < UserID, encryptionKey
api output   > Access token valid till midnight 23:59:59 (is it IST or UTC?)
'''

import requests

BASE_URL = "https://xstream.5paisa.com"
APP_KEY = ""
USER_ID = ""
ENCRYPTION_KEY = ""


def send_api_request(method, endpoint, *, headers=None, payload=None, params=None, timeout=30):
    """Generic boilerplate for sending JSON API requests."""
    url = f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"
    response = requests.request(
        method=method.upper(),
        url=url,
        headers=headers or {},
        json=payload,
        params=params,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json() if response.content else {}


def get_access_token(app_key, user_id, encryption_key):
    """Generate access token using the 5paisa API."""
    headers = {
        "key": app_key,
        "Content-Type": "application/json",
    }
    payload = {
        "UserID": user_id,
        "encryptionKey": encryption_key,
    }
    # Replace '/access-token' with the exact endpoint from the official docs if needed.
    return send_api_request("POST", "/access-token", headers=headers, payload=payload)


token_response = get_access_token(APP_KEY, USER_ID, ENCRYPTION_KEY)
print(token_response)