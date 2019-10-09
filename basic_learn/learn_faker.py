#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_faker.py
# @Author: Feng
# @Date:2019/8/9
# @Desc:

from faker import Faker

# 实例化一个对象
faker = Faker()

# 简体中文：zh_CN
# 繁体中文：zh_TW
# 美国英文：en_US
# 英国英文：en_GB
# 德文：de_DE
# 日文：ja_JP
# 韩文：ko_KR
# 法文：fr_FR

# 实例化一个支持国家语言的对象
faker = Faker('zh_CN')

print('name:', faker.name())
print('address:', faker.address())
print('text:', faker.text())

print(faker.providers)
print('name:', faker.name)
print('address:', faker.address)
print('text:', faker.text)



