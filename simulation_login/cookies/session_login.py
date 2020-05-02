 # 
 # Created by preference on 2020/05/02
 # Author: AlfredZKY
 # Files:session_login.py
 # WorkPlace:learn_python
 # 


import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.cuiqingcai.com/login'
LOGIN_URL = urljoin(BASE_URL,'/login')
INDEX_URL = urljoin(BASE_URL,'/page/1')

USERNAME = 'admin'
PASSWORD = 'admin'

requests.packages.urllib3.disable_warnings()

session = requests.Session()

response_login = session.post(LOGIN_URL,data={
    'username':USERNAME,
    'password':PASSWORD
},verify=False)

cookies = response_login.cookies
print('Cookies:',cookies)
response_index = session.get(INDEX_URL)
print('Response Status',response_index.status_code)
print('Response URL',response_index.url)



