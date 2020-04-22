# 使用selenium执行动作链
# 一些交互动作都是针对某个节点执行的，比如，对于输入框，我们调用它的输入文字和清空文字；对于按钮，我们调用它的点击方法。其实还有另外一些操作
# 他们没有特定的执行对象，比如鼠标的拖拽，键盘按键等，这些动作用另一种方式来执行，那就是动作链。

from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()

url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)

# id="iframeResult"
browser.switch_to.frame('iframeResult')

# 查找到要滑动的滑块
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')

actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()

browser.close()
browser.quit()
