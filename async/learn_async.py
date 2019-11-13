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
import multiprocessing
from aiomultiprocess import Pool

async def execute(x):
    print('Number:',x)
    return x

# # 返回一个协程对象
# coroutine = execute(1)

# print('Coroutine:',coroutine)
# print('After calling execute')

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

# 开始运行时，时间循环会运行第一个 task，针对第一个 task 来说，当执行到第一个 await 跟着的 get() 方法时，
# 它被挂起，但这个 get() 方法第一步的执行是非阻塞的，挂起之后立马被唤醒，所以立即又进入执行，
# 创建了 ClientSession 对象，接着遇到了第二个 await，调用了 session.get() 请求方法，然后就被挂起了，
# 由于请求需要耗时很久，所以一直没有被唤醒，好第一个 task 被挂起了，那接下来该怎么办呢？
# 事件循环会寻找当前未被挂起的协程继续执行，于是就转而执行第二个 task 了，也是一样的流程操作，
# 直到执行了第五个 task 的 session.get() 方法之后，全部的 task 都被挂起了。所有 task 都已经处于挂起状态，
# 那咋办？只好等待了。3 秒之后，几个请求几乎同时都有了响应，然后几个 task 也被唤醒接着执行，输出请求结果，
# 最后耗时，3 秒！

def multi_task():
    start = time.time()

    tasks = [asyncio.ensure_future(request()) for _ in range(100)]
    # print('Tasks:',tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    # for task in tasks:
    #     print('Task Result:',task.result())

    end = time.time()
    print('Cost time:',end-start)

def process_one():
    start = time.time()
    def request():
        url = 'http://127.0.0.1:5000'
        print('Waiting for',url)
        response = requests.get(url).text
        print('Get response from',url,'Result:',response)

    for _ in range(100):
        request()

    end = time.time()
    print('Cost time:',end-start)

def new_request(_):
        url = 'http://127.0.0.1:5000'
        print('Waiting for',url)
        response = requests.get(url).text
        print('Get response from',url,'Result:',response)

def process_multi():
    start = time.time()
    cpu_count = multiprocessing.cpu_count()
    print('Cpu count:',cpu_count)
    pool = multiprocessing.Pool(cpu_count)
    pool.map(new_request,range(100))

    end = time.time()
    print('Cost time:',end-start)

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    print('Get response from', url, 'Result:', result)

async def newrequest():
    url = 'http://127.0.0.1:5000'
    urls = [url for _ in range(100)]
    async with Pool() as pool:
        result = await pool.map(get,urls)
        print('Get response from', urls, 'Result:', result)

def aio_multi_process():
    start =time.time()
    coroutine = newrequest()
    task = asyncio.ensure_future(coroutine)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)

    end = time.time()
    print('Cost time:',end-start)

if __name__ == '__main__':
    # create_loop()
    # create_no_loop()
    # bind_callback()
    # no_bind_callback()
    # multi_task()
    # process_one()
    # process_multi()
    aio_multi_process()