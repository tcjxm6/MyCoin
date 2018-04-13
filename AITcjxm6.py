# -*- coding=UTF-8 -*-
from TTUser import *
import time

class Tcjxm:
	"""docstring for Tcjxm"""
	user = object
	buyOrders = []
	sellOrders = []
	maxBuyVal = 0.002451
	minSellVal1 = 0.0025
	minSellVal2 = 0.00253
	minSellVal3 = 0.002539
	firstRun = True

	def __init__(self):
		pass

	
	def getPriceDifferencePer(self,price1,price2,price):
		diffPrice = price1 - price2
		return diffPrice/price
		pass

	def analyzeRHOCOrder(self,buyOrders,sellOrders,user):
		self.user = user
		self.buyOrders = buyOrders
		self.sellOrders = sellOrders
		if self.firstRun:
			self.firstRun = False
			# self.user.cancelRHOCAllOrder()
			pass

		# 当ETH有钱的时候，开始处理买
		if user.balanceETH > 0.02:
			# self.analyzeConservativeBuyRHOC()
			# self.analyzeAIBuyRHOC()
			pass
		self.analyzeConservativeSellRHOC()
		# 当RHOC大于的时候，开始卖
		if user.balanceRHOC > 0.02:
			# self.analyzeConservativeSellRHOC()
			pass
		# if user.freezeBalanceRHOC > 0.02:
		# 	self.analyzeConservativeSellRHOC()
		# 	pass
		pass
		if user.freezeBalanceETH > 0.02:
			# self.analyzeConservativeBuyRHOC()
			# self.analyzeAIBuyRHOC()
			pass

	def analyzeAIBuyRHOC(self):
		buyAmount = 0
		for order in self.buyOrders:
			buyAmount += self.getRealAmount(order)
			print order.price 
			if order.price < self:
				pass
			pass
		pass

	def analyzeConservativeBuyRHOC(self):
		for order in self.buyOrders:
			print order.price 
			if order.price < self.maxBuyVal:
				if self.isMe(order):
					return
					pass
				newPrice = order.price + 0.0000001 
				print '新的买订单啦：'+str(newPrice)
				return
				pass
			pass
		pass

	def analyzeConservativeSellRHOC(self):
		meOrder = TTOrder([])
		for order in self.sellOrders:
			# print order.price 
			minSellVal = self.minSellVal2
			if order.price > minSellVal:
				if self.isMe(order):
					meOrder = order
					print '是我自己拉'
					continue
					pass

				print str(meOrder.price) + '  他人单价格' + str(order.price) + '相差：' + str(order.price - meOrder.price)
				if (order.price - meOrder.price) != 0.0000001:
					print str(order.amount) + '  ' + str(order.price) 
					newPrice = order.price - 0.0000001
					self.makeNewSellOrder(newPrice)
					print '新的卖订单啦：'+str(newPrice)
					return
					pass
				pass
				print '没啥事了，再来看看'
				return
			pass
		pass

	def analyzeConservativeSellRHOC2(self):
		for order in self.sellOrders:
			# print order.price 
			minSellVal = 1
			if (self.user.freezeBalanceRHOC+self.user.balanceRHOC) > 3000:
				minSellVal = minSellVal1
				pass
			if order.price > minSellVal:
				if self.isMe(order):
					return
					pass
				newPrice = order.price - 0.0000001 
				if self.isOutRange(newPrice,'SELL'):
					continue
					pass
				print '新的卖订单啦：'+str(newPrice)
				return
				pass
			pass
		pass

	def isMe(self,order):
		for mOrder in self.user.getBuyOrders('RHOC-ETH'):
			if mOrder.price == order.price:
				return True
				pass
			pass
		print self.user.getSellOrders('RHOC-ETH')
		for mOrder in self.user.getSellOrders('RHOC-ETH'):
			print '卖的订单的价格'
			print mOrder.price
			print order.price
			if mOrder.price == order.price:
				return True
				pass
			pass
		return False
		pass

	def isOutRange(self,price,type):
		if type == 'BUY' and len(self.sellOrders) > 0:
			firstSellPrice = self.sellOrders[0]
			spread = firstSellPrice - price
			rate = spread / price
			# if spread <= 0 or rate <= 0.02:
			if spread <= 0:
				return True
				pass
			return False
			pass
		if type == 'SELL' and len(self.buyOrders) > 0:
			firstBuyPrice = self.buyOrders[0]
			spread = price - firstBuyPrice
			rate = spread / price
			# if spread <= 0 or rate <= 0.02:
			if spread <= 0:
				return True
				pass
			return False
			pass
		return True
		pass

	def getRealAmount(self,order):
		for mOrder in self.user.getBuyOrders('RHOC-ETH'):
			if mOrder.price == order.price:
				return order.amount - mOrder.amount
				pass
			pass
		return order.amount
		pass

	def makeNewSellOrder(self,price):
		self.user.cancelRHOCAllSellOrder()
		time.sleep(5)
		self.user.refreshCoinBalance()
		amount = self.user.balanceRHOC
		self.user.createSellOrder('RHOC-ETH', price, int(amount))
		time.sleep(5)
		pass











