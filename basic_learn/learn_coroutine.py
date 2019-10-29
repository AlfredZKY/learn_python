#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_coroutine.py
# @Author: Feng
# @Date:2019/8/29
# @Desc:

import time


# def consumer():
#     r = ""
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         time.sleep(1)
#         r = "200 OK"
#
#
# def produce(c):
#     c.next()
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consuming %s...' % r)
#     c.close()

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(c):
    c.__next__()
    n = 0
    while n < 15:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
