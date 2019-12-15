#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:useprofile.py
# @Author: Feng
# @Date:2019/7/19
# @Desc:

# 建议使用，调用了C扩展
import cProfile
# 纯python 增大了开销
import profile
import re
from functools import wraps


# cProfile.run('re.compile("foo|bar")')
# pr = profile.Profile()
# for i in range(5):
#     print(pr.calibrate(10000))

def memoize(f):
    memo = {}
    # @wraps(f)

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n - 1))
    res.append(fib(n))
    return res


# print(fib_seq(30))
cProfile.run('fib_seq(30)')
