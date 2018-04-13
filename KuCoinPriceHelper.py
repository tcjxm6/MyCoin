# -*- coding=UTF-8 -*-

import requests
import urllib
import base64
import hmac
import hashlib
import sys
import time
import json

RHOC_ETH = 'RHOC-ETH'
ETH_BTC = 'ETH-BTC'
ETH_USDT = 'ETH-USDT'

URL_KC_COIN_PRICE_SELL = 'https://kitchen-6.kucoin.com/v1/{}/open/orders-sell?limit=100&c=&lang=zh_CN'
URL_KC_COIN_PRICE_BUY = 'https://kitchen-6.kucoin.com/v1/{}/open/orders-buy?limit=100&c=&lang=zh_CN'

proxies = {
  "http": "http://127.0.0.1:1087",
  "https": "http://127.0.0.1:1087",
}

def getCoinBuyPrice(coin):
	url = URL_KC_COIN_PRICE_BUY.format(str(coin))
	r = requests.get(url,proxies=proxies)
	responseDic = json.loads(r.text)
	return responseDic
	pass

def getCoinSellPrice(coin):
	url = URL_KC_COIN_PRICE_SELL.format(str(coin))
	r = requests.get(url,proxies=proxies)
	responseDic = json.loads(r.text)
	return responseDic
	pass