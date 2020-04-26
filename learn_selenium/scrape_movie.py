 # 
 # Created by preference on 2020/04/26
 # Author: AlfredZKY
 # Files:scrape_movie.py
 # WorkPlace:learn_python
 # 

# 所以本课时我们要完成的目标有：

# 通过 Selenium 遍历列表页，获取每部电影的详情页 URL。
# 通过 Selenium 根据上一步获取的详情页 URL 爬取每部电影的详情页。
# 提取每部电影的名称、类别、分数、简介、封面等内容。

import pymongo
import requests
import logging
import json
import re
from urllib.parse import urljoin
from pyquery import PyQuery as pq
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')

INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
TOTAL_PAGE = 10


# 开头无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 实例化一个浏览器对象
TIME_OUT = 10
browser = webdriver.Chrome(options=options)

# 设置显式等待时间
wait = WebDriverWait(browser,TIME_OUT)

# 判断列表页加载成功 当页面出现成功，我们可以通过css选择器，判断css选择器的内容即可判断页面是否加载成功 
# 配合超时设置，如果没有加载成功，就会抛出超时异常
def scrape_page(url,condition,locator): 
    logging.info('scrapeing %s',url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutError:
        logging.error('error occurred while scraping %s',url,exc_info=True)

def scrape_index(page):
    url = INDEX_URL.format(page=page)
    scrape_page(url,condition=EC.visibility_of_all_elements_located,locator=(By.CSS_SELECTOR,'#index .item'))

def parse_index():
    elements = browser.find_elements_by_css_selector('#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL,href)

def scrape_detail(url):
    scrape_page(url,condition=EC.visibility_of_all_elements_located,locator=(By.TAG_NAME,'h2'))

def parse_detail():
    url = browser.current_url
    name = browser.find_element_by_tag_name('h2').text
    # 选择 button 
    categories = [element.text for element in browser.find_elements_by_css_selector('.categories button span')]
    cover = browser.find_element_by_css_selector('.cover').get_attribute('src')
    score = browser.find_element_by_class_name('score').text
    drama = browser.find_element_by_css_selector('.drama p').text
    return {
        'url':url,
        'name':name,
        'categories':categories,
        'cover':cover,
        'score':score,
        'drama':drama
    }

from os import makedirs
from os.path import exists

RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data,open(data_path,'w',encoding='utf-8'),ensure_ascii=False)

def main():
    try:
        for page in range(1,TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info('details urls %s',detail_url)
                scrape_detail(detail_url)
                detail_data=parse_detail()
                logging.info('detail data %s',detail_data)
                save_data(detail_data)
            
    finally:
        browser.close()

if __name__ == '__main__':
    main()

