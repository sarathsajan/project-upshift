# get the current positions for the user
# https://upstox.com/developer/api-documentation/get-positions
# https://github.com/upstox/upstox-python/blob/master/examples/portfolio/code/get-positions.md

import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

try:
    api_response = api_instance.get_positions(api_version)
    all_positions = api_response.data   # list of objects of type upstox_client.models.position_data.PositionData   # type: ignore

    for position in all_positions:
        print(position)
        print()

except ApiException as e:
    print(f"Exception when calling ChargeApi->get_brokerage: {e}\n" )
