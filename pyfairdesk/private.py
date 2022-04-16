"""Fairdesk private api
"""
import time
import hmac
import hashlib
import urllib
import json
import requests


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

    def _generate_signature(self, url_path, query_string, body, expiry):
        message = url_path + query_string + str(expiry) + urllib.parse.urlencode(body)
        return  hmac.new(
            self.api_secret.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256).hexdigest()

    def _post_request(self, url_path:str, query_string:str, body:dict):
        expiry = int(time.time() * 1000000)
        signatue = self._generate_signature(url_path, query_string, body, expiry)

        headers = {
            "x-fairdesk-access-key": self.api_key,
            "x-fairdesk-request-expiry": str(expiry),
            "x-fairdesk-request-signature": signatue
        }

        url = self.BASE_ENDPOINT + url_path
        resp = requests.post(url=url, headers=headers, data=json.dumps(body))
        return resp.json()

    def _get_request(self, url_path: str, params: str=""):
        expiry = int(time.time() * 1000000)
        signatue = self._generate_signature(url_path, params, body="", expiry=expiry)

        headers = {
            "x-fairdesk-access-key": self.api_key,
            "x-fairdesk-request-expiry": str(expiry),
            "x-fairdesk-request-signature": signatue
        }

        url = self.BASE_ENDPOINT + url_path
        resp = requests.get(url=url, headers=headers, params=params)
        return resp.json()

    def fetch_positions(self):
        """query current furture positions

        Returns:
            _type_: _description_
        """
        return self._get_request("/api/v1/private/account/positions")



if __name__ == "__main__":
    import pprint

    with open("../fairdesk.key", "r", encoding="utf-8") as f:
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()

    exchange = Fairdesk(key, secret)
    markets = exchange.load_markets()
    print(len(markets['data']))

    pprint.pprint(exchange.fetch_positions())
