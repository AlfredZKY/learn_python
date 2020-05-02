 # 
 # Created by preference on 2020/05/02
 # Author: AlfredZKY
 # Files:session_cookies.py
 # WorkPlace:learn_python
 # 




import requests

from urllib.parse import urljoin

# 祛除报警信息
requests.packages.urllib3.disable_warnings()

BASE_URL = 'https://login2.scrape.cuiqingcai.com/ '
LOGIN_URL=urljoin(BASE_URL,'/login')
INDEX_URL = urljoin(BASE_URL,'/page/1')

USERNAME='admin'
PASSWORD='admin'


response_login = requests.post(LOGIN_URL,data={
    'username':USERNAME,
    'password':PASSWORD
},allow_redirects=False,verify=False)

cookies = response_login.cookies
print('Cookies',cookies)

response_index = requests.get(INDEX_URL,cookies=cookies,verify=False)
print('Response Status',response_index.status_code)
print('Response URL',response_index.url)
print('Sopurce code',response_index.content)