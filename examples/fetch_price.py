"""
fetch current price
"""
import pprint
import pyfairdesk

exchange = pyfairdesk.Fairdesk()
pprint.pprint(exchange.fetch_24h(symbol='btcusdt'))