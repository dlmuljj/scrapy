# -*- coding = utf-8 -*-
# @Time  :21/4/4 21:16
# @Author: 吕佳杰
# @File  :get_title_string.py
# @Software:PyCharm

#用"上下文管理器"-"with"方法去打开html文档

with open('demo_html.html', mode='r', encoding='utf-8') as f:
    # a = f.readline()   # 读取第一行，文本形式
    b = f.read()         #读取所有，并以文本形式
    # c = f.readlines()   # 读取所有行，并以列表行式


#如果网页特别规范，行数固定，可以用readlines去读取，通过列表的切片去定位，然后利用字符串的方法或者正则表达式去精确控制
#常用方法有strip(),replace(),split(),join()
# print(1,2,3)
# print(b[14],b[16])

# print('a=readline()的类型为',type(a),'长度为：',len(a))
print('a=read()的类型为',type(b),'长度为：',len(b))
# print('a=readlines()的类型为',type(c),'长度为：',len(c))
# print(c)
# title = c[8].strip().replace(' ','')
# print(title)
# name1 = c[279].strip()
# print(name1)
# film1=c[274:315]
# print(film1)

