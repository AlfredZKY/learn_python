# import asyncio

# async def do_some_work(x):
#     print("waiting " + str(x))
#     await asyncio.sleep(x)

# print(asyncio.iscoroutinefunction(do_some_work))
# # print(asyncio.iscoroutine(do_some_work(3))) #这样执行会报出一条警告
# asyncio.get_event_loop().run_until_complete(do_some_work(3))

import time
import concurrent.futures 

import asyncio

def process_bar():
    scale = 50 
    print("执行开始".center(scale//2,"-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

    start = time.perf_counter() # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
    for i in range(scale+1):   
        a = '*' * i             # i 个长度的 * 符号
        b = '.' * (scale-i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50 
        c = (i/scale)*100  # 显示当前进度，百分之多少
        dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
        time.sleep(0.1)     # 在输出下一个百分之几的进度前，停止0.1秒
    print("\n"+"执行结果".center(scale//2,'-'))

async def execute(x):
    print('Number:',x)

# 返回一个coroutine对象
coroutine = execute(1)
print('Coroutine:',coroutine)
print('After calling execute')

# 创建一个事件循环
loop = asyncio.get_event_loop()

# 创建task1
# 将 coroutine 对象注册进事件循环
# loop.run_until_complete(coroutine)

# 由上可知，async定义的方法就会变成一个无法执行的coroutine对象，必须将其注册到事件循环中才可以执行
print("After calling loop")

# 创建task2
# task是对coroutine对象的进一步封装，它里面相比coroutine对象多了运行状态，比如running，finished等。我们可以用这些状态来获取协程对象的执行情况
# task = loop.create_task(coroutine)
# print('Task:',task)
# loop.run_until_complete(task)
# print('Task:',task)
# print('After calling loop')

# 创建task3
task = asyncio.ensure_future(coroutine)
print('Task:',task)
loop.run_until_complete(task)
print('Task:',task)
print('After calling loop')