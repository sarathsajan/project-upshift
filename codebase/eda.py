from login import get_authenticated_client

def print_holdings_summary(holdings_list: list[dict]) -> None:
    """Print a readable summary of the holdings returned by the broker API."""
    print(f"Number of stocks in hand : {len(holdings_list)}")

    if not holdings_list:
        print("No stock holdings found.")
        return

    print("first item in the list : ", holdings_list[2])

    for stock_kv in holdings_list:
        continue
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



client = get_authenticated_client()
holdings_list = client.holdings()
print_holdings_summary(holdings_list)
positions_list = client.positions()
print(positions_list)