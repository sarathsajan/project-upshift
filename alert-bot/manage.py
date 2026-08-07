# GET list of instruments to trade
# GET list of portfolio holdings
# FOR EACH instrument in instruments
#   IF instrument not in holdings
#       send BUY notification
#   IF instrument in holdings AND IF market price <= average price
#       send BUY notification
# FOR EACH holding in holdings
#   IF market price >= average price * 1.11
#       send SELL notification