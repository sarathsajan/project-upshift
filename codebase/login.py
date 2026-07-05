from datetime import datetime

import pyotp
from py5paisa import FivePaisaClient

from env_vars import cred, client_code, pin, fivepaisa_totp_secret


def get_totp(secret: str) -> str:
    """Generate a TOTP code from the shared secret.

    The generated code is used as a second-factor login value for 5paisa.
    """
    totp = pyotp.TOTP(secret)
    code = totp.now()
    print(f"totp : {code} generated at {datetime.now().strftime('%H:%M:%S')}, valid for 30 seconds")
    return code


def print_holdings_summary(holdings_list: list[dict]) -> None:
    """Print a readable summary of the holdings returned by the broker API."""
    print("list of stocks in hand : ", len(holdings_list))

    if not holdings_list:
        print("No holdings found.")
        return

    print("first item in the list : ", holdings_list[0])

    for stock_kv in holdings_list:
        avg_rate = float(stock_kv["AvgRate"])
        current_price = float(stock_kv["CurrentPrice"])
        dp_qty = float(stock_kv["DPQty"])
        total_value = dp_qty * current_price

        print(f"FullName\t: {stock_kv['FullName']}")
        print(f"AvgRate\t\t: {avg_rate}")
        print(f"CurrentPrice\t: {current_price}")
        print(f"DPQty\t\t: {dp_qty}")
        print(f"Total stock worth in hand : INR {total_value}")

        if current_price >= avg_rate:
            profit = total_value - (dp_qty * avg_rate)
            print(f"SELL for profits of INR {profit}")
        else:
            print("BUY")

        print()


def main() -> None:
    """Authenticate with 5paisa and print the portfolio holdings summary."""
    client = FivePaisaClient(cred=cred)
    client.get_totp_session(client_code, get_totp(fivepaisa_totp_secret), pin)
    holdings_list = client.holdings()
    print_holdings_summary(holdings_list)


if __name__ == "__main__":
    main()