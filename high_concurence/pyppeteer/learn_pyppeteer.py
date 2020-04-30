 # 
 # Created by preference on 2020/04/30
 # Author: AlfredZKY
 # Files:learn_pyppeteer.py
 # WorkPlace:learn_python
 # 


import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


width,heigth = 1366,768

url = 'https://dynamic2.scrape.cuiqingcai.com/'

async def main():
    # 实例化一个浏览器对象
    browser = await launch()
    
    # 浏览器中新建一个选项卡，同时新建一个page对象
    page = await browser.newPage()

    # 设置浏览器窗口
    await page.setViewport({'width':width,'height':heigth})

    # 在浏览器中输入url,浏览器跳转到对应的页面进行加载
    await page.goto(url)
    
    # 页面等待所选的选择器对应的节点信息加载出来，如果加载出来了，立即返回，否则会持续等待，直到超市
    await page.waitForSelector('.item .name')

    # 异步等待一下
    await asyncio.sleep(2)

    # 截图 成功后可以看到js渲染后的页面 另外还可以指定保存格式 type、清晰度 quality、是否全屏 fullPage、裁切 clip 等各个参数实现截图。
    await page.screenshot(path='results/example.png')

    # # 获取当前浏览器页面的源代码
    # doc = pq(await page.content())

    # names = [item.text() for item in doc('.item .name').items()]
    # print('names:',names)

    # 执行js代码 设置网页的宽高，像素大小比率三个值
    dimensions = await page.evaluate('''()=>{
        return {
            width:document.documentElement.clientWidth,
            height:document.documentElement.clientHeight,
            deviceScaleFactor:window.devicePixelRatio,
        }   
    }''')
    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

