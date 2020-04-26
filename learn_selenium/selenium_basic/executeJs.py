# 执行JavaScript selenium API 并没有提供实现某些方法，比如，下拉进度条，但它可以直接模拟运行JavaScript，此时使用execute_script()实现

from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alter(To Bottom)')

browser.close()