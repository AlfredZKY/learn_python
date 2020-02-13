#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_creator.py
# @Author: Feng
# @Date:2019/8/23
# @Desc:

import psutil
import os
params = [1234, '1234', [1, 2, 3, 4, 5], set(
    [1, 2, 3, 4]), {1: 1, 2: 2, 3: 3, 4: 4}, (1, 2, 3, 4)]


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


for param in params:
    pass
    # print('{} is iterable? {}'.format(param, is_iterable(param)))


def show_memory_info(hint):
    pass
    # pid = os.getpgid()
    # p = psutil.Process(pid)
    # info = p.memory_full_info()
    # memory = info.uss / 1024. / 1024
    # print('{} memory used:{}MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    # print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = [i for i in range(100000000)]
    show_memory_info('after generator initiated')
    # print(sum(list_2))
    show_memory_info('after sum called')


def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


gen_1 = generator(1)
gen_3 = generator(3)

# print(gen_1)
# print(gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        # print('next_1 = {},next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
        # print('sum_1 = {},sum_3 = {}'.format(sum_1, sum_3))
    # print(sum_1 * sum_1, sum_3)


def suqare(n):
    for i in range(n):
        yield i ** 2


if __name__=='__main__':
    for i in suqare(8):
        print(i)