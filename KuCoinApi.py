# -*- coding=UTF-8 -*-

import requests
import urllib
import base64
import hmac
import hashlib
import sys
import time
import json

URL_HOST = 'https://api.kucoin.com'

#获取秘钥列表
URL_KC_KEYLIST = '/v1/api/list'
#  获取币价格
URL_KC_COIN_BALANCE = '/v1/account/{}/balance'
#  新建挂单
URL_KC_CREATE_ORDER = '/v1/order'
#  新建挂单
URL_KC_CANCEL_ALLORDER = '/v1/order/cancel-all'


def getUnixTime():
	return str(int(round(time.time() * 1000)))
	pass

def hmac_sha256(key, msg):
    hash_obj = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
    return hash_obj.hexdigest()
    pass

def getHeaders(key,secret,nonce,endpoint,queryString):
	h = {'KC-API-KEY': key,
	  'KC-API-NONCE': getUnixTime(),
	  'KC-API-SIGNATURE': getSignature(endpoint,nonce,queryString,secret),
	  'Accept-Language': 'zh_CN',
	  'content-type':'application/json'}
	return h
	pass

def getSignature(endpoint,nonce,queryString,secret):
	strForSign = endpoint + "/" + nonce +"/" + queryString
	print strForSign
	signatureStr = base64.b64encode(strForSign)
	# print 'base64 : ' + signatureStr
	signatureResult = hmac_sha256(secret,signatureStr)
	# print 'signatureResult : ' + signatureResult
	return signatureResult
	pass

def getQueryString(mType,price,amount):
	# symbol = 'amount=' + str(amount) + '&price=' + str(price) + '&symbol=ETH-BTC' + '&type=' + str(mType)
	symbol = 'type=BUY'
	return symbol
	pass

#  酷币请求函数
def getKeyList(key,secret,nonce):
	h = getHeaders(key,secret,nonce,URL_KC_KEYLIST,'')
	# print h
	r = requests.get(URL_HOST+URL_KC_KEYLIST, headers=h)
	print r.text
	pass
#  酷币价格获取接口
def getCoinBalance(key,secret,nonce,coin):
	url = URL_KC_COIN_BALANCE.format(str(coin))
	h = getHeaders(key,secret,nonce,url,'')
	print url
	r = requests.get(URL_HOST+url, headers=h)
	print r.text
	pass

#  取消所有挂单
def cancelAllOrder(key,secret,nonce):
	url = URL_KC_CANCEL_ALLORDER
	queryString = getQueryString('','','')
	print queryString
	h = getHeaders(key,secret,nonce,url,'')
	print url
	mData = {
		# 'type':'BUY',	
	}
	r = requests.post(URL_HOST+url, data=json.dumps(mData), headers=h)
	print r.text
	pass
#  酷币挂单接口
def createOrder(key,secret,nonce,mType,price,amount,symbol):
	queryString = getQueryString(mType,price,amount)
	print queryString
	url = URL_KC_CREATE_ORDER
	h = getHeaders(key,secret,nonce,url,queryString)
	print url
	mData = {
		'amount':amount,
		'price':price,
		'symbol':symbol,
		'type':mType,
		
		
	}
	r = requests.post(URL_HOST+url,data=json.dumps(mData), headers=h)
	print r.text
	pass

#  kucoinAPI 管理类
class KuCoinApiManager(object):
	"""docstring for KuCoinApi"""
	def __init__(self, key, secret):
		super(KuCoinApiManager, self).__init__()
		self.key = key
		self.secret = secret

cancelAllOrder('5ab0c3ee09e5a1a61e43cb34','15844185-f6ca-47af-8e34-b5bcf8205f75',getUnixTime())
createOrder('5ab0c3ee09e5a1a61e43cb34','15844185-f6ca-47af-8e34-b5bcf8205f75',getUnixTime(),'BUY','10','1.1','ETH-BTC')
# getKeyList('5ab0c3ee09e5a1a61e43cb34','15844185-f6ca-47af-8e34-b5bcf8205f75',getUnixTime())
# getCoinBalance('5ab0c3ee09e5a1a61e43cb34','15844185-f6ca-47af-8e34-b5bcf8205f75',getUnixTime(),'BTC')
