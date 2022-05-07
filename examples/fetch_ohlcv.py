"""
fetch current price
"""
import pprint
import pyfairdesk
import datetime
import pandas as pd

exchange = pyfairdesk.Fairdesk()

start = datetime.datetime.strptime("2022-05-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2022-05-07", "%Y-%m-%d")
from_ts = int(datetime.datetime.timestamp(start) * 1000)
to_ts = int(datetime.datetime.timestamp(end) * 1000)

resp = exchange.fetch_ohlcv(
    symbol='btcusdt',
    interval='1d',
    from_ts=from_ts,
    to_ts=to_ts,
    limit=1000
)
pprint.pprint(resp)

data = resp['data']
df = pd.DataFrame(data)
dt = pd.to_datetime(df['openTime'], unit='ms')
df.set_index(dt, inplace=True)
print(df)