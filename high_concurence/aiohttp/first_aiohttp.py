import asyncio
import aiohttp
import time


url = 'https://cuiqingcai.com'

async def fetch(session,url):
    async with session.get(url) as response:
        return await response.text(),response.status

async def main():
    async with aiohttp.ClientSession() as session:
        html,status = await fetch(session,url)
        print(f'html:{html[:1000]} ...')
        print(f'status:{status}')

async def seturlparameter():
    timeout = aiohttp.ClientTimeout(total=1)
    url = "https://httpbin.org/get"
    params = {'name':'germey','age':25}
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url,params=params) as response:
        #async with session.post(url,params=params) as response:
            print(await response.text())
            
# 并发限制
CONCURRENCY = 5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None
async def scrape_api():
    async with semaphore:
        print('scraping',URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(100)]
    await asyncio.gather(*scrape_index_tasks)
    

# 注意在 Python 3.7 及以后的版本中，我们可以使用 asyncio.run(main()) 来代替最后的启动操作，不需要显式声明事件循环，
# run 方法内部会自动启动一个事件循环。但这里为了兼容更多的 Python 版本，依然还是显式声明了事件循环。

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
    loop.run_until_complete(seturlparameter())

    loop.run_until_complete(main())

