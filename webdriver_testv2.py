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
options.add_argument('-headless')

views=3

line=0
drivers=[]
chrome_options = webdriver.ChromeOptions()





for x in range(views):
	flag=False
	while(flag==False):
		flag=True
		try:
			temp=alist[x+15].split(':')
			profile=webdriver.FirefoxProfile()
			profile.set_preference('network.proxy_type',1)
			profile.set_preference('network.proxy.http',temp[0])
			profile.set_preference('network.proxy.http_port',temp[1])

			driver=webdriver.Firefox(firefox_profile=profile)
			driver.get('http://checkmyip.com')
			print("create viewer ",(x))
			#time.sleep(10)
		except Exception as error:
			print('Caught this error: ' + repr(error))
			flag=False
	drivers.append(driver)

time.sleep(3600)