import requests


proxy = '127.0.0.1:1087'
url = 'https://httpbin.org/get'
# socks 代理同理scoks5,且需要安装另外一个包 requests[scoks] pip install "requests[scoks]"
proxies ={
    'http':'http://' + proxy,
    'https':'https://'+proxy
}



try:
    response = requests.get(url,proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)