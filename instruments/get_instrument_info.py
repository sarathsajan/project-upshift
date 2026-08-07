# get a list of all instruments available at the beginning of the day.
# https://upstox.com/developer/api-documentation/instruments

import gzip
import json
import re
import shutil
from urllib.request import Request, urlopen

URL = "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"
GZ_PATH = "complete.json.gz"
JSON_PATH = "complete.json"
SEARCH_SEGMENT = "EQ"
SEARCH_NAME = "RELIANCE INDUSTRIES"


############### download and decompress scrips data ###############
request = Request(URL)
with urlopen(request) as response, open(GZ_PATH, "wb") as f:
    shutil.copyfileobj(response, f)

with gzip.open(GZ_PATH, "rb") as gz_file, open(JSON_PATH, "wb") as out_file:
    shutil.copyfileobj(gz_file, out_file)


############### search scrips data ###############
with open('complete.json') as f:
    COMPLETE_data = json.load(f)

# regex reference
# ^NSE_.* → starts with NSE_
# .*EQ$ → ends with EQ
# .*MARUTI.* → contains MARUTI

results = [
    item for item in COMPLETE_data
    if re.search(rf".*{SEARCH_NAME}.*", item.get("name", ""))
    and re.search(rf".*{SEARCH_SEGMENT}$", item.get("segment", ""))
]

for result_item in results:
    print(result_item)
print(f"\nfound {len(results)} results")