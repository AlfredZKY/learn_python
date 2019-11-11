'''
Python 中使用协程最常用的库莫过于 asyncio，所以本文会以 asyncio 为基础来介绍协程的使用。

首先我们需要了解下面几个概念：

event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足条件发生的时候，就会调用对应的处理方法。

coroutine：中文翻译叫协程，在 Python 中常指代为协程对象类型，我们可以将协程对象注册到时间循环中，它会被事件循环调用。我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。

task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

future：代表将来执行或没有执行的任务的结果，实际上和 task 没有本质区别。

另外我们还需要了解 async/await 关键字，它是从 Python 3.5 才出现的，专门用于定义协程。其中，async 定义一个协程，await 用来挂起阻塞方法的执行。
'''

import asyncio
import requests
import time
import aiohttp

async def execute(x):
    print('Number:',x)
    return x

# 返回一个协程对象
coroutine = execute(1)

print('Coroutine:',coroutine)
print('After calling execute')

def create_loop():
    # 创建了一个事件循环loop
    loop = asyncio.get_event_loop()

    task = loop.create_task(coroutine)
    print('Task:',task)

    # 将协程对象注册到事件循环中
    loop.run_until_complete(task)
    print('Task:',task)
    print('After calling loop')

def create_no_loop():
    task = asyncio.ensure_future(coroutine)
    print('Task:',task)

    loop = asyncio.get_event_loop()
    # 将协程对象注册到事件循环中
    loop.run_until_complete(task)
    print('Task:',task)
    print('After calling loop')

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result

async def request():
    # url = 'https://www.baidu.com'
    url = 'http://127.0.0.1:5000'
    print('Waiting for',url)
    response = await get(url)
    print('Get response from',url,'Result:',response)

def callback(task):
    print('Status:',task.result())

def bind_callback():
    coroutine = request()
    task = asyncio.ensure_future(coroutine)
    task.add_done_callback(callback)
    print('Task:',task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    print('Task:',task)

def no_bind_callback():
    coroutine = request()
    task = asyncio.ensure_future(coroutine)
    # task.add_done_callback(callback)
    print('Task:',task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    print('Task Result:',task.result())

def multi_task():
    start = time.time()

    tasks = [asyncio.ensure_future(request()) for _ in range(5)]
    print('Tasks:',tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print('Task Result:',task.result())
    end = time.time()

    print('Cost time:',end-start)

if __name__ == '__main__':
    # create_loop()
    # create_no_loop()
    # bind_callback()
    # no_bind_callback()
    multi_task()