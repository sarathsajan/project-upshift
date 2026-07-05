from py5paisa import FivePaisaClient
from env_vars import cred, client_code, pin, fivepaisa_totp_secret
from datetime import datetime
import pyotp
import pprint

def get_totp(secret: str) -> str:
    """Generate a TOTP code from the given secret.

    Args:
        secret: The shared secret used to generate the one-time password.

    Returns:
        The current TOTP code as a string.
    """
    totp = pyotp.TOTP(secret)
    code = totp.now()
    print(f"totp : {code} generated at {datetime.now().strftime('%H:%M:%S')}, valid for 30 seconds")
    return code


Client = FivePaisaClient(cred=cred)
Client.get_totp_session(client_code, get_totp(fivepaisa_totp_secret), pin)

holdings_list = Client.holdings()
print("list of stocks in hand : ", len(holdings_list))
print("first item in the list : ", holdings_list[0])
for stock_kv in holdings_list:
    if float(stock_kv['AvgRate']) > float(stock_kv['CurrentPrice']):
        continue
        print(f"FullName\t: {stock_kv['FullName']}")
        print(f"AvgRate\t\t: {stock_kv['AvgRate']}")
        print(f"CurrentPrice\t: {stock_kv['CurrentPrice']}")
        print(f"DPQty\t\t: {stock_kv['DPQty']}")
        print(f"Total stock worth in hand : INR {float(stock_kv['DPQty']) * float(stock_kv['CurrentPrice'])}")
        print("BUY")
        print("\n")
    else:
        # continue
        print(f"FullName\t: {stock_kv['FullName']}")
        print(f"AvgRate\t\t: {stock_kv['AvgRate']}")
        print(f"CurrentPrice\t: {stock_kv['CurrentPrice']}")
        print(f"DPQty\t\t: {stock_kv['DPQty']}")
        print(f"Total stock worth in hand : INR {float(stock_kv['DPQty']) * float(stock_kv['CurrentPrice'])}")
        print(f"SELL for profits of INR {float(stock_kv['DPQty']) * float(stock_kv['CurrentPrice'])  - float(stock_kv['DPQty']) * float(stock_kv['AvgRate'])}")
        print("\n")