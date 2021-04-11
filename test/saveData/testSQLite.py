# -*- coding = utf-8 -*-
# @Time  :21/4/11 21:38
# @Author: 吕佳杰
# @File  :testSQLite.py
# @Software:PyCharm
import sqlite3
from get_title_bs_all import get_data

# 操作难点：就是拼接一个sql语句

# 初始化一个数据库，名字呀，表格结构
def init_db(path):
    # 创建一个movie250的表格，并设备字段和主键
    # 'name,link,img,common,rating,comment,inq'
    sql = '''
        create table  if not exists movie250(
            id integer primary key autoincrement,
            name text,
            link text,
            img varchar ,
            common varchar ,
            rating numeric ,
            comment numeric ,
            inq text
        );
        '''
    # id,name,link,img,common,rating,comment,inq
    # 真正的创建过程
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
# 然后往数据库里写数据，这里要用到数据库操作相关的语句
def save_sqlite(datalist):
    # 链接数据库
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    len_row = len(datalist)
    len_col = len(datalist[0])

    for data in datalist:

        # 由于sqlite的特点，每个要插入的内容，需要用双引号括起来
        for index in range(len_col):
            data[index] = str(data[index]).replace("'",'').replace('"','')
            data[index] = '"' + data[index] + '"'
        sql = '''insert into movie250 (name,link,img,common,rating,comment,inq)
        values(%s)''' % ','.join(data)
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()






if __name__ == '__main__':
    path = 'movie250.db'
    datalist = get_data()
    init_db(path)
    save_sqlite(datalist)