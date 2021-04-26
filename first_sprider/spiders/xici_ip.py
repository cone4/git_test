# import time
# import requests
#
#
# def inspect_ip(ipprot):
#     time.sleep(1)
#     herder = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Upgrade-Insecure-Requests': '1'
#
#     }
#
#     url = 'https://www.baidu.com'
#     proxies = {"http": "http://" + str(ipprot)}
#     request = requests.get(url, headers=herder, proxies=proxies)
#     if request.status_code == 200:
#         print('可用代理' + ipprot)
#         # if Db.r.llen('Iplist') <= 50:
#         #     Db.add_ip(ipprot)
#         # # Alt.iplist.append(ipprot)
#         #
#         # else:
#         #     Db.add_ips(ipprot)
#     else:
#         print('不可用代理' + ipprot)
#
#
# if __name__ == '__main__':
#     inspect_ip()



