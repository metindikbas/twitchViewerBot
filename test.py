import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def getProxyList():
	resp = requests.get('https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US')
	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	element = resp.text.split('\r\n')
	#return list of ip with port exp: 64.17.30.238:61496 and so on
	#use pop() to get and remove list element
	return element


alist=getProxyList()
drivers=[]
options=webdriver.FirefoxOptions()

for i in range(30):
	temp=alist[i].split(':')
	profile=webdriver.FirefoxProfile()
	profile.set_preference('network.proxy_type',1)
	profile.set_preference('network.proxy.http',temp[0])
	profile.set_preference('network.proxy.http_port',temp[1])

	driver=webdriver.Firefox(firefox_profile=profile,firefox_options=options)
	driver.get('https://www.youtube.com/watch?v=HPUSFsxAbKc&t=2s')
	drivers.append(driver)
	print("working on:"+str(i))
	if ((i+1)%3)==0:
		print("sleeping:"+str(i))
		time.sleep(40)
		print("finish sleeping")
		for p in range(len(drivers)):
			print("tapping here")
			drivers.pop().close()






'''

temp=alist[6].split(':')
profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference('network.proxy.http',temp[0])
profile.set_preference('network.proxy.http_port',temp[1])

driver=webdriver.Firefox(firefox_profile=profile,firefox_options=options)
driver.get('https://www.youtube.com/watch?v=HPUSFsxAbKc&t=2s')

----------------

temp=alist[3].split(':')
profile=webdriver.FirefoxProfile()
profile.set_preference('network.proxy_type',1)
profile.set_preference('network.proxy.http',temp[0])
profile.set_preference('network.proxy.http_port',temp[1])
driver1=webdriver.Firefox(firefox_profile=profile,firefox_options=options)
driver1.get('https://www.youtube.com/watch?v=HPUSFsxAbKc&t=2s')

time.sleep(10000)
driver.close()
driver1.close()
'''