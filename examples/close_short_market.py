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

# market order
resp = exchange.create_market_order(
    symbol="btcusdt",
    side="buy",
    amount="0.001",
    params={'close_position': True}
)
pprint.pprint(resp)
