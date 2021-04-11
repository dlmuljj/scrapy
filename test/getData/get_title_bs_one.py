# -*- coding = utf-8 -*-
# @Time  :21/4/4 21:16
# @Author: 吕佳杰
# @File  :get_title_string.py
# @Software:PyCharm
import re

from bs4 import BeautifulSoup
'''A data structure representing a parsed HTML or XML document.
BeautifulSoup是一个可以从html或xml文件中提取数据的Python库。
它能够通过你喜欢的转换器实现惯用的文档导航、查找、修改文档的方式。
在Python开发中，主要用的是BeautifulSoup的查找提取功能，修改功能很少使用
'''
# print(dir(BeautifulSoup))
# soup = BeautifulSoup('')

with open('demo_html.html',mode='r',encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html,features='html.parser')

# print(soup.lvjiajie)  #标签
# a = soup.html
# print(len(html))

# b = soup.html.title
# print(b)

# c = soup.ol
# print(len(c))
# print(type(c))

#

'''
html有一些唯一项可以帮助我们去定位有效数据区域
1.标签Tag
比如：title唯一, 没问题
***比如：head唯一，head作为一个块状元素，它里面包含很多内容
***比如：body唯一，body主为一个主体内容，它里面也包含嵌套很多子标签
比如：lvjiajie唯一，没问题
2.id号，绝对唯一，语法规范ID必须唯一
'''

'''
1.获取一块内容
'''

# soup.find_all("div",class_="item")
# find找到第一个匹配的选项
content = soup.find('div',class_='item')
# print(len(content))
# print(content)
# print(dir(content))

datalist = []

'''
    2. 提取子内容
    跟上一步一模一样的方法，进一步定位到具体我们想要的位置，再缩小一次。
    2.1 影片链接link
    2.2 影片图片img
    2.3 提取名字name
    2.4 影片概况common
    2.5 提取分数rating
    2.6 评论人数comment
    2.7 一句话评论inq 
'''
# 2.1 影片链接link
# 通过get方法去获取标签的属性
linktag = content.find('a')
link = linktag.get('href')
# print(link)

datalist.append(link)

# 2.2 影片图片img
imgtag = content.find('img')
img = imgtag.get('src')
# print(img)
datalist.append(img)

# 2.3 提取名字name
nametag = content.find('span',class_='title')
# print(nametag)
# name = nametag.get_text()
# getText 和get_text是一样的
name = nametag.text
# print(name)
# print(name)
datalist.append(name)


# 2.4 影片概况common
commontag = content.find('p',class_="")
# print(commontag)
common = commontag.text
common = common.strip()
common = common.split('\n')
common[1] = common[1].strip()
# print(common[0])
# print(common[1])
datalist.append(common)

# 2.5 提取分数rating
ratingtag = content.find('span',class_="rating_num")
rating = ratingtag.text
# print(type(rating))
# print(rating)
datalist.append(rating)

# 2.6 评论人数comment
# 我自己试出来了一种方法，用class = None
commenttag = content.find('span',class_=None, content=None)
comment = commenttag.text
# print(comment)
# comment = re.findall('\d+',comment)
# print(comment)
#也可以用替换将文字替换出去
comment = comment.replace('人评价','')
datalist.append(comment)


# 2.7 一句话评论inq
inqtag = content.find('span', class_="inq")
inq = inqtag.text
# print(inq)
datalist.append(inq)

# print(len(datalist))
print('第一个电影的详细信息爬取如下：')
for i,item in enumerate(datalist):
    print('index {0} : {1}'.format(i,item))


