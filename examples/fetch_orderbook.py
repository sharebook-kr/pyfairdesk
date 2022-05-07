"""
fetch current price
"""
import pprint
import pyfairdesk

exchange = pyfairdesk.Fairdesk()
resp = exchange.fetch_order_book(symbol="btcusdt")
pprint.pprint(resp)