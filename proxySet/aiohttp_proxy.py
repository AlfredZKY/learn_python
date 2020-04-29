import asyncio
import aiohttp


proxy = 'http://127.0.0.1:1087'
url = 'https://httpbin.org/get'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url,proxy=proxy) as response:
            print(await response.text())

if __name__ == '__main__':
    loop = asyncio.get_event_loop().run_until_complete(main())