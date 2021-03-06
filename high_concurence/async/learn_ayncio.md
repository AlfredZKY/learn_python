# 异步IO
    所谓「异步 IO」，就是你发起一个 IO 操作，却不用等它结束，你可以继续做其他事情，当它结束时，你会得到通知。
    Asyncio 是并发（concurrency）的一种方式。对 Python 来说，并发还可以通过线程（threading）和多进程（multiprocessing）来实现。
    Asyncio 并不能带来真正的并行（parallelism）。当然，因为 GIL（全局解释器锁）的存在，Python 的多线程也不能带来真正的并行。
    可交给 asyncio 执行的任务，称为协程（coroutine）。一个协程可以放弃执行，把机会让给其它协程（即 yield from 或 await）。

# 异步爬虫的原理和解析
    - 爬虫是IO密集型任务，当我们使用rerques爬取某个站点，就必须等待返回响应，而在在等待响应过程中，整个爬虫在这段时间内，是处于空闲状态
    - 采用异步方式进行爬取，即可缩减爬取时间，该方法对于IO密集型任务非常有效，应用到网络爬虫中，效果非常明显

# 熟悉协程用法
    - event_loop:
        时间循环，相当于一个无线循环，我们可以把一些函数注册到这个事件循环上，当满足条件发生时，就会调用对应的处理方法
    - coroutine:
        协程，在Python中常指代为协程对象类型，我们可以将协程对象注册到事件循环中。它会被事件循环调用，我们可以使用async关键字来定义一个方法
        这个方法在调用时不会立即被执行，而是返回一个协程对象
    - task :
        任务，它是协程对象的进一步封装，包含了任务的各个状态
    - future:
        代表将来执行或没有执行的任务结果，实际上和task没有区别
    - aysnc/await 
        它是从Python3.5才出现，专门用于定义协程，其中async定义一个协程，await用来挂起阻塞方法的执行,协程必须挂起，才能让出其他协程执行时间
        - 一个原生 coroutine 对象
        - 一个由 types.coroutine 修饰的生成器，这个生成器可以返回 coroutine 对象。
        - 一个包含 __await__ 方法的对象返回的一个迭代器。
    - 使用情形
        - 原则是，如果其返回的是一个coroutine对象(如async修饰的方法)，那么前面就要加await

# async 和 await
    - async 正常的函数执行是不会中断执行的，async可以声明可中断的函数，即异步函数，执行过程中可挂起，然后执行其他异步函数
    - await 用于挂起异步函数
    - asyncio.wait 和 asyncio.gather都是可以接受多个future或coro组成的列表，但不同的是，
    asyncio.gather会将列表中不是task的coro预先封装future，而wait则不会。



