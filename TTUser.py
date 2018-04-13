# -*- coding=UTF-8 -*-
from KuCoin import client

Client = client.Client

class TTUser(object):

	# 交易类型 RHOC-ETH
	symbols = []
	# 交易订单 key:symbol  val:orders
	orders = {}
	# key
	key = ''
	# secret
	secret = ''
	# KuCoin client
	m_client = object
	balanceRHOC = 0
	freezeBalanceRHOC = 0
	balanceETH = 0
	freezeBalanceETH = 0
	# 代理
	proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'https://127.0.0.1:1087'
	}

	"""docstring for TTUser"""
	def __init__(self,key,secret):
		self.key = key
		self.secret = secret
		self.m_client = Client(key, secret, language='zh_CN',requests_params={'proxies': self.proxies})
		pass
	
	def createSellOrder(self,symbol, price, amount):
		self.m_client.create_sell_order(symbol, price, amount)
		pass

	def getBuyOrders(self,symbols):
		orders = self.orders[symbols]
		return orders['BUY']
		pass

	def getSellOrders(self,symbols):
		orders = self.orders[symbols]
		return orders['SELL']
		pass

	def refreshOrderList(self,symbols):
		rsp = self.m_client.get_active_orders(symbols)
		buys = rsp['BUY']
		sells = rsp['SELL']
		newBuys = []
		for buyItem in buys:
			order = TTOrder(buyItem)
			newBuys.append(order)
		newSells = []
		for sellItem in sells:
			sellOrder = TTOrder(sellItem)
			newSells.append(sellOrder)
		newOrders = {}
		newOrders['BUY'] = newBuys
		newOrders['SELL'] = newSells
		self.orders[symbols] = newOrders
		pass

	def refreshCoinBalance(self):
		coins = ['RHOC','ETH']
		for coin in coins:
			rsp = self.m_client.get_coin_balance(coin)
			if coin == 'RHOC':
				self.balanceRHOC = rsp['balance']
				self.freezeBalanceRHOC = rsp['freezeBalance']
				pass
			elif coin == 'ETH':
				self.balanceETH = rsp['balance']
				self.freezeBalanceETH = rsp['freezeBalance']
				pass
			pass
		pass

	def getUserInfo(self):
		rsp = self.m_client.get
		pass

	def cancelAllOrder(self):
		self.m_client.cancel_all_orders()
		pass

	def cancelRHOCAllOrder(self):
		self.m_client.cancel_all_orders('RHOC-ETH')
		pass

	def cancelRHOCAllBuyOrder(self):
		self.m_client.cancel_all_orders('RHOC-ETH','BUY')
		pass

	def cancelRHOCAllSellOrder(self):
		self.m_client.cancel_all_orders('RHOC-ETH','SELL')
		pass
	


class TTCoin(object):
	"""docstring for TTCoin"""
	assignedCount = 0
	drawingCount = 0
	grantCountDownSeconds = 0
	def __init__(self, dict):
		self.assignedCount = dict['grantCountDownSeconds']
		self.drawingCount = dict['drawingCount']
		self.grantCountDownSeconds = dict['grantCountDownSeconds']
		



class TTOrder(object):
	"""docstring for Order"""
	time = ''
	types = ''
	price = 0
	amount = ''
	deal_amount = ''
	order_oid = ''
	desc = ''
	def __init__(self,buyItem):
		if len(buyItem) != 6:
			return
		self.order_oid = buyItem[0]
		self.types = buyItem[1]
		self.price = buyItem[2]
		self.amount = buyItem[3]
		self.deal_amount = buyItem[4]
		self.desc = buyItem[5]
		pass

		
