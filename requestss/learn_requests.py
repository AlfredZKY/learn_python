import requests

url1 = 'http://httpbin.org/get'
url2 = 'https://static1.scrape.cuiqingcai.com/'
url3 = 'http://httpbin.org/get?name=germey&age=25'

data = {
    'name':'germey',
    'age':25
}


r = requests.get(url1,params=data)
# print(r.text)

import re

r = requests.get(url2)
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)
# print(titles)
# print(r.content)


r = requests.get('https://github.com/favicon.ico')
with open('/Volumes/mac_store/project/learn_python/requestss/favicon.ico','wb') as f:
    f.write(r.content)


data = {'name':'germey','age':25}
r = requests.post("http://httpbin.org/post",data=data)
# print(r.text)

# 这里我们首先调用cookies属性即可成功得到Cookies，可以发现它是RequestCookieJar类型。然后用items方法将其转化为元组组成的列表，遍历输出每一个Cookie...
r = requests.get("http://www.baidu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)


cookies = '''_ga=GA1.2.773314249.1586595978; _octo=GH1.1.601185704.1586596090; tz=Asia%2FShanghai; _device_id=94cb8a1c78f5880e6ec2b011608acc19; _gat=1; has_recent_activity=1; user_session=ViJ1c1_s5fXGVhsu9YIYJ-0FnGoEI7EfOyejhTOUJlvtNIiO; __Host-user_session_same_site=ViJ1c1_s5fXGVhsu9YIYJ-0FnGoEI7EfOyejhTOUJlvtNIiO; logged_in=yes; dotcom_user=AlfredZKY; _gh_sess=k3lgA1Cg0OMJhioud%2FvNIP2ZP8uRTToeOGKDH1rOkTuvN91%2FGf1G5JSDlGpYup21fsscVYPhKpD3gfMwp4x20xQso%2FKxu%2BsdALwWIwXpNKN7Q0LbC%2F01z7Uc9objQeU8nC9swnT0j%2B3fVSMVOeXrMZt%2FhjJmrVakIpq8TDNhsEnoKwhrFKQw7urRPMLMQJ%2BEiyJJomxAThqTtO20tonLOvMkqDYnL3D0JGiws3Wk5jzhGGu1l5mi6UlwXibLGnMgpBGCgBALR1uzMD3hND%2FFn9k59mk8QS32xryXKV3RYGGq8nZKqmUjV20RGJmdumnjoqUI1DE2fP00qS2tSiZMASy7e8a8L98cdWlpca5O2KN%2BuxmG5WGqWzKjlUdWvlviNKE5pkLXi5cwA%2F7RJyW5VSHWYmRo7xKxmcFUgDuoBPIheTBpC%2BWebr3NBJtDsBMBOR90XPrcQNklFrjME5M8%2FAfnNT6llrCwb2RQSf%2Fe9zgXtZRgnrm2BAAp9obEsNeVdejm5A83nTKC5uAoZUqie2b%2BmMZkiHSkK6MKqISONlMJD55JOirsBxQXkCmsLN0X%2Fkj8eR3G59MBoPAPMKFSEBeHDFGLbXeb4eO5kYXbfe127cFIg0LBSsQCp7zB6748Xu5%2Fw%2FRktArkAhC3JWq5p6JrSXWhT9U%2B2sA8U7xu9c3zvDrqfO%2Bj%2BgZwYIvHtu%2FVsI27X54GmXVwUPU44xtkOvtkDYdRD6K521eOO3875l4LcGWiUAG8pKCJzMUq98K1y4Sdno50tXptbM262HbdlkhlNixSbL1Oj3XTWiLNrgAbXsJ9dz1LkAKJs1X%2BzMwrr0pkOOplGL9rnWlDwUA2FpxQn%2FKTDPlwi%2BmUOhPmH7KDbMuQi9y337RFQlIXGSD52f%2BQwlnxaHYM8VtuNzCTFou5VN8xb%2FmK6IvqqLbc0YlUWXmRynP%2FVvMgSEruDd0hDli%2Bu8%2BhT41jhOac1aWdcpkXImw4aZu8d3OlRauC%2BQK2GZj555bgmM4vxHZiz%2BYpos2B2SEwXaFLP1tFj4ZXGBOMEuUR4OEXiIGvOqk4rLW5UleCOawXgB4iUH32iSCZPxqqzE0XEp2APtXUDaVw%2B8CW3aNAZqhrDwsVrHijVSI1liwhWLblSsyU535WwVnwOZrxS6jh1WDA2VFITPz56nHnZQfwmSJEvjIWcRa4NnTP7vaeky6%2F5jY8%2FFQviaSC2NT%2Bg34%2FgbRudYgT0obgfsAmBJRKtHEDPN6efrhS1c%2BcMvB%2FCuwwIICoN5fZ1clSMUYtaAr%2BbFMY3y%2F5KdQbhovW%2FaMm2hPO85MddWsZ8F3iV2niDOcpN1g2Y6rbjFLtMZPIpM8IzoIiOwOlk%2FRmYp06%2BE83dqrPYnhBmjEY3azqr920PYIgdXUfyhyRBlOfQL90qvnm0JC01%2FPI6babPRlvys2InSiop8%2BOtazGK2D28wxbNMC7YU1LDAiqaU%2F8GzmAQ6ZS85gViB2wsLUZMHDxaguOuLKaox78koiCtYLkUd%2F2xDk7GyQKCr8%3D--PF3sRgHRBMNIoO7e--U4u7aBZmoQYsVp5MkMm%2FYQ%3D%3D'''
jar = requests.cookies.RequestsCookieJar()

headers = {
    #"Cookie": "_ga=GA1.2.773314249.1586595978; _octo=GH1.1.601185704.1586596090; tz=Asia%2FShanghai; _device_id=94cb8a1c78f5880e6ec2b011608acc19; _gat=1; has_recent_activity=1; user_session=ViJ1c1_s5fXGVhsu9YIYJ-0FnGoEI7EfOyejhTOUJlvtNIiO; __Host-user_session_same_site=ViJ1c1_s5fXGVhsu9YIYJ-0FnGoEI7EfOyejhTOUJlvtNIiO; logged_in=yes; dotcom_user=AlfredZKY; _gh_sess=k3lgA1Cg0OMJhioud%2FvNIP2ZP8uRTToeOGKDH1rOkTuvN91%2FGf1G5JSDlGpYup21fsscVYPhKpD3gfMwp4x20xQso%2FKxu%2BsdALwWIwXpNKN7Q0LbC%2F01z7Uc9objQeU8nC9swnT0j%2B3fVSMVOeXrMZt%2FhjJmrVakIpq8TDNhsEnoKwhrFKQw7urRPMLMQJ%2BEiyJJomxAThqTtO20tonLOvMkqDYnL3D0JGiws3Wk5jzhGGu1l5mi6UlwXibLGnMgpBGCgBALR1uzMD3hND%2FFn9k59mk8QS32xryXKV3RYGGq8nZKqmUjV20RGJmdumnjoqUI1DE2fP00qS2tSiZMASy7e8a8L98cdWlpca5O2KN%2BuxmG5WGqWzKjlUdWvlviNKE5pkLXi5cwA%2F7RJyW5VSHWYmRo7xKxmcFUgDuoBPIheTBpC%2BWebr3NBJtDsBMBOR90XPrcQNklFrjME5M8%2FAfnNT6llrCwb2RQSf%2Fe9zgXtZRgnrm2BAAp9obEsNeVdejm5A83nTKC5uAoZUqie2b%2BmMZkiHSkK6MKqISONlMJD55JOirsBxQXkCmsLN0X%2Fkj8eR3G59MBoPAPMKFSEBeHDFGLbXeb4eO5kYXbfe127cFIg0LBSsQCp7zB6748Xu5%2Fw%2FRktArkAhC3JWq5p6JrSXWhT9U%2B2sA8U7xu9c3zvDrqfO%2Bj%2BgZwYIvHtu%2FVsI27X54GmXVwUPU44xtkOvtkDYdRD6K521eOO3875l4LcGWiUAG8pKCJzMUq98K1y4Sdno50tXptbM262HbdlkhlNixSbL1Oj3XTWiLNrgAbXsJ9dz1LkAKJs1X%2BzMwrr0pkOOplGL9rnWlDwUA2FpxQn%2FKTDPlwi%2BmUOhPmH7KDbMuQi9y337RFQlIXGSD52f%2BQwlnxaHYM8VtuNzCTFou5VN8xb%2FmK6IvqqLbc0YlUWXmRynP%2FVvMgSEruDd0hDli%2Bu8%2BhT41jhOac1aWdcpkXImw4aZu8d3OlRauC%2BQK2GZj555bgmM4vxHZiz%2BYpos2B2SEwXaFLP1tFj4ZXGBOMEuUR4OEXiIGvOqk4rLW5UleCOawXgB4iUH32iSCZPxqqzE0XEp2APtXUDaVw%2B8CW3aNAZqhrDwsVrHijVSI1liwhWLblSsyU535WwVnwOZrxS6jh1WDA2VFITPz56nHnZQfwmSJEvjIWcRa4NnTP7vaeky6%2F5jY8%2FFQviaSC2NT%2Bg34%2FgbRudYgT0obgfsAmBJRKtHEDPN6efrhS1c%2BcMvB%2FCuwwIICoN5fZ1clSMUYtaAr%2BbFMY3y%2F5KdQbhovW%2FaMm2hPO85MddWsZ8F3iV2niDOcpN1g2Y6rbjFLtMZPIpM8IzoIiOwOlk%2FRmYp06%2BE83dqrPYnhBmjEY3azqr920PYIgdXUfyhyRBlOfQL90qvnm0JC01%2FPI6babPRlvys2InSiop8%2BOtazGK2D28wxbNMC7YU1LDAiqaU%2F8GzmAQ6ZS85gViB2wsLUZMHDxaguOuLKaox78koiCtYLkUd%2F2xDk7GyQKCr8%3D--PF3sRgHRBMNIoO7e--U4u7aBZmoQYsVp5MkMm%2FYQ%3D%3D",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}

for cookie in cookies.split(';'):
    key,value = cookie.split('=',1)
    jar.set(key,value)

r = requests.get("https://github.com/",cookies=jar,headers=headers)
# print(r.text)

# 设想这样一个场景，第一个请求利用post方法登录了某个网站，第二次想获取成功登录后的自己的个人信息，你又用了一次get方法去请求个人信息页面。
# 实际上，这相当于打开了两个浏览器，是两个完全不相关的 Session，能成功获取个人信息吗？当然不能
requests.get("http://httpbin.org/cookies/set/number/123456789")
r = requests.get("http://httpbin.org/cookies")
print(r.text)

# 采用Session
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)


# 忽略证书的验证,且忽略下面的警告
# InsecureRequestWarning: Unverified HTTPS request is being made to host 'static2.scrape.cuiqingcai.com'. Adding certificate verification is strongly advised. 
# See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# InsecureRequestWarning,
from requests.packages import urllib3
urllib3.disable_warnings()
url11 = 'https://static2.scrape.cuiqingcai.com/'
response = requests.get(url11,verify=False)
print(response.status_code)


# 超时设置 timeo=seconds 或者None

# 身份认证，如果遇到身份认证这种情况Authentication它是一种用来允许网页浏览器或者其他客户端程序在请求时提供用户名和口令形式的身份凭证的一种登录验证方式
from requests.auth import HTTPBasicAuth
url12 = 'https://static3.scrape.cuiqingcai.com/'
# r = requests.get(url12,auth=HTTPBasicAuth('admin','admin'))
r = requests.get(url12,auth=('admin','admin'))
print(r.status_code)

