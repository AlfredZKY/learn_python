#
# Created by preference on 2020/05/02
# Author: AlfredZKY
# Files:pyppeteer_login.py
# WorkPlace:learn_python
#


import asyncio
import aiohttp
import logging
import time
import requests

from pyppeteer import launch
from pyppeteer.errors import TimeoutError

from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')


BASE_URL = 'https://login2.scrape.cuiqingcai.com/login'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')

USERNAME = 'admin'
PASSWORD = 'admin'
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False

browser, tab = None, None


async def init():
    global browser, tab
    browser = await launch(headless=HEADLESS, args=['--disable-infobars',
                                                    f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'
                                                    ], ignoreHTTPSErrors=True)
    tab = await browser.newPage()

    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def simulationlogin():
    await init()
    logging.info('Login in %s', LOGIN_URL)
    try:
        await tab.goto(LOGIN_URL)
        await tab.waitForSelector('.el-input__inner', options={
            'timeout': 1000
        })

        await tab.type('input[name="username"]', USERNAME)
        await tab.type('input[name="password"]', PASSWORD)
        await tab.click('input[type="submit"]', options={
            'button': 'left',
            'clickCount': 1,
            'delay': 3000,
        })
        time.sleep(10)

        cookies = await tab.cookies()
        print(cookies)

        requests.packages.urllib3.disable_warnings()

        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        response_index = session.get(INDEX_URL, verify=False)
        print('Response Status', response_index.status_code)
        print('Response URL', response_index.url)

        await tab.close()
        await browser.close()

    except TimeoutError:
        logging.error('error occurred while login %s',
                      LOGIN_URL, exc_info=True)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(simulationlogin())
