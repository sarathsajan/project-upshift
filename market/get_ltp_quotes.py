# get last traded price quotes for specified instruments
# https://upstox.com/developer/api-documentation/ltp-v3
# https://github.com/upstox/upstox-python/blob/master/examples/market-quote/code/ltp-quotes-v3.md

import os
import subprocess
import read_creds
import upstox_client
from upstox_client.rest import ApiException

INSTRUMENT_KEY  = "NSE_EQ|INE669E01016"

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN

api_instance = upstox_client.MarketQuoteV3Api(upstox_client.ApiClient(configuration))


if os.name == 'nt':
    subprocess.run('cls', shell=True, check=False)      # Windows
else:
    subprocess.run('clear', shell=True, check=False)    # POSIX (Linux, macOS)

try:
    api_response = api_instance.get_ltp(instrument_key=INSTRUMENT_KEY)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling MarketQuoteV3Api->get_ltp: {e}\n")