# -*- coding = utf-8 -*-
# @Time  :21/3/29 23:26
# @Author: 吕佳杰
# @File  :testGetUrl.py
# @Software:PyCharm

# https://movie.douban.com/top250?start=225&filter=
for i in range(1,11,1):
    a = (i-1)*25 + 1

    head = 'https://movie.douban.com/top250?start='
    tail = '&filter='
    url = head + str(a) +tail

    print(i,url)

