import asyncio

from pyppeteer import launch

url = 'https://httpbin.org/get'
proxy = '127.0.0.1:1087'

async def main():
    browser = await launch({'args':['--proxy-server=http://' + proxy],'headless':False})
    page = await browser.newPage()
    await page.goto(url)
    print(await page.content)
    await browser.close()

if __name__ == '__mian__':
    asyncio.get_event_loop().run_until_complete(main())
