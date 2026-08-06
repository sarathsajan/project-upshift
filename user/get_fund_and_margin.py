# get fund and margin of the user
# https://upstox.com/developer/api-documentation/get-funds-and-margin-v3
# https://github.com/upstox/upstox-python/blob/master/examples/user/code/get-fund-and-margin-v3.md

import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN

api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

try:
    # Get User Fund And Margin V3
    api_response = api_instance.get_user_fund_margin_v3()
    print(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_fund_margin_v3: %s\n" % e)