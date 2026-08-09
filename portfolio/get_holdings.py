# get the long term holdings of the user
# https://upstox.com/developer/api-documentation/get-holdings

import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

try:
    api_response = api_instance.get_holdings(api_version)
    all_holdings = api_response.data    # list of objects of type upstox_client.models.holdings_data.HoldingsData # type: ignore
    
    for holding in all_holdings:
        print(holding)
        print()

except ApiException as e:
    print(f"Exception when calling ChargeApi->get_brokerage: {e}\n" )