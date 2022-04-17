"""fetch configure
"""
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)
resp = exchange.fetch_symbol_config()
data = resp['data']
for d in data:
    #print(d)
    if d['symbol'] in ['btcusdt', 'ethusdt']:
        print(d)
