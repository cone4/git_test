# # -*- coding: utf-8 -*-
# # @Time    : 2021/4/9 下午1:28
# # @Author  : Tian Jin wu
# # @FileName: ip_ceshi.py
# import requests
# from fake_useragent import UserAgent
# from .kdl_ip import can_use
#
# # url = 'http://zhushou.360.cn/search/index/?kw=QQ'
# url = 'https://www.baidu.com'
# headers = {"User-Agent": UserAgent().random}
# for ip in can_use:
#     proxies = {"https": "http://" + str(ip)}
#     print(proxies)
#     r = requests.get(url, headers=headers, verify=False, proxies=proxies, timeout=10)
#     print(r.content)
