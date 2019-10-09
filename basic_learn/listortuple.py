#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:listortuple.py
# @Author: Feng
# @Date:2019/8/30
# @Desc:


li = []
tu = ()

print(li.__sizeof__())
print(tu.__sizeof__())



li = [1, 2, 3, 4]
tu = (1, 2, 3, 4)

print(li.__sizeof__())
print(tu.__sizeof__())

li.append(5)

print(li.__sizeof__())
print(tu.__sizeof__())
