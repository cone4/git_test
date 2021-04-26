# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
import requests
from selenium import webdriver
from scrapy import signals
from scrapy.http import HtmlResponse


class FirstSpriderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class FirstSpriderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        # if response.url in spider.start_urls:
        #     driver = spider.driver
        #     driver.get(url=response.url)
        #     time.sleep(2)
        #     input_element = driver.find_element_by_id('kwd')
        #     input_element.clear()  # 清楚文本
        #     input_element.send_keys("tt")  # 模拟按键输入
        #     time.sleep(1)
        #     input_element.submit()  # 模拟回车操作
        #     # input_element.search_text.click() # 单机元素  # 模拟回车操作
        #
        #     # 通过javascript设置浏览器窗口的滚动条位置
        #     # 通过execute_script()方法执行
        #     try:
        #         i = 0
        #         while True:
        #             i += 1
        #             print('正在爬取第%s页----------------------------------------------' % i)
        #             time.sleep(2)
        #             # js = 'window.scrollTo(0, document.body.scrollHeight)'
        #             # driver.execute_script(js)
        #             # 展开更多的按钮可能出现不止一次，点了之后还有的情况
        #             # showmore_button = driver.find_element_by_class_name("page_box")
        #             showmore_button = driver.find_element_by_link_text("下一页")
        #             showmore_button.click()
        #             time.sleep(5)
        #
        #             if not showmore_button:
        #                 break
        #
        #     except Exception as e:
        #         pass
        #
        #     html = driver.page_source
        #     # print(driver.current_url)
        #     my_response = HtmlResponse(url=driver.current_url, body=html, encoding='utf-8', request=request)
        #     if my_response:
        #         return my_response
        #
        # raise Exception("页数超过限制!!!")
        # else:
        #     html = driver.page_source
        #     # print(driver.current_url)
        #     my_response = HtmlResponse(url=driver.current_url, body=html, encoding='utf-8', request=request)
        #     if my_response:
        #         return my_response
        #     else:
        #         return response

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path=r"E:\chromedriver\chromedriver.exe")
        self.driver = webdriver.Firefox()

    def process_request(self, request, spider):
        self.driver.get(url=request.url)
        time.sleep(2)
        input_element = self.driver.find_element_by_id('kwd')
        input_element.clear()  # 清楚文本
        input_element.send_keys("tt")  # 模拟按键输入
        time.sleep(1)
        input_element.submit()  # 模拟回车操作
        time.sleep(2)

        try:
            # 找专题收入的展开更多的按钮，有就拿，没有就什么都不做
            while True:
                # 展开更多的按钮可能出现不止一次，点了之后还有的情况
                showmore_button = self.driver.find_element_by_link_text("下一页")
                # showmore_button = self.driver.find_element_by_class_name("H7E3vT")
                showmore_button.click()
                time.sleep(2)
                if not showmore_button:
                    break
        except:
            pass

        source = self.driver.page_source
        # 再selenium操作完之后获取整个页面的源码
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding="utf-8")
        # 把源代码封装成response对象
        return response


class MyproxiesSpiderMiddleware(object):

    def __init__(self, ip=None):
        self.ip = ip

    def process_request(self, request, spider):
        # print(request.meta['proxy'])
        url = 'http://127.0.0.1:5555/random'  # 随机ip提取接口
        response = requests.get(url)
        if response.status_code == 200:
            proxy = response.text.strip()
            print('---------this is request ip ----------:' + proxy)
            ip = 'http://' + proxy
            print(ip)
            request.meta['proxy'] = ip

    def process_response(self, request, response, spider):
        if response.status_code == 403:
            url = 'http://127.0.0.1:5555/random'  # 随机ip提取接口
            response = requests.get(url)
            if response.status_code == 200:
                proxy = response.text.strip()
                print('---------this is request ip ----------:' + proxy)
                ip = 'http://' + proxy
                print(ip)
                request.meta['proxy'] = ip
