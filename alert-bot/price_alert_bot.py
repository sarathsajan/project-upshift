import datetime as dt
import zoneinfo
import read_creds
import upstox_client
from upstox_client.rest import ApiException
import telegram_bot

box_width = 26
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

api_response_user_profile = user_api_instance.get_profile(api_version)
api_response_portfolio_holdings = portfolio_api_instance.get_holdings(api_version)
api_response_portfolio_positions = portfolio_api_instance.get_positions(api_version)

current_holdings = api_response_portfolio_holdings.data     # list of objects of type upstox_client.models.holdings_data.HoldingsData   # type: ignore
current_positions = api_response_portfolio_positions.data   # list of objects of type upstox_client.models.position_data.PositionData   # type: ignore
generate_log(f"User Name\t\t:\t{api_response_user_profile.data.user_name}") # type: ignore
generate_log(f"User Email\t\t:\t{api_response_user_profile.data.email}")    # type: ignore
generate_log(f"User ID\t\t\t:\t{api_response_user_profile.data.user_id}")   # type: ignore
telegram_bot.send_telegram_message(f"Last Heartbeat : {datetime_now_ist_tz} IST")

# STEP 2
# FOR EACH holding in holdings
#   IF last traded price <= average price + open positions
#       send BUY notification/order
for holding in current_holdings:
    gross_profit_price = round(holding.average_price * 1.11, 2)
    generate_log(f"\n+{'-'*box_width}+")
    generate_log(f"| Company Name\t\t:\t{holding.company_name}")
    generate_log(f"| ISIN\t\t\t:\t{holding.isin}")
    generate_log(f"| Instrument Key\t:\t{holding.instrument_token}")
    generate_log(f"| Quantity\t\t:\t{holding.quantity}")
    generate_log(f"| Average Price\t\t:\t{holding.average_price}")
    generate_log(f"| Last Traded Price\t:\t{holding.last_price}")
    generate_log(f"| Gross Profit Price\t:\t{gross_profit_price}")
    if holding.last_price >= gross_profit_price:
        generate_log("|")
        generate_log("| SELL")
        generate_log(f"+{'-'*box_width}+")
        telegram_bot.send_telegram_message(f"SELL : {holding.company_name}\nLTP : Rs.{holding.last_price}\nGPP : Rs.{gross_profit_price}")
    elif holding.last_price <= holding.average_price:
        generate_log("|")
        generate_log("| BUY")
        generate_log(f"+{'-'*box_width}+")
        for position in current_positions:
            if holding.isin == position.instrument_token[7:]:
                generate_log("| POSITION ACTIVE")
                generate_log(f"+{'-'*box_width}+")
                break
        else:
            telegram_bot.send_telegram_message(f"BUY : {holding.company_name}\nLTP : Rs.{holding.last_price}\nAVG : Rs.{holding.average_price}")
    else:
        generate_log("|")
        generate_log("| HOLD")
        generate_log(f"+{'-'*box_width}+")

# write final_log to a text file
with open(f"log_{datetime_now_ist_tz.strftime('%Y%m%d_%H0000')}.log", "w", encoding="utf-8") as log_file:
    for log_item in final_log:
        log_file.write(f"{log_item}\n")
