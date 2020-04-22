from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.taobao.com")

#print(browser.page_source)

# 查找单节点
# id="q"  name="q"
# 通过selenium 对淘宝框搜索节点，先拿到搜索框的节点
input_first = browser.find_elements_by_id("q")
input_second = browser.find_elements_by_css_selector("#q")
input_third = browser.find_elements_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)

# 同上 通用办法 find_element
input_four = browser.find_element(By.ID,'q')
print(input_four)
print('--------------------------------------')
# 查找多节点 class="service-bd" li标签
#lis = browser.find_elements_by_css_selector('.service-bd li')
lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')

print(lis)

# 节点交互 selenium可以驱动浏览器来执行一些操作，或者说可以让浏览器模拟执行一些操作，比较常见的用法：
# 1.输入文字时用send_keys方法，清空文字时用clear方法，点击按钮时用click方法。
# 打开淘宝，输入iPhone 然后清空，输入iPad，清空，点击button按钮
import time
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)

input.clear()
input.send_keys('iPad')
input.clear()
button = browser.find_element_by_class_name('btn-search')
button.click()

browser.close()


