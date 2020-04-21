from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import requests
import time
def getProxyList():
	resp = requests.get('https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US')
	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	element = resp.text.split('\r\n')
	#return list of ip with port exp: 64.17.30.238:61496 and so on
	#use pop() to get and remove list element
	return element

alist=getProxyList()

options=webdriver.FirefoxOptions()

views=3

line=0
drivers=[]

proxyFile='proxies.txt'
lines = [line.rstrip('\r\n') for line in open(proxyFile)]




for x in range(views):
	flag=False
	while(flag==False):
		flag=True
		try:
			temp=alist[x+15]
			print(temp)
			#chrome_options = webdriver.ChromeOptions()
			#chrome_options.add_argument('--proxy-server=%s' % temp)
			#chrome_options=chrome_options
			driver=webdriver.Chrome()
			driver.get('https://www.youtube.com/watch?v=HPUSFsxAbKc')
			#driver.get('https://whatismyipaddress.com')
			print("create viewer ",(x))
			time.sleep(10000)
			#time.sleep(10)
		except Exception as error:
			print('Caught this error: ' + repr(error))
			flag=False
	drivers.append(driver)
	line+=1
time.sleep(3600)