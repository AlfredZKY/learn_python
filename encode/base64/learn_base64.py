from base64 import b64decode
from base64 import b64encode

sourece = ["www.huawei.com","www.juejie.im"]
code = ['d3d3Lmh1YXdlaS5jb20=','d3d3Lmp1ZWppZS5pbQ==']

# 编码
for c in sourece:
    str = b64encode(c.encode('utf8'))
    print(str)

# 解码
for c in code:
    str = b64decode(c).decode('utf8')
    print(str)