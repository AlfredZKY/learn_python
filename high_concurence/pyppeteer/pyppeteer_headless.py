 # 
 # Created by preference on 2020/04/30
 # Author: AlfredZKY
 # Files:pyppeteer_headless.py
 # WorkPlace:learn_python
 # 


import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq 

proxy = '127.0.0.1:1087'

url = 'https://www.baidu.com'

check_url = 'https://antispider1.scrape.cuiqingcai.com/'
check_url1 = 'https://antispider1.scrape.cuiqingcai.com/'
check_url2 = 'https://antispider2.scrape.cuiqingcai.com/'

click_url = 'https://dynamic2.scrape.cuiqingcai.com/'

width,height = 1366,768

async def headless_module():
    # 关闭无头模式，生产环境中还是关闭
    await launch(headless=False)
    await asyncio.sleep(100)

async def dev_module():
    # 设置 devtools=True时，headless模式默认false
    # 禁用提示条 --disable-infobars
    # browser = await launch(devtools=True,args=['--disable-infobars'])
    browser = await launch(headless=False,args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto(check_url)
    await asyncio.sleep(10)

async def web_check():
    # 设置浏览器窗口
    browser = await launch(headless=False,args=['--disable-infobars',f'--window-size={width},{height}'])
    page = await browser.newPage()
    
    # 设置浏览器页面的窗口
    await page.setViewport({'width':width,'height':height})

    # 执行js代码，过掉webdriver浏览器设置 
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')
    
    await page.goto(check_url)
    await asyncio.sleep(10)

async def load_data():
    url = 'https://www.taobao.com'
    browser = await launch(headless=False,userDataDir='high_concurence/pyppeteer/userdata',args=['--disable-infobars',f'--window-size={width},{height}'])
    page = await browser.newPage()

    # 设置页面窗口
    await page.setViewport({'width':width,'height':height})

    await page.goto(url)
    await asyncio.sleep(100)

async def clear_data():
    browser = await launch(headless=False,args=['--window-size={width},{height}','--disable-infobars'])

    # 无痕模式
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()

    await page.setViewport({'width':width,'height':height})
    await page.goto(url)
    await asyncio.sleep(100)
    await browser.close()


async def page_selector():
    browser = await launch()
    page = await browser.newPage()

    url = 'https://dynamic2.scrape.cuiqingcai.com/'

    await page.goto(url)

    await page.waitForSelector('.item .name')
    j_result1 = await page.J('.item .name')
    j_result2 = await page.querySelector('.item .name')
    print(j_result1)
    print(j_result2)

    jj_result1 = await page.JJ('.item .name')
    jj_result2 = await page.querySelectorAll('.item .name')

    print(jj_result1)
    print(jj_result2)

    await asyncio.sleep(10)
    await browser.close()

async def page_switch():
    browser = await launch(headless=False)

    page = await browser.newPage()
    await page.goto(url)

    page = await browser.newPage()
    await page.goto(url)

    pages = await browser.pages()
    print('Pages:',pages)
    page1 = pages[1]

    # 选项卡切换
    await page1.bringToFront()

    await asyncio.sleep(10)

    await browser.close()

# page Basic operation
async def page_operate():
    browser = await launch(headless=False,args=['--disable-infobars'])
    page = await browser.newPage()

    await page.goto(check_url1)
    await page.goto(check_url2)

    # 后退
    await page.goBack()

    # 前进
    await page.goForward()

    # 刷新
    await page.reload()

    # 保存
    await page.pdf()

    # 截图
    await page.screenshot()

    # 设置页面 HTML
    await page.setContent('<h2>Hello World </h2>')

    # 设置User-Agent
    await page.setUserAgent('Python')

    # 设置Headers
    await page.setExtraHTTPHeaders(headers={})

    await asyncio.sleep(2000)

    # 关闭
    await page.close()
    await browser.close()

async def click_operate():
    browser = await launch(headless=False,args=['--disable-infobars'])
    page = await browser.newPage()

    await page.goto(click_url)
    await page.waitForSelector('.item .name')
    await page.click('.item .name',options={
        'button':'right',
        'clickCount':1,
        'delay':3000,
    })

    await browser.close()

async def input_text():
    url = 'https://www.taobao.com'
    browser = await launch(headless=False,args=['--disable-infobars',f'--window-size={width},{height}'])
    page = await browser.newPage()

    await page.goto(url)

    # 设置窗口
    await page.setViewport({'width':width,'height':height})

    # 后退
    await page.waitForSelector('#q')

    await page.type('#q','iPad')

    # 点击
    await page.click('.btn-search', options={
        'button':'left',
        'clickCount':1,
        'delay':300,
        })

    # 关闭
    await asyncio.sleep(10)
    await browser.close()


async def get_info():
    browser = await launch(headless=False,args=['--disable-infobars',f'--window-size={width},{height}'])

    page = await browser.newPage()

    await page.goto(click_url)
    print('HTML:',await page.content())
    print('Cookies:',await page.cookies())
    await browser.close()


# asyncio.get_event_loop().run_until_complete(headless_module())
# asyncio.get_event_loop().run_until_complete(dev_module())
# asyncio.get_event_loop().run_until_complete(web_check())
# asyncio.get_event_loop().run_until_complete(load_data())
# asyncio.get_event_loop().run_until_complete(clear_data())
# asyncio.get_event_loop().run_until_complete(page_selector())
# asyncio.get_event_loop().run_until_complete(page_switch())
# asyncio.get_event_loop().run_until_complete(page_operate())
# asyncio.get_event_loop().run_until_complete(click_operate())
# asyncio.get_event_loop().run_until_complete(input_text())
asyncio.get_event_loop().run_until_complete(get_info())
