# # # # -*- coding: utf-8 -*-
# # # #
# # # a=[1,2,3]
# # # dict = {"name": {"360":'1'}, "list_xpath": '11111'}
# # #
# # # dict['name']["360"]=a
# # # d=dict['name']["360"]
# # # # d=
# # # print(a)
# # # print(dict)
# # # # print(type(xpath_dict))
# # # # print(xpath_dict['name'])
# # # # b = {"xpath_dict": None}
# # # b = b
# # # print(b)
# # # response.meta["list_item"]["file_urls"] = response.meta["list_item"][""]
# #
# import json
# import re
#
# # url = 'http://zhushou.360.cn/search/index/?kw=wx&page=25'
# # url = ['/category/0','/category/15','/category/27']
# # for i in url:
# #     res=re.findall(r"[^/category]+(?!.*/)",i)
# #     print(res)
# #
# #
# # hraders = {
# #     'Host': 'www.wandoujia.com',
# #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
# #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# #     'Accept-Encoding': 'gzip, deflate, br',
# #     'Connection': 'keep-alive',
# #     'Upgrade-Insecure-Requests': '1',
# # }
#
#
# dict = {"count": 2000, "data": [{"appId": 1265396, "displayName": "捕鱼大作战-柳岩代言",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/016f5cc1ec9874e0cacaaef62fd30ca106cd6054c",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.tuyoo.fish3d.mi"},
#                                 {"appId": 569773, "displayName": "欢喜斗地主",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0fdd85a90836140109cb38abc549536debe23147c",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.qileyx.ddz.mi"},
#                                 {"appId": 684754, "displayName": "在我们之间",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0af564056e8352b1fc68d42d25e3a2f04ec42dff6",
#                                  "level1CategoryName": "休闲创意", "packageName": "com.innersloth.spacemafia.mt"},
#                                 {"appId": 1217380, "displayName": "多乐斗地主",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/042e6558490e8564a84b922e1e9d1d169a540b10a",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.duole.doudizhuhd.mi"},
#                                 {"appId": 421915, "displayName": "汤姆猫跑酷",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0bc3195962ee34fec3d977ea376489d79a617c882",
#                                  "level1CategoryName": "跑酷闯关", "packageName": "com.outfit7.talkingtomgoldrun.mi"},
#                                 {"appId": 691650, "displayName": "左轮手枪模拟器",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/028b1f4b87a7d4f281a47b14cabb22f691ed6d956",
#                                  "level1CategoryName": "休闲创意", "packageName": "com.eweapons.revolvergunssim.mg"},
#                                 {"appId": 623587, "displayName": "猫和老鼠",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0bdae5bf3187318f4832f2b2b84d543600d4274bf",
#                                  "level1CategoryName": "网游RPG", "packageName": "com.netease.tom.mi"},
#                                 {"appId": 106432, "displayName": "三国杀",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0ef92dabfab8945fa929b4df3d10079312beb5ec4",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.bf.sgs.hdexp.mi"},
#                                 {"appId": 75420, "displayName": "天天象棋",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/02e9a422fa8fa3029cf1769354804b69c7342c700",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.tencent.qqgame.xq"},
#                                 {"appId": 1185110, "displayName": "口袋之旅-口袋妖怪复刻",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/09e7c1461346c46a8394df98e90651e34882544dd",
#                                  "level1CategoryName": "网游RPG", "packageName": "com.maichi.kdzl.mi"},
#                                 {"appId": 509823, "displayName": "狼人杀",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/032c65d3e2ad8680548369bbd083e8f12b14212b6",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.netease.lrs.mi"},
#                                 {"appId": 1302530, "displayName": "粉末游戏",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/04eac75ba6ae544613108d37a27b5d01c3a280db1",
#                                  "level1CategoryName": "模拟经营", "packageName": "jp.danball.powdergameviewer.bnn"},
#                                 {"appId": 365301, "displayName": "欢乐真人麻将",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0b78a51272414e94abd0a2507630d98a737429d5c",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.mengmi.majiang.mi"},
#                                 {"appId": 296916, "displayName": "皇室战争",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/00ccc5d4a45645e1eeb4030e38a6a6df0bf426eaa",
#                                  "level1CategoryName": "战争策略", "packageName": "com.supercell.clashroyale.mi"},
#                                 {"appId": 48217, "displayName": "天天酷跑",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/02b58db73cc95413893929771a83da84b561eca63",
#                                  "level1CategoryName": "跑酷闯关", "packageName": "com.tencent.pao"},
#                                 {"appId": 649733, "displayName": "忍者必须死3-春日校园祭",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/01a9215026d514c3223975d620cf1cbdd7aa3c54e",
#                                  "level1CategoryName": "跑酷闯关", "packageName": "com.pandadastudio.ninjamustdie3.mi"},
#                                 {"appId": 630604, "displayName": "明日之后-电影联动",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0aa218fb89b334544894ae10e5292fab6733d8401",
#                                  "level1CategoryName": "网游RPG", "packageName": "com.netease.mrzh.mi"},
#                                 {"appId": 25940, "displayName": "地铁跑酷",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/01e297902efe640ccbfc74d2c230e410e0f53b609",
#                                  "level1CategoryName": "跑酷闯关", "packageName": "com.kiloo.subwaysurf"},
#                                 {"appId": 1255332, "displayName": "斗罗大陆：武魂觉醒-送极品魂骨",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0804b90e2ee8b42b089b719ebb65586242960add3",
#                                  "level1CategoryName": "网游RPG", "packageName": "com.hnzh.dldlwhjx.mi"},
#                                 {"appId": 79963, "displayName": "炉石传说",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/094fa4e6d6c21180a500c0e2668effc809343fd67",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.blizzard.wtcg.hearthstone"},
#                                 {"appId": 106181, "displayName": "腾讯桌球",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/02db9e49d8c1e42ce3d9b36c53bfcb0abb5318aca",
#                                  "level1CategoryName": "棋牌桌游", "packageName": "com.tencent.pocket"},
#                                 {"appId": 661497, "displayName": "新斗罗大陆",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/097627489a36f48b80f10fc64005ac8339b956c0a",
#                                  "level1CategoryName": "网游RPG", "packageName": "com.qidian.dldl.mi"},
#                                 {"appId": 679100, "displayName": "枪械模拟器",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/075104f52d0e81b9dc99aeeea4b6c76409041dbdd",
#                                  "level1CategoryName": "模拟经营",
#                                  "packageName": "com.eweapons.ultimateweaponsimulator.dbzq.m"},
#                                 {"appId": 21629, "displayName": "神庙逃亡2-元气大作战！",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/07ac55016ec2f48bbbb13d198161bea3cd410e9ca",
#                                  "level1CategoryName": "跑酷闯关", "packageName": "com.imangi.templerun2"},
#                                 {"appId": 732019, "displayName": "快游戏",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/01557491567f0f5192c74b78a1e1670824e417bfb",
#                                  "level1CategoryName": "休闲创意", "packageName": "com.h5gamecenter.h2mgc"},
#                                 {"appId": 801638, "displayName": "狂野飙车9：竞速传奇",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/024482299f94d4badba017bfdd9d7a5d8729b4e73",
#                                  "level1CategoryName": "赛车体育", "packageName": "com.aligames.kuang.kybc.mi"},
#                                 {"appId": 269712, "displayName": "乐乐捕鱼-任达华正版代言",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/061e005229d164a47251d4b26cddca6f5f49e0117",
#                                  "level1CategoryName": "休闲创意", "packageName": "com.youkuss.lelecatchfish.mi"},
#                                 {"appId": 793914, "displayName": "三国志&middot;战略版-水攻火战",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0f43a5d9a4d1d44919f5bba3c3daf78018d91efaa",
#                                  "level1CategoryName": "战争策略", "packageName": "com.aligames.sgzzlb.mi"},
#                                 {"appId": 1067363, "displayName": "匠木",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0b534866b32764fdf8cf08814fd4dad5f7bf3b9dd",
#                                  "level1CategoryName": "休闲创意", "packageName": "com.leiting.jm.mi"},
#                                 {"appId": 844226, "displayName": "保卫萝卜3",
#                                  "icon": "http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/096df35d59e8a46d8235f99a7fbc80162955c30cd",
#                                  "level1CategoryName": "塔防迷宫", "packageName": "com.feiyu.carrot3.mi"}]}
#
# # a=[item[key] for item in dict for key in item]
#
# dict = dict["data"]
# for item in dict:
#     for v, k in item.items():
#         if v == "packageName":
#             print(k)
#
# # for values,key in item:
# #     if values =="packageName":
# #         print(key)
# a = 4
# #
# page = [page for page in range(1, 7)][::-1][:a]
#
# print(page)

# a = ["QQ"]
# b = "手机QQ影音"
# for i in a:
#     if i in b:
#         print('1')
#     else:
#         print('2')

import re

# a = '?table_flag=app&urlos=&words=QQ&page=4'
# # res = re.findall(r"[^&page=]", a)
# res = a.split("&page=")[1]
# print(int(res))
# for i in range(1, 6)[::-1][:1]:
#     print(i)
