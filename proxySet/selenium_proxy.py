from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait


proxy = '127.0.0.1:1087'
url = 'https://httpbin.org/get'

# socks 代理同理scoks5,且需要安装另外一个包 requests[scoks] pip install "requests[scoks]"
proxies ={
    'http':'http://' + proxy,
    'https':'https://'+proxy
}

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(options=options)
browser.get(url)
print(browser.page_source[:1000])
browser.close()
