import asyncio
import requests
import aiohttp
import time

url = 'https://static4.scrape.cuiqingcai.com/'

start = time.time()


# 把io密集型任务放在协程中，然后在挂起即可
async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response

async def request():
    print('Waitting for',url)
    response = await get(url)
    print('Get response from',url,'response',response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('Cost time:',end - start)


