 # 
 # Created by preference on 2020/05/02
 # Author: AlfredZKY
 # Files:selenium_login.py
 # WorkPlace:learn_python
 # 

from urllib.parse import urljoin

from selenium import webdriver

import requests
import time 


BASE_URL = 'https://login2.scrape.cuiqingcai.com/login'
LOGIN_URL = urljoin(BASE_URL,'/login')
INDEX_URL = urljoin(BASE_URL,'/page/1')

USERNAME='admin'
PASSWORD='admin'

# 祛除Chrome的ssl证书检测
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(chrome_options=options)


# browser = webdriver.Chrome()
browser.get(BASE_URL)
browser.find_element_by_css_selector('input[name="username"]').send_keys(USERNAME)
browser.find_element_by_css_selector('input[name="password"]').send_keys(PASSWORD)
browser.find_element_by_css_selector('input[type="submit"]').click()

time.sleep(10)

requests.packages.urllib3.disable_warnings()

# get cookies from selenuim
cookies = browser.get_cookies()
print('Cookies:',cookies)
browser.close()

# set cookies to requests
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'],cookie['value'])

response_index = session.get(INDEX_URL,verify=False)
print('Response Status',response_index.status_code)
print('Response URL',response_index.url)


