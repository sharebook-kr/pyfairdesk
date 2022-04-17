# pyfairdesk
python wrapper of the Fairdesk API 


# Fairdesk Sign up

[Fairdesk Sign up Referral](https://www.fairdesk.com/signup?channels=pyquant&vipCode=pyquant)

# Install

```
$ pip install pyfairdesk
```

# API Usage
## Load Markets
[official document](https://github.com/fairdesk/fairdesk-api-docs#queryproductinfo)

```
import pyfairdesk

exchange = pyfairdesk.Fairdesk()
exchange.load_markets()
```

## fetch balances

```
import pprint
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)
resp = exchange.fetch_balance()
data = resp['data']
pprint.pprint(data)
```

## Margin mode and leverage

```
import pyfairdesk

with open("../fairdesk.key", "r", encoding="utf-8") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()

exchange = pyfairdesk.Fairdesk(key, secret)
resp = exchange.fetch_symbol_config()
data = resp['data']
for symbol in data:
    print(symbol)
```

**response**
```
{'symbol': 'axsusdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
{'symbol': 'thetausdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
{'symbol': 'linkusdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
{'symbol': 'ftmusdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
{'symbol': 'xlmusdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
{'symbol': 'sushiusdt', 'crossLeverage': 20, 'isolatedLeverage': 20, 'makerFeeRate': '0.00018', 'takerFeeRate': '0.00028'}
```

## order

