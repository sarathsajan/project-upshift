# Get user profile information using access token
# https://upstox.com/developer/api-documentation/get-profile
# https://github.com/upstox/upstox-python/blob/master/examples/user/code/get-profile.md

import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

try:
    # Get User Fund And Margin
    api_response = api_instance.get_profile(api_version)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling UserApi->get_user_fund_margin:{e}\n")