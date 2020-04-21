from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

br = webdriver.Chrome()

br.get("https://www.baidu.com")

first = br.find_element_by_link_text("设置")
ActionChains(br).move_to_element(first).perform()
menu = br.find_element_by_link_text("搜索设置")
menu.click()