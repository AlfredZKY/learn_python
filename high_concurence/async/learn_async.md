# 阻塞
    - 阻塞状态指程序未得到所需计算资源时被挂起的状态。程序在等待某个操作完成期间，自身无法继续干别的事情，则称该程序在该操作上是阻塞的。  
常见的阻塞形式有：网络 I/O 阻塞、磁盘 I/O 阻塞、用户输入阻塞等。阻塞是无处不在的，包括 CPU 切换上下文时，所有的进程都无法真正干事情，它们也会被阻塞。如果是多核 CPU 则正在执行上下文切换操作的核不可被利用。

# 非阻塞
    - 程序在等待某操作过程中，自身不被阻塞，可以继续运行干别的事情，则称该程序在该操作上是非阻塞的。  
    - 非阻塞并不是在任何程序级别、任何情况下都可以存在的。  
    - 仅当程序封装的级别可以囊括独立的子程序单元时，它才可能存在非阻塞状态。  
    - 非阻塞的存在是因为阻塞存在，正因为某个操作阻塞导致的耗时与效率低下，我们才要把它变成非阻塞的。  

# 同步  
    - 不同程序单元为了完成某个任务，在执行过程中需靠某种通信方式以协调一致，称这些程序单元是同步执行的。
    例如购物系统中更新商品库存，需要用“行锁”作为通信信号，让不同的更新请求强制排队顺序执行，那更新库存的操作是同步的。
    简言之，同步意味着有序。

# 异步
    为完成某个任务，不同程序单元之间过程中无需通信协调，也能完成任务的方式，不相关的程序单元之间可以是异步的。  
    例如，爬虫下载网页。调度程序调用下载程序后，即可调度其他任务，而无需与该下载任务保持通信以协调行为。不同网页的下载、保存等操作都是无关的，
    也无需相互通知协调。这些异步操作的完成时刻并不确定。  
    简言之，异步意味着无序。  

# 多进程
    多进程就是利用 CPU 的多核优势，在同一时间并行地执行多个任务，可以大大提高执行效率。  

# 协程
    协程，英文叫做 Coroutine，又称微线程，纤程，协程是一种用户态的轻量级线程。
    协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈。
    因此协程能保留上一次调用时的状态，即所有局部状态的一个特定组合，每次过程重入时，就相当于进入上一次调用的状态。
    协程本质上是个单进程，协程相对于多进程来说，无需线程上下文切换的开销，无需原子操作锁定及同步的开销，编程模型也非常简单。
