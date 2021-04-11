#-*- codeing = utf-8 -*-
#@Time  :2020/11/3 21:31
#@Author: 吕佳杰
#@File  :spider.py
#@Software:PyCharm

from bs4 import BeautifulSoup           #网页解析，获取数据
import re                               #正则表达式，进行文字配置
import urllib.request, urllib.error     #制定URL，获取网页数据
import xlwt                             #进行excel操作
import sqlite3                          #进行SQLite数据操作




#打main自动补全,ctrl+/ 自动注释选择的行

def main():
    baseurl = "https://movie.douban.com/top250?start="
#1.爬取网页
    datalist = getData(baseurl)
    print(len(datalist))
    #savepath = "豆瓣电影Top250.xls"
    #askURL(baseurl)
    dbpath = "movie.db"
    #saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)
    # getData(baseurl)




#影片的链接
findlink = re.compile(r'<a href="(.*?)">')   # 表示 <a href="www.baidu.com">
#影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S忽略里面的换行符,让换行符包含在里面
# <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">

#影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评论数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#影片概况
findInq = re.compile(r'<span class="inq">(.*?)</span>')
#影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getData(baseurl):
    datalist = []
    print('开始数据爬取--------------')
    for i in range(0,10):  #调用获取页面信息的函数10次，每次25条
        url = baseurl + str(i*25)
        html = askURL(url) #保存获取到的网页原码
        print('爬取第----%d----个页面'%(i))
        print(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):   #查找符合要求的字符串形成列表
            #print(item)  #测试，查看电影item
            data = []  #保存一部电影的所有信息
            item = str(item)
            #print('____item____')
            link = re.findall(findlink, item)[0]   #组一个链接的库,findlink是规则,规则用来匹配item
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]  #添加图片
            #print(imgSrc)
            data.append(imgSrc)

            title = re.findall(findTitle,item)       #片名可能只有一个中文名，也可能都有
            if(len(title) == 2):
                ctitle = title[0]                    #添加中文名
                data.append(ctitle)
                otitle = title[1].replace("/","")  #无关内容去掉
                data.append(otitle)                  #添加外国名
            else:
                data.append(title[0])
                data.append(" ")                   #外文名，留空，保持格式

            rating = re.findall(findRating,item)[0]
            data.append(rating)                     #添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)                   #添加评分人数

            inq = re.findall(findInq,item)
            if(len(inq) !=0):
                inq = inq[0].replace("。","")  #去掉句号
                data.append(inq)                        #添加概述
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)/>(\s+)?',' ',bd) #去掉br
            bd = re.sub('/',' ',bd)                #去掉/
            data.append(bd.strip())                #去掉前后的空格

            datalist.append(data)   #把处理里的一部电影信息放进datalist

    print(len(datalist))
    return datalist


#得到指定一个URL的网页内容
def askURL(url):
    head = {   #模拟浏览器头部信息向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Cookie":'bid=2CTnZrkCbtk; __yadk_uid=UjpNNw0XIwn9ChowSHWvzyEBuXQetuz1; douban-fav-remind=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1607951500%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftop250%22%5D; __gads=ID=316a4a6e3ed6f924-22a2773e32c500bb:T=1607951501:RT=1607951501:R:S=ALNI_MZYm-ZfaQHKHBDnnq20LhtEWrBEiw; dbcl2="160797671:BkZ1xuinaYM"; ck=lavV; __utma=30149280.401170701.1595393204.1599037878.1607951500.3; __utmb=30149280.0.10.1607951500; __utmc=30149280; __utmz=30149280.1607951500.3.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.751946792.1595393204.1595393204.1607951500.2; __utmb=223695111.0.10.1607951500; __utmc=223695111; __utmz=223695111.1607951500.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.4cf6=2cf8b86585bf66bd.1595393204.3.1607951989.1607252491.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0'
    }


    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器
    reqest  = urllib.request.Request(url, headers=head)

    html = ""
    try:
        response = urllib.request.urlopen(reqest)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)

        if hasattr(e,'reason'):
            print(e.reason)
    return html
#3.保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建EXCEL文件
    sheet = book.add_sheet('豆瓣电影250',cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接','图片链接','中文名','外文名','评分','评价数','概况','相关信息')

    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("正在写入第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])


    book.save(savepath)       #保存数据

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    print(len(datalist))
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250 (info_link,pic_link,cname,ename,score,rated,introduction,info)
                values(%s)'''%",".join(data)   #用连接符拼接%s的内容
        #print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print('...正在存入DB数据库')

def init_db(dbpath):
    sql = '''
        create table movie250 
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar ,
            ename varchar ,
            score numeric ,
            rated numeric ,
            introduction text,
            info text
        );
    
    
    '''
    #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':  #当程序执行时，
#调用函数
    main()
    #init_db('movetest.db')
    print('爬取完毕！')