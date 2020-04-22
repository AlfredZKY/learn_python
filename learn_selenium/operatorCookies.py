import time
from selenium import webdriver
browser = webdriver.Chrome()

url1 = "https://www.baidu.com"
url2 = "https://www.taobao.com"
url3 = "https://www.python.org"

browser.get(url1)
browser.get(url2)
browser.get(url3)

browser.back()
time.sleep(1)
browser.forward()
# browser.close()

# Cookies 
# 使用selenium还可以方便对Cookies进行操作，例如获取，添加，删除Cookies等
url4 = "https://www.zhihu.com/explore"
browser.get(url4)
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

