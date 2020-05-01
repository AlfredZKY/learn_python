
pyppeteer.launcher.launch(options: dict = None, **kwargs) → pyppeteer.browser.Browser 
接下来看看它的参数：
    - ignoreHTTPSErrors (bool)：是否要忽略 HTTPS 的错误，默认是 False。
    - headless (bool)：是否启用 Headless 模式，即无界面模式，如果 devtools 这个参数是 True 的话，那么该参数就会被设置为 False，否则为 True，即默认是开启无界面模式的。
    - executablePath (str)：可执行文件的路径，如果指定之后就不需要使用默认的 Chromium 了，可以指定为已有的 Chrome 或 Chromium。
    - slowMo (int|float)：通过传入指定的时间，可以减缓 Pyppeteer 的一些模拟操作。
    - args (List[str])：在执行过程中可以传入的额外参数。
    - ignoreDefaultArgs (bool)：不使用 Pyppeteer 的默认参数，如果使用了这个参数，那么最好通过 args 参数来设定一些参数，否则可能会出现一些意想不到的问题。这个参数相对比较危险，慎用。
    - handleSIGINT (bool)：是否响应 SIGINT 信号，也就是可以使用 Ctrl + C 来终止浏览器程序，默认是 True。
    - handleSIGTERM (bool)：是否响应 SIGTERM 信号，一般是 kill 命令，默认是 True。
    - handleSIGHUP (bool)：是否响应 SIGHUP 信号，即挂起信号，比如终端退出操作，默认是 True。
    - dumpio (bool)：是否将 Pyppeteer 的输出内容传给 process.stdout 和 process.stderr 对象，默认是 False。
    - userDataDir (str)：即用户数据文件夹，即可以保留一些个性化配置和操作记录。
    - env (dict)：环境变量，可以通过字典形式传入。
    - devtools (bool)：是否为每一个页面自动开启调试工具，默认是 False。如果这个参数设置为 True，那么 headless 参数就会无效，会被强制设置为 False。
    - logLevel  (int|str)：日志级别，默认和 root logger 对象的级别相同。
    - autoClose (bool)：当一些命令执行完之后，是否自动关闭浏览器，默认是 True。
    - loop (asyncio.AbstractEventLoop)：事件循环对象。

# Browser
    luanch()方法返回的就是Browser对象，即浏览器对象，我们会通常将其赋值给browser变量
    class pyppeteer.browser.Browser(connection: pyppeteer.connection.Connection, contextIds: List[str], ignoreHTTPSErrors: bool, 
    setDefaultViewport: bool, process: Optional[subprocess.Popen] = None, closeCallback: Callable[[], Awaitable[None]] = None, **kwargs)
    通过设置浏览器参数就可修改浏览器的配置

# Page
    Page即页面，就对应一个网页，一个选项卡
        - 选择器
            Page对象内置了一些用于选取节点的选择器方法，如J方法传入一个选择器Selector,则能返回对应匹配的第一个节点，等价于querySelector,
            如JJ方法则是返回符合Selector的列表，类似于querySelectorAll
        
        - 选项卡操作
            newpage()即创建选项卡操作

# pyppeteer模拟操作
    - click点击
        button 鼠标按钮，分为left middle right
        clickcount 点击次数，如双击，单击
        delay 延迟点击
        输入文本
    
    - 输入文本
        page.type() 传入两个函数，一个是选择器，一个是要输入的文本

# 让页面等待符合条件的节点加载出来再返回
    - 在这里waitForSelector就是传入一个CSS选择器，如果找到了，立马返回结果，否则等待直到超时
    - 除了waitForSelector方法，还有很多其他的等待方法：
        - waitForFunction:等待某个Js方法执行完毕或返回结果
        - waitForNavigation:等待页面跳转，如果没有加载出来就会报错
        - waitForRequest:等待某个特定请求被发出
        - waitForResponse:等待某个特定的请求收到了回应
        - waitFor:等待通用的等待方法
        - waitForSelector:等待符合选择器的节点加载出来
        - waitForXPath:等待符合XPath的节点加载出来