#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_decorator.py
# @Author: Feng
# @Date:2019/8/8
# @Desc:

import functools


def func(message):
    # print('Got a message :{}'.format(message))
    return 'Got a message :{0}'.format(message)


def root_call(func, message):
    print(func(message))


# send_message = func
#
# send_message('hello world')

root_call(func, 'hello world')

print("***************************************************")


def func1(message):
    def get_message(message):
        print('Got a message :{}'.format(message))

    return get_message(message)


func1('hello world')


def func_closure():
    def get_message(message):
        print('Got a message :{}'.format(message))

    return get_message


send_message = func_closure()
send_message('hello world')


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


# @称为语法糖。
@my_decorator
def greet(message):
    print(message)


# greet = my_decorator(greet)
greet('hello world')

print('---------------------------------------------')


def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(2)
def greet(message):
    print(message)


greet('hello world')

# 改变了元信息，被wrapper函数所取代，如果不想改变元信息，可以使用内置装饰器@functools.wrap，它会帮助保留原函数的元信息
# (也就是原函数的元信息，拷贝到对应的装饰器函数里)
print(greet.__name__)
help(greet)
print('---------------------------------------------')


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        print('my_decorator')
        func(*args, **kwargs)

    return wrapper


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        print('my_decorator1')
        func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator
def greet(message):
    print(message)


greet('hello world')

print(greet.__name__)


# 通过装饰器修改被装饰的函数的参数以及，被修饰的函数返回值
def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("==================================")
        new_args = [args[0] + 100, args[1] + 100]
        res = func(*tuple(new_args), **kwargs)
        return res
    return wrapper


a, b = 3, 5


@my_decorator3
def is_max(a, b):
    if a > b:
        return a
    else:
        return b


res = is_max(a, b)
print(res)
