# 现在很多网站都加上了对selenium的检测，来防止一些爬虫的恶意爬取，即如果检测到有人在使用selenium打开浏览器，那就直接屏蔽
# 在大多数情况下，检测基本原理是检测当前浏览器窗口下的window.navigator对象是否包含webdriver这个属性，因为在正常使用浏览器的情况下，
# 这个属性是undefined，然而一旦我们使用了selenium，selenium会给window.navigator设置webdriver属性，很多网站就通过JavaScript判断
# 如果webdriver属性存在，那就直接屏蔽

# 比如通过调用execute_script方法来执行如下代码：
# Object.defineProperty(navigator, "webdriver", {get: () => undefined})
# 这行JavaScript的确是可以把webdriver属性置空，但是execute_script调用这行JavaScript语句实际上是在页面加载完毕之后才执行的，执行太晚了，
# 网站早在最初页面渲染之前就已经对 webdriver 属性进行了检测，所以用上述方法并不能达到效果。
# 在 Selenium 中，我们可以使用 CDP（即 Chrome Devtools-Protocol，Chrome 开发工具协议）来解决这个问题，
# 通过 CDP 我们可以实现在每个页面刚加载的时候执行 JavaScript 代码，执行的 CDP 方法叫作 Page.addScriptToEvaluateOnNewDocument，
# 然后传入上文的 JavaScript 代码即可，这样我们就可以在每次页面加载之前将 webdriver 属性置空了
# 另外我们还可以加入几个选项来隐藏webdriver提示条和自动化扩展信息

from selenium import webdriver
from selenium.webdriver import ChromeOptions

url = 'https://antispider1.scrape.cuiqingcai.com/'
option = ChromeOptions()

# 采用无头模式
option.add_argument('--headless')

option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
    'source':'Object.defineProperty(navigator,"webdriver",{ get: () => undefined})'
})

browser.set_window_size(1366,768)

browser.get(url)
browser.get_screenshot_as_file('/Volumes/mac_store/project/learn_python/learn_selenium/images/preview.png')
browser.close()



