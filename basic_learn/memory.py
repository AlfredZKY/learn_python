#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:memory.py
# @Author: Feng
# @Date:2019/9/9
# @Desc:


import sys

# 该方法用于获取一个对象的字节大小（bytes）
# 它只计算直接占用的内存，而不计算对象内所引用对象的内存

a = [1, 2]
b = [a, a]


def get_size():
    print(sys.getsizeof(a))  # 80
    print(sys.getsizeof(b))  # 80


def get_obj_size():
    # 排一下序：基础数字<空元组 < 空字符串 < 空列表 < 空集合 < 空字典。
    print(sys.getsizeof(""))  # 49
    print(sys.getsizeof([]))  # 64
    print(sys.getsizeof(()))  # 48
    print(sys.getsizeof(set()))  # 224
    print(sys.getsizeof(dict()))  # 240

    # 作为参照：
    print(sys.getsizeof(1))  # 28
    print(sys.getsizeof(True))  # 28


def get_allowed_mem():
    # 内存的扩充是不均匀的
    letters = "abcdefghijklmnopqrstuvwxyz"
    a = []
    b = set()
    c = dict()

    for i in letters:
        a.append(i)
        b.add(i)
        c[i] = i
        print(f'{len(a)},sys.getsizeof(a) = {sys.getsizeof(a)}', '\t'
              f'{len(b)},sys.getsizeof(b) = {sys.getsizeof(b)}', '\t' f'{len(c)},sys.getsizeof(c) = {sys.getsizeof(c)}')


# 静态创建对象
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5}
dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
list_1 = ['a', 'b']
list_2 = ['a', 'b', 'c']
list_3 = ['a', 'b', 'c', 'd']
list_4 = ['a', 'b', 'c', 'd', 'e']


def get_static_size():
    print(sys.getsizeof(set_1))  # 224
    print(sys.getsizeof(set_2))  # 736
    print(sys.getsizeof(dict_1))  # 240
    print(sys.getsizeof(dict_2))  # 368
    print(sys.getsizeof(list_1))  # 80
    print(sys.getsizeof(list_2))  # 88
    print(sys.getsizeof(list_3))  # 96
    print(sys.getsizeof(list_4))  # 104


def del_ele_size():
    a = [1, 2, 3, 4]
    print(sys.getsizeof(a))  # 初始值：96
    a.append(5)  # 扩充后：[1, 2, 3, 4, 5]
    print(sys.getsizeof(a))  # 扩充后：128
    a.pop()  # 缩减后：[1, 2, 3, 4]
    print(sys.getsizeof(a))  # 缩减后：128


def clear_obj_size():
    a = [1, 2, 3]
    b = {1, 2, 3}
    c = {'a': 1, 'b': 2, 'c': 3}

    print(sys.getsizeof(a))  # 88
    print(sys.getsizeof(b))  # 224
    print(sys.getsizeof(c))  # 240

    a.clear()  # 清空后：[]
    b.clear()  # 清空后：set()
    c.clear()  # 清空后：{}，也即 dict()
    print(sys.getsizeof(a))  # 64
    print(sys.getsizeof(b))  # 224
    print(sys.getsizeof(c))  # 72


if __name__ == '__main__':
    get_size()
    get_obj_size()
    get_allowed_mem()
    get_static_size()
    print("===================================")
    del_ele_size()
    print("===================================")
    clear_obj_size()
