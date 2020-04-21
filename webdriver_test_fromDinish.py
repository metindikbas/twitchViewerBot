from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
views=3
url='http://www.bilibili.com/video/av46952064'
#url="http://www.youtube.com"
#url='http://www.google.com'
proxyFile='privateList.txt'
#chromedriver="home\yufan\Desktop\twitch-viewer-master"
#proxyFile='proxies.txt'
lines = [line.rstrip('\r\n') for line in open(proxyFile)]
line=0
drivers=[]
chrome_options = webdriver.ChromeOptions()

fireFox_options=webdriver.FirefoxOptions()




for x in range(views):
	flag=False
	while(flag==False):
		flag=True
		try:
			#chrome_options.add_argument('--headless')
			chrome_options.add_argument('--proxy-server={}'.format(lines[line]))
			#temp=lines[line].split(':')
			driver=webdriver.Chrome(chrome_options=chrome_options)
			#driver.get("https://api.ipify.org")
			#detect_ip=driver.find_element_by_tag_name("pre").text
			#ip=lines[line].split(':')
			
			#service_args = ['--proxy={}'.format(lines[line]),'--proxy-type=https']
			#driver = webdriver.PhantomJS('phantomjs.exe')
			#, service_args = service_args
			print(lines[line])
			line += 1
			time.sleep(5000)
			#if(ip[0]!=detect_ip):
			#	raise Exception('ip proxy mismatch')
			driver.get("https://www.youtube.com/watch?v=HPUSFsxAbKc")
			'''
			print('working on '+temp[0])
			profile=webdriver.FirefoxProfile()
			profile.set_preference('network.proxy_type',1)
			profile.set_preference('network.proxy.http',temp[0])
			profile.set_preference('network.proxy.http_port',temp[1])
			driver=webdriver.Firefox(firefox_profile=profile,firefox_options=fireFox_options)
			driver.get('http://twitch.tv/jokkizi')
			'''
		except Exception as error:
			print('Caught this error: ' + repr(error))
			flag=False
	drivers.append(driver)
	
time.sleep(3600)
