
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