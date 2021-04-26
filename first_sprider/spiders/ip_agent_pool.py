# import requests
# import time
# from fake_useragent import UserAgent
# from lxml import etree
#
#
# def Ip_agen_89():
#     for page in range(1, 2):
#         time.sleep(1)
#         print('==========正在获取第{}页数据============'.format(str(page)))
#         headers = {
#             "User-Agent": UserAgent().random
#         }
#         url = 'http://www.66ip.cn/' + str(page) + '.html'
#         # print(url)
#         # url = 'https://www.89ip.cn/index_' + str(page) + '.html'
#         # print(url)
#         res = requests.get(url=url, headers=headers)
#         html_data = etree.HTML(res.text)
#         tr_list = html_data.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/tr')
#         for tr in tr_list:
#             ip = tr.xpath('./td[1]/text()').extract_first()
#             # 端口
#             ip_port = tr.xpath('./td[2]/text()').extract_first()
#             # 运营商
#             # ip_operator = tr.xpath('./td[3]/text()').extract_first()
#             # ip类型
#             ip_type = tr.xpath('./td[4]/text()').extract_first()
#             print(ip)
#             print(ip_port)
#             print(ip_type)
#
#
# Ip_agen_89()
