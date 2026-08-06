# Get user profile information using access token
# https://upstox.com/developer/api-documentation/get-profile

import json
import upstox_client
from upstox_client.rest import ApiException


with open('env.json', 'r', encoding='utf-8') as file:
    env_data = json.load(file)
UPSTOX_ACCESS_TOKEN = env_data.get('UPSTOX_ACCESS_TOKEN')

configuration = upstox_client.Configuration()
configuration.access_token = UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))

try:
    # Get User Fund And Margin
    api_response = api_instance.get_profile(api_version)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling UserApi->get_user_fund_margin:{e}\n")