# 异步IO
所谓「异步 IO」，就是你发起一个 IO 操作，却不用等它结束，你可以继续做其他事情，当它结束时，你会得到通知。
Asyncio 是并发（concurrency）的一种方式。对 Python 来说，并发还可以通过线程（threading）和多进程（multiprocessing）来实现。
Asyncio 并不能带来真正的并行（parallelism）。当然，因为 GIL（全局解释器锁）的存在，Python 的多线程也不能带来真正的并行。
可交给 asyncio 执行的任务，称为协程（coroutine）。一个协程可以放弃执行，把机会让给其它协程（即 yield from 或 await）。