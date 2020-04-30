 # 
 # Created by preference on 2020/04/30
 # Author: AlfredZKY
 # Files:pyppeteer_headless.py
 # WorkPlace:learn_python
 # 


import asyncio
from pyppeteer import launch

url = 'https://www.baidu.com'

check_url = 'https://antispider1.scrape.cuiqingcai.com/'

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
    
# asyncio.get_event_loop().run_until_complete(headless_module())
asyncio.get_event_loop().run_until_complete(dev_module())

