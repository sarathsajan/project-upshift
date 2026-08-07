# get last traded price quotes for specified instruments
# https://upstox.com/developer/api-documentation/ltp-v3
# https://github.com/upstox/upstox-python/blob/master/examples/market-quote/code/ltp-quotes-v3.md

import read_creds
import upstox_client
from upstox_client.rest import ApiException

INSTRUMENT_KEY  = "NSE_EQ|INE848E01016"

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN

api_instance = upstox_client.MarketQuoteV3Api(upstox_client.ApiClient(configuration))

try:
    api_response = api_instance.get_ltp(instrument_key=INSTRUMENT_KEY)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling MarketQuoteV3Api->get_ltp: {e}\n")