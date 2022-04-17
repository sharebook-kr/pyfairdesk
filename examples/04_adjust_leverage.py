"""adjust leverage
"""
import pprint
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)
resp = exchange.adjust_leverage(symbol="btcusdt", isolated=True, leverage=2)
pprint.pprint(resp)
