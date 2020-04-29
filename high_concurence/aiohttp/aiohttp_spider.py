 # 
 # Created by preference on 2020/04/29
 # Author: AlfredZKY
 # Files:aiohttp_spider.py
 # WorkPlace:learn_python
 # 

import pymongo
import requests
import logging
import json
import re
from urllib.parse import urljoin
from pyquery import PyQuery as pq


import asyncio
import aiohttp

import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
MONGO_CONNECT_STRING = 'mongodb://127.0.0.1:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME='books'
client = AsyncIOMotorClient(MONGO_CONNECT_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

async def save_data_to_mongo(data):
     # 这里实际上是 upsert 参数，如果把这个设置为 True，则可以做到存在即更新，不存在即插入的功能，更新会根据第一个参数设置的 name 字段，所以这样可以防止数据库中出现同名的电影数据。
     logging.info('save data %s',data)
     if data:
         return await collection.update_one({
     'id':data.get('id')
     },{
     '$set':data
     },upsert=True)


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')
INDEX_URL = 'https://dynamic5.scrape.cuiqingcai.com/api/book/?limit=18&offset={offset}'
DETAIL_URL= 'https://dynamic5.scrape.cuiqingcai.com/api/book/{id}'

PAGE_SIZE=18
PAGE_NUMBER=10
CONCURRENCY=15

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api(url):
    async with semaphore:
        try:
            logging.info('scraping %s',url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error("error occurred while scraping %s",url,exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * ( page - 1 ))
    return await scrape_api(url)

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data_to_mongo(data)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1,PAGE_NUMBER + 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    logging.info('result %s',json.dumps(results,ensure_ascii=False,indent=2))
    ids = []
    for index_data in results:
        if not index_data:continue 
        for item in index_data.get('results'):
            ids.append(item.get('id'))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_detail_tasks)
    await session.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())