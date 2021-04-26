# -*- coding: utf-8 -*-
import time
# from fake_useragent import UserAgent
from uuid import uuid1
import scrapy
import json
from selenium import webdriver


# 爬虫类
class ExampleSpider(scrapy.Spider):
    # name 爬虫名称
    # 唯一标识了爬虫 运行爬虫的时候会用的到 必须要有 且不能重复
    # 有时候运行不需要爬虫名，但是爬虫名不可以删掉
    name = 'example'

    # allowed:允允许 domains:域名
    # 限定爬取的范围 这个我一般是注掉的 看自己需要
    # allowed_domains = ['baidu.com']

    # 起始的url 项目一启动会自动的对start_urls的url进行发起请求
    # start_urls = ['https://my.oschina.net/u/4264487/blog/3790472']
    # start_urls = ['https://appgallery.huawei.com/search/洋葱学院']
    # start_urls = ['https://shouji.baidu.com/s?wd=洋葱学院']
    # start_urls = ['https://shouji.baidu.com/s?wd=QQ']
    # start_urls = ['https://sj.qq.com/myapp/searchAjax.htm?kw=洋葱学院']
    # start_urls = ['https://www.wandoujia.com/search?key=QQ&source=index']
    # start_urls = ['https://s.liqucn.com/s.php?words=QQ']
    # start_urls = ['http://zhushou.360.cn/']
    # start_urls = ['http://zhushou.360.cn/search/index/?kw=QQ']
    # start_urls = ['http://icanhazip.com/']

    # start_urls = ['https://s.liqucn.com/s.php?words=QQ']
    start_urls = ['https://www.lenovomm.com/search?key=微信']

    # start_urls = ['http://app.mi.com/search?keywords=QQ']
    # start_urls = ['https://app.mi.com/categotyAllListApi?page=1&categoryId=15&pageSize=30']

    # start_urls = ['http://app.mi.com/']

    #
    # start_urls = ['https://app.mi.com/search?keywords=QQ&page=6']
    # start_urls = ['https://www.wandoujia.com/search?key=QQ&source=index']
    # start_urls = [
    #     'https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.completeSearchWord&serviceType=20&keyword=QQ=&locale=zh']

    # start_urls = ['https://app.mi.com/searchAll?keywords=QQ']
    # start_urls = ['https://sj.qq.com/myapp/search.htm?kw=tx']
    # https://sj.qq.com/myapp/searchAjax.htm?kw=tx&pns=MTA=&sid=0
    # pages = ["MTA", "MjA", "MzA", "NDA"]
    # start_urls = ['https://sj.qq.com/myapp/searchAjax.htm?kw=QQ&pns=%s=&sid=0' % page for page in pages] + [
    #     'https://app.mi.com/searchAll?keywords=QQ']
    # print(start_urls)

    # 设置无头浏览器
    # option = webdriver.FirefoxOptions()
    # option.add_argument('--headless')
    # Firefox浏览器
    # driver = webdriver.Firefox(firefox_options=option, executable_path='/usr/local/bin/geckodriver')
    # driver = webdriver.Firefox()

    # driver = webdriver.Firefox("驱动路径")

    def parse(self, response):
        # print(response.text)

        app_ip = json.loads(response.text)["data"]
        print(app_ip)
        li_list = response.xpath('//ul[@class="category-list"]/li')
        for li in li_list:
            title = li.xpath("./a/text()").extract_first()
            link = li.xpath("./a/@href").extract_first()
            print(title)
            print(link)
        # pass
        # app_info_list_all = json.loads(response.text)["app"]
        # item['channel_name1'] = 'Tencent'
        # item['file_urls'] = [i['apkUrl']]
        # item['app_name'] = i['appName']
        # item['downNum'] = i['appDownCount']
        # item['app_type'] = i['categoryName']
        # item['image_urls'] = [i['iconUrl']]

        # app_name = app_info_list_all["name"]
        # app_type = app_info_list_all["kindName"]
        # update_time = app_info_list_all["releaseDate"]
        # app_downloads = app_info_list_all["sizeDesc"]
        # image_urls = app_info_list_all["icon"]
        #
        # print(app_name)
        # print(app_type)
        # print(update_time)
        # print(str(app_downloads)[:-2])
        # print(image_urls)

        # app_info_list_all = response.text["layoutData"]["dataList"]
        # print(app_info_list_all)
        # with open('q.html', 'a', encoding='utf-8') as f:
        #     f.write(response.text)
        # print(type(json.loads(response.text)))

        # li_list = response.xpath('//ul[@id="j-search-list"]/li')
        # for li in li_list:
        #     link = li.xpath("./div[@class='app-desc']/h2/a/@href").extract_first()
        #     # link = 'https://app.mi.com' + link
        #     # print(link)
        #     time.sleep(3)
        #     headers = {
        #         'Host': 'www.wandoujia.com',
        #         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
        #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #         'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        #         'Accept-Encoding': 'gzip, deflate, br',
        #         'Connection': 'keep-alive',
        #         'Referer': 'https://www.wandoujia.com/search/9103467383794509466',
        #         'Cookie': '_uab_collina=161785133957097958743899; sid=17682720161785076525563132026683; sid.sig=aBLa7ZeElZNIDC29r8pLXN2thMoKNliurOl_jiLE9WU; _pwid=27286720161785077123350206269253; wdj_source=direct; _ga=GA1.2.866678610.1617850774; _gid=GA1.2.164716687.1617850774; Hm_lvt_c680f6745efe87a8fabe78e376c4b5f9=1617860536,1617863215,1617864171,1617865611; UM_distinctid=178af6bb65e322-037677c4c3136e-7e22675c-109e74-178af6bb65f88b; CNZZDATA1272849134=1821409722-1617848396-%7C1617864623; cna=fNLuGCn7qn8CAW/BgVWXoVvi; isg=BAMDd-izZwRnPyvwVt39oj5lkc6teJe6V_GCSzXgNGLA9CIWvUt5CtclbgS6z--y; xlly_s=1; _uToken=T2gA8gHL4KRAW_EQBydLyVvPzHr1ErfVFrpcL82YabGuWba3_tGCMLOniwiY5MVJpJs%3D; x5sec=7b2277616762726964676561643b32223a22373636636335633865323761306363623465336535333235613865303162373843506a4c756f4d47454a4830324a69627a38584b496a4430764e753441773d3d227d; ctoken=-ioVFkyRyJShR3wFcKYl5ENP; _gat=1; Hm_lpvt_c680f6745efe87a8fabe78e376c4b5f9=1617865611',
        #         'Upgrade-Insecure-Requests': '1',
        #         'TE': 'Trailers',
        #     }
        #     yield scrapy.Request(url=link, callback=self.detai_parse, headers=headers)
        # li_xpath = []
        # li_list = response.xpath('//div[@class="SeaCon"]/ul/li')
        # for li in li_list:
        #     link = li.xpath('./dl/dd/h3/a/@href').extract_first()
        #     link = 'http://zhushou.360.cn' + link
        #     print(link)
        #     li_xpath.append(link)
        # print(li_xpath)

        # with open('json.txt', 'a', encoding='utf-8') as f:
        #     f.write(response.text)
        # for item in url_list:
        #     f.write(item)
        #     f.write('\n')
        # @id="appQrcode" and
        # @class="product-qrcode"
        # print(response.text)
        # li_list=response.xpath('//*[@id="appQrcode"]/@title')
        # print(li_list)

        # list_xpath = []
        # li_list = response.xpath('//div[@class="download comdown"]/a')
        # for i in li_list:
        #     link = i.xpath('./@href').extract_first()
        #     # print(link)
        #     if link !='':
        #         list_xpath.append(link)
        # print(list_xpath)
        # li_list = response.xpath('//div[@class="SeaCon"]/ul/li[1]')
        # for li in li_list:
        #     link = li.xpath('./dl/dd/h3/a/@href').extract_first()
        #     link = 'http://zhushou.360.cn' + link
        # print(link)
        # yield scrapy.Request(url=link, callback=self.detai_parse)
        #     list_xpath.append(link)
        # print(list_xpath)
        # pass

        # li_list = response.xpath('//ul[@id="menu-list"]/li')
        # for li in li_list:
        #     title = li.xpath('./h2/a/@title').extract_first()
        #     link = li.xpath('./h2/a/@href').extract_first()
        #     brief = ''.join(li.xpath('./text()').extract()).replace('\n', '')
        #     # date = re.findall(r'\d+-\d+-\d+', li.xpath('./p/text()').extract_first())[0]
        #     print(title)
        #     print(link)
        #     print(brief)
        #     # print(date)
        # print('-' * 50)

        # li_list = response.xpath('//ul[@id="menu-list"]/li')
        # for li in li_list:
        #     title = li.xpath('./h2/a/@title').extract_first()
        #     link = li.xpath('./h2/a/@href').extract_first()
        #     brief = ''.join(li.xpath('./text()').extract()).replace('\n', '')
        #     # date = re.findall(r'\d+-\d+-\d+', li.xpath('./p/text()').extract_first())[0]
        #     print(title)
        #     print(link)
        #     print(brief)
        # print(date)
        # print('-'*50)

        # li_list = response.xpath("//div[@class='sear_app']/dl[1]")
        # for li in li_list:
        #     file_urls = li.xpath("//a[@class='btn_android']/text()")
        #     # file_urls = li.xpath("./dd/h3/a/@href").extract_first()
        #     print(file_urls,'2222222222222222222222')
        # yield scrapy.Request(url='https://www.liqucn.com/rj/20089.shtml', callback=self.detail_parse)

        # li_list = response.xpath("//ul[@id='j-search-list']/li[1]")
        # print(li_list)
        # for li in li_list:
        #     app_src=li.xpath("//div[@class='icon']/a/img/@src").extract_first()
        # app_name=li.xpath("//div[@class='icon']/a/img/@alt").extract_first()
        # app_number=li.xpath("//em/span/text()").extract_first()
        # app_size=li.xpath("//span[@class='size']/text()").extract_first()
        # app_brief=li.xpath("//span[@class='brief']//text()").extract_first()
        # print(app_src)
        # print(app_name)
        # print(app_number)
        # print(app_size)
        # print(app_brief)

    # -------------------------
    # tengxun
    # -------------------------
    # app_info_list_all = json.loads(response.text)['obj']['appDetails']
    # print(app_info_list_all[0])

    # -------------------------
    # baidu
    # -------------------------
    # li_list=response.xpath("//ul[@class='app-list']/li[1]")
    # # print(li_list)
    # for li in li_list:
    #     # extract_first()
    #     app_src=li.xpath("//div[@class='icon']/a/img/@src").extract_first()
    #     app_name=li.xpath("//div[@class='icon']/a/img/@alt").extract_first()
    #     app_number=li.xpath("//em/span/text()").extract_first()
    #     app_size=li.xpath("//span[@class='size']/text()").extract_first()
    #     app_brief=li.xpath("//span[@class='brief']//text()").extract_first()
    #     print(app_src)
    #     print(app_name)
    #     print(app_number)
    #     print(app_size)
    #     print(app_brief)

    # li_list = response.xpath("//div[@class='chapter-wrap']/div/a")
    # for li in li_list:
    #     title = li.xpath("./@title").extract_first()
    #     link = li.xpath("./@href").extract_first()
    #     print(title)
    #     print(link)
    # pass
    # linkList = [
    #     {
    #         "app_name": "//div[@class='app-info flt']/ul/li[2]/p[1]/span[@class='title']/text()",
    #         "list_xpath": "//div[@class='list-game-app dotline-btn nofloat']/div[@class='game-info-ico']/a/@href",
    #         "downNum": "//div[@class='app-info flt']/ul/li[2]/p[1]/span[@class='grey sub']/text()",
    #         "app_type": "",
    #         "domain": "https://appstore.huawei.com/",
    #         "file_urls": "//a[@class='mkapp-btn mab-download']/@onclick",
    #         "update_time": "//div[@class='app-info flt']/ul[2]/li[2]/span/text()",
    #         "charset": "utf-8",
    #         "icon": "//div[@class='app-info flt']/ul/li/img/@src"
    #     }]
    # print(linkList)

    def detai_parse(self, response):
        pass
        # dum_list = response.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[3]/a[1]/@href")
        # print(dum_list)
        # title=response.xpath("//div[@class='intro-titles']/h3/text()").extract_first()
        # update_time=response.xpath("/html/body/div[6]/div[1]/div[5]/div[1]/div[2]/text()").extract_first()
        # update_time=response.xpath("//div[@class='cc_cursor']/div[1]/div[2]/text()").extract_first()
        # print(title)
        # print(update_time)
        # print(response.text)
        # with open('bd.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # li_list = response.xpath('//div[@id="appQrcode"]').extract()
        # li_list = response.xpath('//div[@class="product-btn-container"]/a/text()')
        # print(li_list)
