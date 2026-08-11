import os
import subprocess
import datetime as dt
import zoneinfo
import read_creds
import upstox_client
from upstox_client.rest import ApiException
import telegram_bot

box_width = 12
final_log = []
datetime_now_ist_tz = dt.datetime.now(zoneinfo.ZoneInfo("Asia/Kolkata")).replace(microsecond=0)

configuration = upstox_client.Configuration()
configuration.access_token = read_creds.UPSTOX_ACCESS_TOKEN
api_version = '2.0'
user_api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))
portfolio_api_instance = upstox_client.PortfolioApi(upstox_client.ApiClient(configuration))

def generate_log(log_string):
    print(log_string)
    final_log.append(log_string)
    
# STEP 1
# GET list of instruments to trade from the holdings
generate_log(f"Timestamp (IST)\t\t:\t{datetime_now_ist_tz}")
portfolio_api_response = portfolio_api_instance.get_holdings(api_version)
user_api_response = user_api_instance.get_profile(api_version)
current_holdings = portfolio_api_response.data    # list of objects of type upstox_client.models.holdings_data.HoldingsData # type: ignore
generate_log(f"User Name\t\t:\t{user_api_response.data.user_name}")
generate_log(f"User Email\t\t:\t{user_api_response.data.email}")
generate_log(f"User ID\t\t\t:\t{user_api_response.data.user_id}")
telegram_bot.send_telegram_message(f"Timestamp (IST)\t\t:\t{datetime_now_ist_tz}")

# STEP 2
# FOR EACH instrument in holdings
#   IF last traded price <= average price + open positions
#       send BUY notification/order
for instrument in current_holdings:
    gross_profit_price = round(instrument.average_price * 1.11, 2)
    generate_log(f"\n+{'-'*box_width}+")
    generate_log(f"| Company Name\t\t:\t{instrument.company_name}")
    generate_log(f"| ISIN\t\t\t:\t{instrument.isin}")
    generate_log(f"| Instrument Key\t:\t{instrument.instrument_token}")
    generate_log(f"| Quantity\t\t:\t{instrument.quantity}")
    generate_log(f"| Average Price\t\t:\t{instrument.average_price}")
    generate_log(f"| Last Traded Price\t:\t{instrument.last_price}")
    generate_log(f"| Gross Profit Price\t:\t{gross_profit_price}")
    if instrument.last_price >= gross_profit_price:
        generate_log(f"|")
        generate_log(f"| SELL")
        generate_log(f"+{'-'*box_width}+")
        telegram_bot.send_telegram_message(f"SELL : {instrument.company_name}\nLTP  : Rs.{instrument.last_price}\nGPP  : Rs.{gross_profit_price}")
    elif instrument.last_price <= instrument.average_price:
        generate_log(f"|")
        generate_log(f"| BUY")
        generate_log(f"+{'-'*box_width}+")
        telegram_bot.send_telegram_message(f"BUY  : {instrument.company_name}\nLTP  : Rs.{instrument.last_price}\nAVG  : Rs.{instrument.average_price}")
    else:
        generate_log(f"|")
        generate_log(f"| HOLD")
        generate_log(f"+{'-'*box_width}+")

# write final_log to a text file
with open(f"log_{datetime_now_ist_tz.strftime('%Y%m%d_%H0000')}.log", "w", encoding="utf-8") as log_file:
    for log_item in final_log:
        log_file.write(f"{log_item}\n")
