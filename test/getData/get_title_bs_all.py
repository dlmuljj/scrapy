# -*- coding = utf-8 -*-
# @Time  :21/4/4 21:16
# @Author: 吕佳杰
# @File  :get_title_string.py
# @Software:PyCharm

import re
from bs4 import BeautifulSoup

def get_content():
    with open('demo_html.html', mode='r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')
    content = soup.find_all('div', class_='item')
    return content

def get_link(content):
    linktag = content.find('a')
    link = linktag.get('href')
    return link

def get_img(content):
    imgtag = content.find('img')
    img = imgtag.get('src')
    return img

def get_name(content):
    nametag = content.find('span', class_='title')
    name = nametag.text
    return name

def get_common(content):
    commontag = content.find('p', class_="")
    # print(commontag)
    common = commontag.text
    common = common.strip()
    common = common.split('\n')
    common[1] = common[1].strip()
    return common

def get_rating(content):
    ratingtag = content.find('span', class_="rating_num")
    rating = ratingtag.text
    return rating

def get_comment(content):
    commenttag = content.find('span', class_=None, content=None)
    # print(commenttag)
    comment = commenttag.text
    comment = comment.replace('人评价', '')
    return comment

def get_inq(content):
    inqtag = content.find('span', class_="inq")
    inq = inqtag.text
    return inq

def get_data():
    datalist = []
    content = get_content()
    for movie in content:
        link = get_link(movie)
        img = get_img(movie)
        name = get_name(movie)
        common = get_common(movie)
        rating = get_rating(movie)
        comment = get_comment(movie)
        inq = get_inq(movie)
        data = [name, link, img, common, rating, comment, inq]
        datalist.append(data)
    return datalist



# if __name__ == '__main__':
#     datalist = []
#     content = get_content()
#     # comment = get_comment(content[0])
#     # print(comment)
#     # print(content[0])
#     # link = get_link(content[0])
#     # print(link)
#     for movie in content:
#         link = get_link(movie)
#         img  = get_img(movie)
#         name = get_name(movie)
#         common = get_common(movie)
#         rating = get_rating(movie)
#         comment = get_comment(movie)
#         inq = get_inq(movie)
#         data = [name,link,img,common,rating,comment,inq]
#         datalist.append(data)
#     # print(len(datalist))
#
#     # print(len(datalist[1][3]))
#     # print(datalist[1][3])
#     # for i,item in enumerate(datalist[0:4]):
#     #     print('-'*20 +'No. {0}'.format(i) +'-'*20)
#     #     for j,_ in enumerate(item):
#     #         print('index {0}: {1}'.format(j,_))











