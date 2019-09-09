#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:encrypt_data.py
# @Author: Feng
# @Date:2019/8/9
# @Desc:

import hashlib

data = "5a6de3a9588bd021a5dd21b0acba8c86ae33e5c4c40c5f0a067e2b091c35d62e"
nounce = "30"

data = bytearray(data.encode())
md = hashlib.md5()
# md.update(data[0:len(data) - 1])
md.update(data)
sign_data = md.hexdigest()
print(sign_data, len(sign_data))

md = hashlib.md5()
nounce = bytearray(nounce.encode())
md.update(nounce)
sign_data = md.hexdigest()
print(sign_data, len(sign_data))

test_data = "db248656e311c958a227c270b0159fc81"
test_data = bytearray(test_data.encode())
md = hashlib.md5()
md.update(test_data)
sign_data = md.hexdigest()
print(sign_data, len(sign_data))

st = "gmdcdfsfds,1dfdsfdsfdsfds"
res = st.split(",")
print(st.find(','))
print(res)

s1 = "gmdcdfsfds"
if s1 in res:
    print("in")

s2 = "1dfdsfdsfdsfds"
if s2 in res:
    print("in")
