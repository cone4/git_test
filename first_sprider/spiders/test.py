# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 下午5:23
# @Author  : TianJw
# @FileName: test.py
import asyncio
import pyppeteer

# from pyppeteer import launch

pyppeteer.DEBUG = True


async def main():
    browser = await pyppeteer.launch()
    # page = await browser.newPage()
    # browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/?tn=48021271_8_hao_pg')
    await page.xpath("//*[@id='form']/span[1]")
    # await page.screenshot({'path': 'example.png'})
    # await browser.close()
    content = await page.content()
    # with open('q.html', 'a', encoding='utf-8') as f:
    #     f.write(content)
    cookies = await page.cookies()
    print(cookies)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
