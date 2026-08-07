import gzip
import shutil
from urllib.request import Request, urlopen

url = "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"
gz_path = "complete.json.gz"
json_path = "complete.json"

request = Request(url)
with urlopen(request) as response, open(gz_path, "wb") as f:
    shutil.copyfileobj(response, f)
print("downloaded successfully\n")

with gzip.open(gz_path, "rb") as gz_file, open(json_path, "wb") as out_file:
    shutil.copyfileobj(gz_file, out_file)
print("decompressed successfully")
