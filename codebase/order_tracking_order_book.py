import pprint
from user_authentication import get_authenticated_client


def fetch_order_book():
    client = get_authenticated_client()
    pprint.pprint(client.order_book())


if __name__ == '__main__':
    fetch_order_book()