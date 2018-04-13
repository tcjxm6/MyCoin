from KuCoin import client
from TTUser import *
from AITcjxm6 import *
import KuCoinPriceHelper
# -*- coding=UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests
import urllib
import base64
import hmac
import hashlib
import sys
import time
import json

Client = client.Client

# optionally pass the language you wbuysould like to use
# see client.get_languages() for options


proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'https://127.0.0.1:1087'
}




user = TTUser(api_key,api_secret)




aiTT = Tcjxm()

while 1:
	print 'begin'
	try:
		user.refreshOrderList('RHOC-ETH')
		user.refreshCoinBalance()
		price = KuCoinPriceHelper.getCoinBuyPrice('RHOC-ETH')
		buyOrders = price['data']
		newBuyOrders = []
		for buyItem in buyOrders:
			order = TTOrder([])
			order.price = buyItem[0]
			order.amount = buyItem[1]
			newBuyOrders.append(order)


		price2 = KuCoinPriceHelper.getCoinSellPrice('RHOC-ETH')
		sellOrders = price2['data']
		newSellOrders = []
		for sellItem in sellOrders:
			order = TTOrder([])
			order.price = sellItem[0]
			order.amount = sellItem[1]
			newSellOrders.append(order)
		aiTT.analyzeRHOCOrder(newBuyOrders,newSellOrders,user)
		pass
	except Exception as e:
		print e
		continue
	
	print 'end'
	pass












