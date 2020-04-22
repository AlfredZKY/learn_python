# 在selenium中个方法会在网页框架加载完成后结束执行，此时如果获取page_source，可能并不能在浏览器完全加载完成的页面，如果某些页面有额外的Ajax请求
# 我们在网页源码中也不一定能成功获取到，所以这里需要延时等待一定时间，确保节点已经加载出来
# 等待的方式有两种:一种是隐式等待， 一种是显式等待

from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://dynamic2.scrape.cuiqingcai.com/'


# 隐式等待 这里使用implicitly_wait 方法实现了隐式等待 如果selenium没有在DOM中找到节点，将继续等待，超出设定时间后，则抛出找不到节点的异常
# 换句话说，隐式等待可以在我们查找节点而节点并没有立即出现的时候，等待一段时间灾查找DOM，默认时间是0
browser.implicitly_wait(10)
browser.get(url)
input = browser.find_element_by_class_name('logo-image')
print(input)


# 显式等待
# 隐式等待的效果其实并没有那么好，因为我们只规定了一个固定时间，而页面的加载时间会受到网络条件的影响
# 这里还有一种更合适的显式等待方法，它指定要查找的节点，然后指定一个最长等待时间，如果在规定时间内加载出来了这个节点，就返回查找的节点，如果到了
# 规定时间依然没有加载出该节点，则抛出超时异常
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

url = 'https://www.taobao.com/'
browser.get(url)

# 指定最长等待时间
wait = WebDriverWait(browser,10)

# until 传入要等待的条件 expected_conditions 
# presence_of_element_located 代表节点出现
input = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)