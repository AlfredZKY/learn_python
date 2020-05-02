#
# Created by preference on 2020/05/02
# Author: AlfredZKY
# Files:pyppeteer_spider.py
# WorkPlace:learn_python
#


import pymongo
import requests
import logging
import json
import re
import asyncio
import aiohttp
from urllib.parse import urljoin
from pyquery import PyQuery as pq

from pyppeteer import launch
from pyppeteer.errors import TimeoutError


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'


proxy = '127.0.0.1:1087'

TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768

HEADLESS = False

browser, tab = None, None


async def init():
    global browser, tab
    browser = await launch(headless=HEADLESS, args=['--proxy-server=http: //' + proxy,
                                                    '--disable-infobars', f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={
            'timeout': TIMEOUT * 1000
        })
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node=>node,href)')

async def scrape_detail(url):
    await scrape_page(url,'h2')

async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2','node=>node.indexText')
    categories = await tab.querySelectorAllEval('.categories button span','node=>nodes.map(node=>node.innerText)')
    cover = await tab.querySelectorEval('.cover','node=>node.src')
    score = await tab.querySelectorEval('.score','node=>node.innerText')
    drama = await tab.querySelectorEval('.drama p','node=>node.innerText')
    return {
        'url':url,
        'name':name,
        'categories':categories,
        'cover':cover,
        'score':score,
        'drama':drama
    }

async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            # logging.info('detail_urls %s', detail_urls)
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('data %s',detail_data)
    finally:
        await tab.close()

from os import makedirs
from os.path import exists

RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)
async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dumps(data,open(data_path,'w',encoding='utf-8'),ensure_ascii=False,indent=2)



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
