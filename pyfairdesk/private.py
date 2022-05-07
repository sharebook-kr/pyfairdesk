"""Fairdesk private api
"""
import time
import hmac
import hashlib
import json
import requests
from datetime import datetime


class Fairdesk:
    """Fairdesk
    """
    BASE_ENDPOINT = "https://api.fairdesk.com"

    def __init__(self, api_key: str="", api_secret: str=""):
        """initializer

        Args:
            api_key (str, optional): api key (ID). Defaults to "".
            api_secret (str, optional): api secret. Defaults to "".
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def load_markets(self) -> dict:
        """load markets

        Returns:
            dict: status, error, data
        """
        url = self.BASE_ENDPOINT + "/api/v1/public/products"
        resp = requests.get(url)
        return resp.json()

    def _generate_signature(self, url_path, query_string, body: dict, expiry):
        if len(body) != 0:
            message = url_path + query_string + str(expiry) + json.dumps(body)
        else:
            message = url_path + query_string + str(expiry)

        return  hmac.new(
            self.api_secret.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256).hexdigest()

    def _put_request(self, url_path:str, body:dict):
        expiry = int(time.time() * 1000000 + 60 * 1000000)
        signatue = self._generate_signature(url_path, "", body, expiry)

        headers = {
            "x-fairdesk-access-key": self.api_key,
            "x-fairdesk-request-expiry": str(expiry),
            "x-fairdesk-request-signature": signatue
        }

        url = self.BASE_ENDPOINT + url_path
        resp = requests.put(url=url, headers=headers, json=body)
        return resp.json()

    def _post_request(self, url_path:str, body:dict):
        expiry = int(time.time() * 1000000 + 60 * 1000000)
        signatue = self._generate_signature(url_path, "", body, expiry)

        headers = {
            "x-fairdesk-access-key": self.api_key,
            "x-fairdesk-request-expiry": str(expiry),
            "x-fairdesk-request-signature": signatue
        }

        url = self.BASE_ENDPOINT + url_path
        if len(body) == 0:
            resp = requests.post(url=url, headers=headers)
        else:
            resp = requests.post(url=url, headers=headers, json=body)
        return resp.json()

    def _get_request(self, url_path: str, params: str=""):
        expiry = int(time.time() * 1000000 + 60 * 1000000)
        signatue = self._generate_signature(url_path, params, body={}, expiry=expiry)

        headers = {
            "x-fairdesk-access-key": self.api_key,
            "x-fairdesk-request-expiry": str(expiry),
            "x-fairdesk-request-signature": signatue
        }

        url = self.BASE_ENDPOINT + url_path
        resp = requests.get(url=url, headers=headers, params=params)
        return resp.json()

    def fetch_positions(self) -> dict:
        """query current furture positions

        Returns:
            dict : _description_
        """
        return self._get_request("/api/v1/private/account/positions")

    def fetch_open_orders(self) -> dict:
        """fetch open orders

        Returns:
            dict: _description_
        """
        return self._get_request("/api/v1/private/trade/open-orders")

    def fetch_balance(self) -> dict:
        """fetch balance

        Returns:
            dict: balance
        """
        return self._get_request("/api/v1/private/account/balance")

    def _create_order(self, symbol: str, side: str, position: str,
                      isolated: bool, amount: float, price: float,
                      order_type: str) -> dict:
        data = {
            "symbol": symbol,
            "side": side,
            "positionSide": position,
            "isolated": str(isolated).lower(),
            "quantity": str(amount),
            "price": str(price),
            "type": order_type,
            "timeInForce": "POST_ONLY"
        }
        return self._post_request("/api/v1/private/trade/place-order", data)

    def create_limit_buy_order(self, symbol: str, position: str, isolated: bool,
                               amount: float, price: float) -> dict:
        """_summary_

        Args:
            symbol (str): symbol (btcusdt)
            position (str): long, short
            isolated (bool): True, False
            amount (float): quantity
            price (float): price

        Returns:
            dict: _description_
        """
        return self._create_order(symbol, "BUY", position.upper(), isolated,
                                  amount, price, "LIMIT")

    def cancel_all_orders(self, symbol: str="btcusdt") -> dict:
        """cancel all orders

        Returns:
            dict: _description_
        """
        data = {
            "symbol": symbol,
            "settleCcy": "USDT"
        }
        return self._post_request("/api/v1/private/trade/cancel-all-order", data)

    def cancel_order(self, symbol: str, order_id: str) -> dict:
        """cancel single order by order_id

        Args:
            symbol (str): symbol (btcusdt)
            order_id (str): order id to cancel

        Returns:
            dict: basic output format
        """
        data = {
            "symbol": symbol,
            "orderId": order_id
        }
        return self._post_request("/api/v1/private/trade/cancel-order", body=data)

    def fetch_symbol_config(self) -> dict:
        """fetch symbol config

        Returns:
            dict: _description_
        """
        return self._get_request("/api/v1/private/account/symbol-config")

    def adjust_leverage(self, symbol: str, isolated: bool, leverage: int) -> dict:
        """adjust leverage

        Args:
            symbol (str): _description_
            isolated (bool): _description_
            leverage (int): _description_

        Returns:
            dict: _description_
        """
        data = {
            "symbol": symbol,
            "leverage": str(leverage),
            "isolated": isolated
        }
        return self._put_request("/api/v1/private/account/config/adjust-leverage", data)

    def create_websocket_token(self) -> dict:
        """create websocket token

        Returns:
            dict: token
        """
        return self._post_request("/api/v1/private/token/create", body={})

    def refresh_websocket_token(self) -> dict:
        """refresh websocket token

        Returns:
            dict: token
        """
        return self._post_request("/api/v1/private/token/refresh", body={})

    def delete_websocket_token(self) -> dict:
        """delete websocket token

        Returns:
            dict: token
        """
        return self._post_request("/api/v1/private/token/delete", body={})

if __name__ == "__main__":
    import pprint

    with open("../fairdesk.key", "r", encoding="utf-8") as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()

    exchange = Fairdesk(key, secret)
    pprint.pprint(exchange.create_websocket_token())
    #resp = exchange.adjust_leverage(symbol="btcusdt", isolated=True, leverage=2)
    #pprint.pprint(resp)
    #resp = exchange.create_limit_buy_order("btcusdt", "long", True, 0.001, 40000)
    #pprint.pprint(resp)
