# get the current positions for the user
# https://upstox.com/developer/api-documentation/get-positions
# https://github.com/upstox/upstox-python/blob/master/examples/portfolio/code/get-positions.md

import math
import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

try:
    api_response_holdings = api_instance.get_holdings(api_version)
    all_holdings = api_response_holdings.data    # list of objects of type upstox_client.models.holdings_data.HoldingsData   # type: ignore
        
    api_response_positions = api_instance.get_positions(api_version)
    all_positions = api_response_positions.data   # list of objects of type upstox_client.models.position_data.PositionData   # type: ignore

    for holding in all_holdings:
        for position in all_positions:
            if holding.isin == position.instrument_token[7:]:
                print("company name : ", holding.company_name)
                print("isin: ", holding.isin)
                print("holdings avg : ", holding.average_price)
                print("position active : ", position.buy_price)
                # print("total(holdings + positions) avg : ", math.floor((holding.average_price + (position.buy_price))/2))
                print("total(holdings + positions) avg : ", (holding.average_price + (position.buy_price))/2)
        print()

except ApiException as e:
    print(f"Exception when calling ChargeApi->get_brokerage: {e}\n" )
