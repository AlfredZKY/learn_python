import pymongo
import requests
import logging
import re


from urllib.parse import urljoin
from pyquery import PyQuery as pq


Base_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')

def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping is %s',response.status_code,url)
    except requests.RequestException:
        # 这时我们将 logging 的 error 方法的 exc_info 参数设置为 True 则可以打印出 Traceback 错误堆栈信息。
        logging.error('error occurred while scraping %s',url,exc_info=True)

def scrape_index(page):
    # 格式化字符串常量（formatted string literals），是Python3.6新引入的一种字符串格式化方法
    index_url = f'{Base_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    doc = pq(html)
    # .el-card .name
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(Base_URL,href)
        logging.info('get deatil url %s',detail_url)
        yield detail_url


def scrape_defail(url):
    return scrape_page(url)

def parse_detail(html):
    #封面：是一个 img 节点，其 class 属性为 cover。
    # 名称：是一个 h2 节点，其内容便是名称。
    # 类别：是 span 节点，其内容便是类别内容，其外侧是 button 节点，再外侧则是 class 为 categories 的 div 节点。
    # 上映时间：是 span 节点，其内容包含了上映时间，其外侧是包含了 class 为 info 的 div 节点。但注意这个 div 前面还有一个 class 为 info 的 div 节点，我们可以使用其内容来区分，也可以使用 nth-child 或 nth-of-type 这样的选择器来区分。
    # 另外提取结果中还多了「上映」二字，我们可以用正则表达式把日期提取出来。
    # 评分：是一个 p 节点，其内容便是评分，p 节点的 class 属性为 score。
    # 剧情简介：是一个 p 节点，其内容便是剧情简介，其外侧是 class 为 drama 的 div 节点。
    doc = pq(html)
    cover = doc('img.cover').attr("src")
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})',published_at).group(1) if published_at and re.search('(\d{4}-\d{2}-\d{2})',published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        'cover':cover,
        'name':name,
        'categories':categories,
        'published_at':published_at,
        'drama':drama,
        'score':score
    }

def main (page):
    # for page in range(1,TOTAL_PAGE + 1):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    # logging.info('detail urls %s',list(detail_urls))
    for detail_url in detail_urls:
        detail_html = scrape_defail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s',data)
        logging.info('save data to mongodb')
        save_data_to_mongo(data)
        logging.info('data saved successfully')

        
MONGO_CONNECT_STRING = 'mongodb://127.0.0.1:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME='movies'

client = pymongo.MongoClient(MONGO_CONNECT_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

def save_data_to_mongo(data):
    # 这里实际上是 upsert 参数，如果把这个设置为 True，则可以做到存在即更新，不存在即插入的功能，更新会根据第一个参数设置的 name 字段，所以这样可以防止数据库中出现同名的电影数据。
    collection.update_one({
        'name':data.get('name')
    },{
        '$set':data
    },upsert=True)

import multiprocessing

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1,TOTAL_PAGE+1)
    pool.map(main,pages)
    pool.close()
    pool.join()
