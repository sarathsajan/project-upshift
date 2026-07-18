# Get user IPs

import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = '{your_access_token}'

api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

try:
    # Get User IPs
    api_response = api_instance.get_user_ips()
    print(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_ips: %s\n" % e)