# 使用selenium 获取网页中的节点的属性，方法，文本，框架

from selenium import webdriver
browser = webdriver.Chrome()

url = 'https://dynamic2.scrape.cuiqingcai.com/'
browser.get(url)

# 获取节点属性 logo class="logo-image"
logo = browser.find_element_by_class_name('logo-image')
print(logo)
print(logo.get_attribute('src'))

# 获取文本值 class="logo-title"
input = browser.find_element_by_class_name('logo-title')
print(input.text)


# 获取ID，位置，标签名，大小
input = browser.find_element_by_class_name('logo-title')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

# 切换Frame
# 网页中有一种节点叫做iframe,也就是子Frame，相当于页面的子页面，它的结构和外部网页的结构完全一致，selenium打开页面后，默认是在父级Frame里操作
# 而此时如果页面中还有子Frame，selenium是不能获取到子Frame里面的节点，这时就需要使用switch_to.frame方法来切换Frame。

import time
from selenium.common.exceptions import NoSuchElementException

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)