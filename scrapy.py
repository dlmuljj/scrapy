# -*- coding = utf-8 -*-
# @Time  :21/3/29 22:53
# @Author: 吕佳杰
# @File  :scrapy.py.py
# @Software:PyCharm

import time

def scrapy():
    datapath = './data.xls'
    # 1.得到爬取的url
    url = getUrl()
    # 2.模拟浏览器访问url,并获取到html
    htmllist = getHtml(url)
    # 3.根据得到的html结构提取信息
    datalist = getData(htmllist)
    # 4.存储得到的信息
    saveData(datalist, datapath)


# 1.得到爬取的url
def getUrl():
    url = []
    for i in range(1, 11, 1):
        a = (i - 1) * 25 + 1
        # print(a)  #可以先打打印看看结果对不对
        head = 'https://movie.douban.com/top250?start='
        tail = '&filter='
        urlTemp = head + str(a) + tail
        url.append(urlTemp)
    print('1st Step : url获取完毕')
    return url






# 2.模拟浏览器访问url,并获取到html
def getHtml(usr):
    html = []
    time.sleep(1)
    print('2nd Step : html获取完毕')
    return html



# 3.根据得到的html结构提取信息
def getData(html):
    data = []
    time.sleep(1)
    print('3rd Step : 提取数据完毕')
    return data

# 4.存储得到的信息
def saveData(data,datapath):
    time.sleep(1)
    print('4th Step : 数据已保存，爬虫结束')






if __name__ == '__main__':

    scrapy()















