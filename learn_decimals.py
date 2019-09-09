#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_decimals.py
# @Author: Feng
# @Date:2019/8/5
# @Desc:


# 小数点后取2位(四舍五入)的方法 round函数有缺陷，尽量不采用
a = 1.23456
b = 2.35
c = 3.5
d = 2.5

print(round(a, 3))
print(round(b, 2))
print(round(c))
print(round(d))
print("--------------------------------------")

# 使用print格式化输出
f = 1.23456
st = "%.4f" % f
print(st)

print("%.4f" % f)
print("%.3f" % f)
print("%.2f" % f)

res = "%.4f" % f
print(type(res))


print("--------------------------------------")
# decimal函数 看结果也是有时进位，有时不进位，不推荐使用
from decimal import Decimal

aa = Decimal('5.026').quantize(Decimal('0.00'))
bb = Decimal('3.555').quantize(Decimal('0.00'))
cc = Decimal('3.545').quantize(Decimal('0.00'))
print(aa)
print(bb)
print(cc)
