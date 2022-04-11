import requests
import re
import pandas as pd
import pymysql

urls = {"家常菜谱": 'https://www.meishij.net/chufang/diy',
        "中华菜系": 'https://www.meishij.net/china-food/caixi',
        "各地小吃": 'https://www.meishij.net/china-food/xiaochi',
        "外国菜谱": 'https://www.meishij.net/chufang/diy/guowaicaipu1'}

types = ["家常菜谱", "中华菜系", "各地小吃", "外国菜谱"]

hostname = '192.168.50.131'
port = 3306
username = 'root'
passwd = '123456'
dbname = 'cookie_info'
charset = 'utf8'

'''
int_worm:网络爬起jams及
@url:输入一个待爬取网站，String类型
@return:返回爬到网页的内容，String类型
'''


def int_worm(url):
    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        r.raise_for_status()  # 当返回状态码不为200时，弹出错误
        return r.text
    except requests.HTTPError:
        print("网络连接出现异常")
        exit(0)


'''
count_page:得到需爬取网页的总页数
@url:输入一个待爬取网页的网站，String类型
@return:返回需爬取的总页数,Integar类型
'''


def count_page(url):
    html_content = int_worm(url + '/')
    pattern = re.compile(r'共\d*页')
    result = pattern.findall(html_content)
    if len(result) == 0:  # 无页面总数提示时，返回1页
        return 1
    return int(result[0][1:-1])


'''
get_caipu:爬取每个种类的菜谱
@url:待爬取种类的起始地址，String类型
@return:返回所有菜，tuple、list类型[(,),(,)]
'''


def get_caipu(url):
    url_bottom = '/?&page='
    page_end = count_page(url) + 1  # 计算共需多少页
    cookie_dict = {}
    for i in range(1, page_end):
        print("正在爬取第{}页".format(i))
        print("当前爬取网址为:{}".format(url + url_bottom + str(i)))
        html_str = int_worm(url + url_bottom + str(i))
        # print(html_str)
        pattern = re.compile(r'<a target="_blank" href=".*" title=".*" class="big"')
        first_get = pattern.findall(html_str)
        titles = [re.compile(r'title=".*"').findall(i)[0][7:-13] for i in first_get]
        # print(first_get)
        # print(titles)
        hrefs = [re.compile(r'(href="[a-zA-Z0-9_/:?.]*)').findall(i)[0][6:] for i in first_get]
        # print(hrefs)

        for i in range(len(titles)):
            cookie_dict[titles[i]] = hrefs[i]
        # print(cookie_dict)
    return cookie_dict


'''
save_to_file:将爬得的数据生成为csv文件
@cookie_dict:爬得的数据，dict类型
@file_name:保存的文件名,String类型
@:return:无返回值
'''


def save_to_file(cookie_dict, file_name):
    df = pd.Series(cookie_dict)
    try:
        df.to_csv(file_name+'.csv', index=True)
        print("已保存到当前目录下的{}文件".format(file_name+'.csv'))
    except IOError:
        print("文件保存出错")


def conn_mysql():
    db = pymysql.connect(host=hostname, port=port, user=username, passwd=passwd,
                         db=dbname, charset=charset)
    return db


def save_to_mysql(cookie_dict, tb_name):
    db = conn_mysql()
    cs = db.cursor()
    cs.execute("drop table if exists " + tb_name)
    sql = "CREATE TABLE " + tb_name + "(titles varchar(100),href varchar(200));"
    cs.execute(sql)
    for key, value in cookie_dict.items():
        sql_insert = "insert into " + tb_name + " values ('" + key + "','" + value + "');"
        cs.execute(sql_insert)
        db.commit()
        # print(cs.fetchone())


if __name__ == '__main__':
    # print(get_caipu('https://www.meishij.net/chufang/diy'))
    # print(get_caipu('https://www.meishij.net/china-food/xiaochi'))
    for type in types:
        cookie_dict = get_caipu(urls[type])
        save_to_file(cookie_dict, type)
        save_to_mysql(cookie_dict, type)

