import pprint
from user_authentication import get_authenticated_client


def fetch_holdings():
    client = get_authenticated_client()
    holdings_list = client.holdings()
    if not holdings_list:
        print("No stock holdings found.")
    else:
        print(f"Number of stocks in hand : {len(holdings_list)}")
        print("Items in the list : ")
        for item in holdings_list:
            pprint.pprint(item, indent=4)
            print(client.)


if __name__ == '__main__':
    fetch_holdings()