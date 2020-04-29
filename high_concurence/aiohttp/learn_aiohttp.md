# 学习aiohttp
    - aiohttp是一个基于asyncio的异步HTTP网络模块，它既提供服务端，又提供了客户端，其中我们用服务端又可以搭建一个支持
    异步处理的服务器，用于处理请求并返回响应，但requests发起的是同步的请求，而aiohttp则发起是异步的
    - with as 语句之前同样需要加async来修饰，在Python中，with as 语句用于声明一个上下文管理器，能够帮我们自动分配和释放资源，在异步方法中，
    with as 前面加上async代表声明一个支持异步的上下文管理器
    - 对于一些返回coroutine的操作，前面需要加await来修饰，如response调用text方法，查询api可以发现其返回的是coroutine对象，那么前面就要
    加await，而对于状态码来说，其返回值就是一个数值类型，那么就不需要await。
注意：
# 注意在 Python 3.7 及以后的版本中，我们可以使用 asyncio.run(main()) 来代替最后的启动操作，不需要显式声明事件循环，
# run 方法内部会自动启动一个事件循环。但这里为了兼容更多的 Python 版本，依然还是显式声明了事件循环。