from KuCoin import client
from TTUser import *
from AITcjxm6 import *
import KuCoinPriceHelper
import smtplib  
from email.mime.text import MIMEText  
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
# -*- coding=UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

mailto_list=['tcjxm6@aliyun.com'] 
mail_host="smtp.126.com"  
mail_user="tcjxm66@126.com"    
mail_pass="TTT123456"   
mail_postfix="126.com"  

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


  
def send_mail(to_list,sub,content):  
    me="good"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEMultipart()  
    part = MIMEText(content)  
    msg.attach(part)  
    
    msg['Subject'] = sub  
    msg['From'] = mail_user  
    msg['To'] = ";".join(to_list)
    

    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        return False  


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
		buyOrders = user.getBuyOrders('RHOC-ETH')
		sellOrders = user.getSellOrders("RHOC-ETH")
		if user.freezeBalanceRHOC == 0 and user.freezeBalanceETH == 0 and len(buyOrders) == 0 and len(sellOrders) == 0:
			print 'order complete'
			send_mail(mailto_list,'hello tt','order have complete!')
			pass
		pass
		time.sleep(5)
		send_mail(mailto_list,'hello tt','order have complete!')
	except Exception as e:
		print e
		continue
	
	print 'end'
	pass












