"""load markets
"""
import pprint
import pyfairdesk

exchange = pyfairdesk.Fairdesk()
resp = exchange.load_markets()
data = resp['data']

for market in data:
    if market['symbol'] == 'btcusdt':
        pprint.pprint(market)
