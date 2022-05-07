"""Fairdesk public api
"""
import requests

BASE_ENDPOINT = "https://api.fairdesk.com"

def fetch_tickers() -> dict:
    """fetch tickers

    Returns:
        dict: _description_
    """
    url_path = "/api/v1/public/products"
    url = BASE_ENDPOINT + url_path
    resp = requests.get(url)
    return resp.json()

def fetch_order_book(symbol: str) -> dict:
    """fetch order book with REST API

    Args:
        symbol (str): BTCUSDT

    Returns:
        dict: _description_
    """
    url_path = "/api/v1/public/md/orderbook"
    url = BASE_ENDPOINT + url_path
    params = {"symbol": symbol}
    resp = requests.get(url, params=params)
    return resp.json()

def fetch_recent_trade(symbol: str) -> dict:
    """fetch recent trade

    Args:
        symbol (str): btcusdt

    Returns:
        dict: _description_
    """
    url_path = "/api/v1/public/md/trade-recent"
    url = BASE_ENDPOINT + url_path
    params = {"symbol": symbol}
    resp = requests.get(url, params=params)
    return resp.json()

def fetch_trade_history(symbol: str, fromts: int, limit:int=500):
    """_summary_

    Args:
        symbol (str): _description_
        fromts (int): _description_
        limit (_type_, optional): _description_. Defaults to int.

    Returns:
        _type_: _description_
    """
    url_path = "/api/v1/public/md/trade-history"
    url = BASE_ENDPOINT + url_path
    params = {
        "symbol": symbol,
        "from": fromts,
        "limit": limit
    }
    resp = requests.get(url, params=params)
    return resp.json()

def fetch_24h(symbol: str):
    """fetch 24h ticker

    Args:
        symbol (str): ticker (btcusdt)

    Returns:
        _type_: _description_
    """
    url_path = "/api/v1/public/md/ticker24h"
    url = BASE_ENDPOINT + url_path
    params = {"symbol": symbol}
    resp = requests.get(url, params=params)
    return resp.json()

def fetch_ohlcv(symbol: str, interval: str, from_ts: int, to_ts: int, limit: int=500):
    """_summary_

    Args:
        symbol (str): _description_
        interval (str): _description_
        from_ts (int): _description_
        to_ts (int): _description_
        limit (int, optional): _description_. Defaults to 500.

    Returns:
        _type_: _description_
    """
    url_path = "/api/v1/public/md/kline"
    url = BASE_ENDPOINT + url_path
    params = {
        "symbol": symbol,
        "interval": interval,
        "from": from_ts,
        "to": to_ts,
        "limit": limit
    }
    resp = requests.get(url, params=params)
    return resp.json()

if __name__ == "__main__":
    import pprint
    import datetime
    #pprint.pprint(fetch_tickers())
    #pprint.pprint(fetch_order_book("btcusdt"))
    #pprint.pprint(fetch_recent_trade("btcusdt"))
    #pprint.pprint(fetch_24h("btcusdt"))

    #start = datetime.datetime.strptime("2022-05-01", "%Y-%m-%d")
    #end = datetime.datetime.strptime("2022-05-07", "%Y-%m-%d")
    #from_ts = int(datetime.datetime.timestamp(start) * 1000)
    #to_ts = int(datetime.datetime.timestamp(end) * 1000)
    #pprint.pprint(fetch_ohlcv('btcusdt', '1d', from_ts, to_ts))