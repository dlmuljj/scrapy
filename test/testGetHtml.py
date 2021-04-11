# -*- coding = utf-8 -*-
# @Time  :21/3/29 23:36
# @Author: 吕佳杰
# @File  :testGetHtml.py
# @Software:PyCharm














import urllib.request
import urllib.parse

url = 'https://www.zhihu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    # 'Cookie': '_zap=7851f616-56fa-4a23-a206-0dfade8e3253;  \
    #             _xsrf=LxbFQMTmZ9i3z6R8fr4tmbjYTbzi6TiO;  \
    #            d_c0="ANAQ25bMLRGPTqyuPXuaXLFmmXqwXeFtPk0=|1587911306"; \
    #            _ga=GA1.2.1188320851.1587911307; \
    #            z_c0="2|1:0|10:1607664158|4:z_c0|92:Mi4xSndNYkFBQUFBQUFBMEJEYmxzd3RFU1lBQUFCZ0FsVk5IbERBWUFDcGZWMGlhN1JHV0E4ZWpWeW5UMW0yTmdvWkJ3|4f9b3eadd824deec01064afd855ee233e7dc176902fef567d09197e2da274023"; \
    #            q_c1=7664375f4ec44aaeb95c7d9339c801d3|1610718061000|1587911484000; \
    #            Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1614588474,1614588546,1615820143,1616425496; \
    #            tst=r; \
    #            SESSIONID=j3nXxIOpR162jBr9Am1fKbFE7rNjkWBG6bFDh4uvrK6; \
    #            JOID=UlsUC03YSKC4sNiHFNBd-QvFEhoHsXnH7s6Sym2MepSD1Jz2L3JYwNC12YwTF0jlNfLLYq-PDzbIU_4cE8p3whg=; \
    #            osd=VF0cCkzeTqi5sd6BHNFc_w3NExsBt3HG78iUwmyNfJKL1Z3wKXpZwdaz0Y0SEU7tNPPNZKeODjDOW_8dFcx_wxk=; \
    #            KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1617370563|1617370024'



    }
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))






#测试post请求
# http://httpbin.org/post
#封装一些数据给他们
# import urllib.parse
# data = bytes((urllib.parse.urlencode({'hello':'world'})),encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))