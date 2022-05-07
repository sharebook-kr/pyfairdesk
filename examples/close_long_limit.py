"""
Close Long
"""
import pprint
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)

# limit order
resp = exchange.create_limit_order(
    symbol="btcusdt",
    side="sell",
    amount="0.001",
    price=37000,
    params={'reduce_only': True }
)
pprint.pprint(resp)

