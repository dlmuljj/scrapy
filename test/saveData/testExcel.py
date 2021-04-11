# -*- coding = utf-8 -*-
# @Time  :21/4/11 21:25
# @Author: 吕佳杰
# @File  :testExcel.py
# @Software:PyCharm

# 我们要引用另一个文件夹下的内容时，需要把路径加进来
# import sys
# sys.path.append('../getData')
import xlwt


from get_title_bs_all import get_data

def save_excel(datalist, path):
    print('-'*20 + 'Data is ready to save...')

    # 创建一个EXCEL文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 新建一个工作表sheet
    sheet = book.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)

    # 我们定义一行标题名字
    # 'name,link,img,common,rating,comment,inq'
    col = ('电影名称', '电影详情链接', '图片链接', '概况', '评分', '评价数', '一句话描述')

    len_row = len(datalist)
    len_col = len(col)

    # 定入数据到excel表格中的sheet中
    # 第一步，写入第一行表格头
    for i in range(len_col):
        sheet.write(0,i,col[i])

    # 第二步，写入表中数据
    for i in range(len_row):
        print('正在写入第%d条数据'%(i+1))
        data = datalist[i]
        for j in range(len_col):
            sheet.write(i+1,j,data[j])

    book.save(path)
    print('数据已经保存到EXCEL表格中。。。。')


if __name__ == '__main__':
    path = 'movie250.xls'
    datalist = get_data()
    save_excel(datalist,path)


