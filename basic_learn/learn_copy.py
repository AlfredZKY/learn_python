#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File:learn_copy.py
# @Author: Feng
# @Date:2019/8/6
# @Desc:

import copy

a = '1'
b = '1'
# 比较的是两个对象的值相等，还是两个对象完全相等

if a == b:
    print("ok")
else:
    print("no")

# l2 是l1的拷贝,深拷贝还是浅拷贝
l1 = [1, 2, 3]
l2 = list(l1)
l2[2] = 11
print(l1, l2)

# '==' vs 'is' ==操作符比较对象之间的值是够相等
# is 操作符比较的是对象的身份标识是否相等，即它们是否是同一个对象，是否指向同一个内存地址
if a == b:
    print("ok")

a = 10
b = 10
if a == b:
    print("a==b")

# 在python 中每个对象的身份标识，都能通过函数id(object)获得，因此is操作符相当于比较对象之间的ID是否相等
print(id(a))
print(id(b))

print(a is b)

c = 257
d = 257

# 在python 中每个对象的身份标识，都能通过函数id(object)获得，因此is操作符相当于比较对象之间的ID是否相等
# Python 内部会对 -5 到 256 的整型维持一个数组,起到一个缓存的作用。 在python源码中可以看到。
# 所以当你试图创建一个-5到256范围内的整型数字时，Python都会从这个数组中返回相对应的引用，而不是重新开辟一块新的内存空间
# 通过命令行测试，这个比较结果是false,pycharm IDE可能做了优化，返回了True
print(id(c))
print(id(d))
print(c is d)

# is 主要用于判断一个变量是否为None
# is的效率是高于==操作符的，因为is不能重载，而==操作符却不同，执行a==b相当于去执行a.__eq__(b),而Python大部分的数据
# 类型都会重载__eq__这个函数，递归地遍历对象所有值，并逐一比较
# is通常被用于检查一个变量是否是None
if a is not None:
    print(a)

# 元组虽然是不可变的，但是元组是可以嵌套的，它里面的元素可以是可变的。
t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])

print(t1 == t2)
t1[-1].append(5)
print(t1 == t2)

# 深拷贝和浅拷贝
l1 = [1, 2, 3]
l2 = list(l1)

print(l1, l2)
print(l1 == l2)
print(l1 is l2)

s1 = set([1, 2, 3])
s2 = set(s1)
print(s2)
print(s1 == s2)
print(s1 is s2)

# 可以看出以上都是浅拷贝
# 当然对于可变的序列，我们还可以通过切片操作符':'完成浅拷贝
l3 = l1[:]
print(l3 == l1)
print(l3 is l1)

# python 提供了相对应的函数copy.copy()适用于任何数据类型
l4 = copy.copy(l1)

# 对于元组使用tuple()或者切片操作符":",不会创建一份浅拷贝，相反它会返回一个指向相同元祖的引用。
# 这里元组只被创建一次，t1和t2同时指向这个元组
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 == t2)
print(t1 is t2)

# 浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是是原对象中子对象的引用
# 因此，如果原对象中的元素不可变，那倒无所谓;但如果元素可变，浅拷贝通常会带来一些副作用，尤其需要注意
# 对于浅拷贝，会共同指向同一个列表，但元组不可变，会重新创建一个新的元组，会指向不同的地址。
l1 = [[1, 2], (30, 40)]
l2 = list(l1)

print(id(l1))
print(id(l2))
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)
l1[1] += (50, 60)
print(l1)
print(l2)

# 通过上述案例，可以了解到，浅拷贝会影响我们的对象，如果想要避免这种副作用
# 完整的拷贝一个对象，就需要用深拷贝。
# 深拷贝，所谓深度拷贝，是指重新分配一块内存，创建一个对象，并且将原对象中的元素，已递归的方式，
# 通过创建新的子对象拷贝到新对象中。
l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)

print(id(l1))
print(id(l2))
print(l1)
print(l2)
l1.append(100)
l1[0].append(3)
print(l1)
print(l2)

# 当列表指向自身的引用时，会产生一个无限嵌套的列表，测试之后，发现没有出现stack overflow
# 因为深度拷贝函数会维护一个字典，记录已经拷贝的对象及其ID,拷贝过程中，如果字典里已经存储了
# 将要拷贝的对象，则会从字典直接返回
x = [1]
x.append(x)
print(x)

y = copy.deepcopy(x)
print(y)

print(x == y)
print("------------------------------------")
