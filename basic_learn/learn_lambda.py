#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_lambda.py
# @Author: Feng
# @Date:2019/8/7
# @Desc:
import sys
import random

# 1.lambda 是一个表达式，并不是一个语句
#   所谓表达式就是用一系列公式去表达一个东西，例如 x+2、x**2
#   所谓语句，则是完成了一定的功能，比如符合赋值，打印操作。
# 2.匿名函数的主体只能是一行简单的表达式，而不能扩展成多行的代码块

# 优点：
# 1.减少代码的重复性
# 2.模块化代码


def square(x): return x ** 2


print(square(3))

# 匿名函数可以用在常规函数不能用的地方，比如列表生成式中
print([(lambda x: x * x)(x) for x in range(10)])

# 匿名函数可以用在某些函数的参数中，比如排序函数中,根据第二个元素进行排序。
l1 = [(1, 20), (3, 0), (9, 10), (2, -1)]
l1.sort(key=lambda x: x[1])
print(l1)

# 根据第一个元素进行排序操作
l1.sort(key=lambda x: x[0])
print(l1)

suqqred = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
for item in suqqred:
    print(item)

d = {'mike': 10, 'lucy': 2, 'ben': 30}

for kv in d.items():
    print(kv)

# 排完序后，类型以改变成了list
new_dic = sorted(d.items(), key=lambda x: x[1])
print(type(new_dic))
for item in new_dic:
    print(item[0], item[1])

# 打印出模块所在的位置
print(random.__file__)
