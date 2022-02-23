#Author: Juverofan

import os
import sys
import requests
import time
from bs4 import BeautifulSoup as BS
import array as arr
from datetime import datetime

coins = ['SHIB','ETH','BTC','ALICE','BNB']
coin_vals = [0.000032,3100,42000,8.12,400]
coin_tops = [0.000038,3800,48000,9.20,430]

url = "https://www.binance.com/en/trade/SHIB_USDT"
domains = url.split("/")
domain = "" 
i = 0
while i < 3:
	domain += domains[i]+"/"
	i += 1 
print("Data from domain: " + domain+"\n")
save_data = open("coin_val.txt","a+")
now = datetime.now() 
for coin in coins:
	url = "https://www.binance.com/en/trade/"+coin+"_USDT"
	r = requests.get(url)
	soup = BS(r.text, "html.parser")

	for ttag in soup.find_all('title'):
		val = str(ttag.contents).split("|")[0].strip().replace("['","")
		content = coin + ": "+str(val.strip())
		if float(val) <= coin_vals[coins.index(coin)]:
			content = content + " - DOWN"
		elif float(val) >= coin_tops[coins.index(coin)]:
			content = content + " - UP"
		else:
			content = content + " - NORMAL"
		print(content)
		date_time = now.strftime("%d/%m/%Y %H:%M")
		save_data.write(str(date_time)+"|"+coin+"|"+str(val.strip())+"\n")

save_data.close()