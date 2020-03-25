from base64 import b64decode
from base64 import b64encode

sourece = ["www.huawei.com","www.juejie.im"]
code = ['d3d3Lmh1YXdlaS5jb20=','d3d3Lmp1ZWppZS5pbQ==','4oCLaHR0cDovL3Rvb2wubGl1bWluZ3llLmNuL211c2ljLw==',
        'aHR0cHM6Ly90YW9kYXhpYW5nLmNvbS9jcmVkaXQyCQk=','aHR0cDovL3dlbnNodS5jb3VydC5nb3YuY24vCgkJCQkJ','aHR0cHM6Ly9mbGlnaHQucXVuYXIuY29tCgkJCQkJ',
        'aHR0cDovL3NlbGxlci5jaHVjaHVqaWUuY29tL3NxZS5waHA/cz0vVXNlci9pbmRleA==']

# 编码
for c in sourece:
    str = b64encode(c.encode('utf8'))
    print(str)

# 解码
for c in code:
    str = b64decode(c).decode('utf8')
    print(str)