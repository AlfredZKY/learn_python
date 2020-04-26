import requests
import logging
import json


from os import makedirs
from os.path import exists


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')

index_url = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}'
detail_url = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/{id}'

RESULTS_DIR = 'results'
LIMIT = 10
TOTAL_PAGE = 10

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'

    # 然后用json的dump方法将数据保存成文本格式。dump的方法设置了两个参数，一个是ensure_ascii，我们将其设置为False
    # 它可以保证中文字符在文件中能以正常的中文文本呈现，而不是 unicode 字符；
    # 另一个是 indent，它的数值为 2，这代表生成的 JSON 数据结果有两个空格缩进，让它的格式显得更加美观。
    json.dump(data,open(data_path,'w',encoding='utf-8]'),ensure_ascii=False,indent=2)

def scrape_detail(id):
    url = detail_url.format(id=id)
    return scrape_api(url)


def scrape_api(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scrapings %s',url,exc_info=True)    

def scrape_index(page):
    url = index_url.format(limit=LIMIT,offset=LIMIT*(page-1))
    return scrape_api(url)

if __name__ == '__main__':
    for page in range(1,TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s',detail_data)
            save_data(detail_data)
