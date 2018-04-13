from KuCoin import client
import KuCoinPriceHelper
from AITcjxm6 import *
# -*- coding=UTF-8 -*-

import requests
import urllib
import base64
import hmac
import hashlib
import sys
import time
import json


def work():
	buyResponse = KuCoinPriceHelper.getCoinBuyPrice(KuCoinPriceHelper.ETH_BTC)
	# print response['data']
	sellResponse = KuCoinPriceHelper.getCoinSellPrice(KuCoinPriceHelper.ETH_BTC)
	# print response['data']

	sellOnePriceArr = sellResponse['data'][0]
	buyOnePriceArr = buyResponse['data'][0]

	sellPrice = sellOnePriceArr[0]
	buyPrice = buyOnePriceArr[0]

	dealPrice(buyPrice,sellPrice)

	pass


def dealPrice(buyPrice,sellPrice):

	aiTT = Tcjxm()

	percent = aiTT.getPriceDifferencePer(buyPrice,sellPrice,buyPrice)
	print 'buyPrice : ' + str(buyPrice) + 'sellPrice : '+str(sellPrice)  + '   '+str(percent)
	pass




if __name__ == "__main__":

	while 1:
		try:
			work()
			pass
		except Exception as e:
			print e
			continue
		
		time.sleep(2)
		pass

	pass