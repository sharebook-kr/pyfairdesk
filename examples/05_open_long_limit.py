"""adjust leverage
"""
import pprint
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)
resp = exchange.create_limit_buy_order("btcusdt", "long", True, 0.001, 40000)
pprint.pprint(resp)
