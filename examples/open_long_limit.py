"""
Open Long (Buy)
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
    side="buy",
    amount="0.001",
    price=35000
)
pprint.pprint(resp)

