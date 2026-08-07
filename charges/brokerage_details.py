import read_creds
import upstox_client
from upstox_client.rest import ApiException

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'

api_instance = upstox_client.ChargeApi(upstox_client.ApiClient(configuration))
instrument_token = 'NSE_EQ|INE669E01016'
quantity = 10
product = 'D'
transaction_type = 'BUY'
price = 13.4 

try:
    # Brokerage details
    api_response = api_instance.get_brokerage(instrument_token, quantity, product, transaction_type, price, api_version)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling ChargeApi->get_brokerage: {e}\n")