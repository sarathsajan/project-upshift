# place an order to the exchange.
# https://upstox.com/developer/api-documentation/v3/place-order
# https://github.com/upstox/upstox-python/blob/master/examples/orders/code/place-order-v3.md

import read_creds
import upstox_client
from upstox_client.rest import ApiException

INSTRUMENT_TOKEN = "NSE_EQ|INE002A01018"

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN

api_instance = upstox_client.OrderApiV3(upstox_client.ApiClient(configuration))
body = upstox_client.PlaceOrderV3Request(
    quantity=1, 
    product="D", 
    validity="DAY", 
    price=1329.00, 
    instrument_token=INSTRUMENT_TOKEN, 
    order_type="LIMIT", 
    transaction_type="BUY", 
    disclosed_quantity=0, 
    trigger_price=0.0, 
    is_amo=False
)

try:
    api_response = api_instance.place_order(body)
    print(api_response)
except ApiException as e:
    print(f"Exception when calling OrderApiV3->place_order: {e}\n")