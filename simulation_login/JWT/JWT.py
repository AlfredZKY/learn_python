 # 
 # Created by preference on 2020/05/02
 # Author: AlfredZKY
 # Files:JWT.py
 # WorkPlace:learn_python
 # 

import requests
from urllib.parse import urljoin


requests.packages.urllib3.disable_warnings()

BASE_URL = 'https://login3.scrape.cuiqingcai.com/login'
LOGIN_URL = urljoin(BASE_URL,'/api/login')
INDEX_URL =urljoin(BASE_URL,'/api/book')


USERNAME = 'admin'
PASSWORD = 'admin'

response_login = requests.post(LOGIN_URL,data={
    'username':USERNAME,
    'password':PASSWORD
},allow_redirects=False,verify=False)

data = response_login.json()
print('Response JSON',data)

jwt = data.get('token')
print('JWT',jwt)

headers = {
    'Authorization':f'jwt {jwt}'
}

response_index = requests.get(INDEX_URL,params={
    'limit':18,
    'offset':0
},headers=headers,verify=False)
print('Response Status',response_index.status_code)
print('Response URL',response_index.url)
print('Response Data',response_index.json())

