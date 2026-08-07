import re
import json
import pprint

SEARCH_NAME = "RELIANCE INDUSTRIES"
SEARCH_SEGMENT = "EQ" # EQ stands for equity segment for both NSE_EQ and BSE_EQ

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

pprint.pprint(results)
print(len(results))