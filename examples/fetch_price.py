"""
fetch current price
"""
import pprint
import pyfairdesk

exchange = pyfairdesk.Fairdesk()
resp = exchange.fetch_ticker(symbol='btcusdt')
pprint.pprint(resp)