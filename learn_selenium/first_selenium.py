from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

# 声明浏览器对象
brower = webdriver.Chrome()

try:
    # 访问网址
    brower.get("https://www.baidu.com")
    input = brower.find_element_by_id('kw')

    # 输入关键字
    input.send_keys('Python')

    # 回车
    input.send_keys(Keys.ENTER)

    # 显式等待
    wait = WebDriverWait(brower,10)

    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(brower.current_url)
    print(brower.get_cookies())

    # 返回网页源代码
    print(brower.page_source)
    
finally:
    brower.close()


