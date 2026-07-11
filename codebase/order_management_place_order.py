import pprint
from user_authentication import get_authenticated_client


def sell_op():
    client = get_authenticated_client()
    holdings_list = client.holdings()
    if not holdings_list:
        print("No stock holdings found.")
    else:
        stock_to_sell = holdings_list[0]
        print(stock_to_sell)
        order_status = client.place_order(
            OrderType='S',
            Exchange=stock_to_sell['Exch'],
            ExchangeType=stock_to_sell['ExchType'],
            ScripCode='13966',
            Qty=stock_to_sell['DPQty'],
            Price=int(stock_to_sell['AvgRate'])*1.05,
            IsIntraday=False,
        )
        print(order_status)


if __name__ == '__main__':
    sell_op()