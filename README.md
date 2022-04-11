## 需求分析
项目功能分为三步：

1. 使用python进行爬虫，并将数据存入文件和数据库。
2. 使用某种编程语言连接数据库，并从数据库提取并生成JSON数据，以便之后的小程序通过api调用形式读取JSON数据。
3. 微信小程序至少需实现数据的查找功能，并有一定的排版。

## 项目实现

### 语言采用

考虑时间较短，所以应从快速上线和代码量的角度选择语言。数据库采用MySQL，爬虫语言采用python，API编写采用PHP语言。
### 环境配置

MySQL采用8.0.21版本，并开启native_password认证方式。
Python采用较为使用较为广泛的Python3.7，开发工具采用PyCharm2021.1.3。
PHP采用PHP7.3，配套服务器采用Apache2.4，开发工具采用PhpStorm2021.2。
微信小程序开发工具采用微信开发者工具Stable 1.05.2108130。

### 爬虫实现

爬虫目标网址：https://www.meishij.net/

> 发现其下的：
> > 1.https://www.meishij.net/chufang/diy/?&page=1
> >
> > 2.https://www.meishij.net/china-food/caixi/?&page=1
> >
> > 3.https://www.meishij.net/china-food/xiaochi/?&page=1
> >
> > 4.https://www.meishij.net/chufang/diy/guowaicaipu1/?&page=1中的page参数可以被爬虫给。

使用Python的request模块进行初步尝试，发现网站未对请求头进行检查，即无需伪装。
对网站元素进行分析，发现网站的评论和人气几乎均为0或1，并没有爬取价值。

**具有爬取的价值的是**菜谱的标题和具体菜谱的连接。通过F12打开控制台审查元素发现：<a target="_blank" href="具体菜谱链接" title="菜谱的标题" class="big">
同时发现，页面底部有提示“共有XX页”，因此可以根据不同的页数来进行爬虫。
进行翻页操作发现，本页与下一页相比，区别仅在url的page参数加上1。
综上所述，先构造正则表达式，提取一页中的菜谱标题和具体菜谱网址，再构造正则表达式，分析总页数，并依据总页数进行爬虫，最后，使用for循环爬取每个存在内容的页面。
 而在数据保存时，同时将数据保存到pandas和MySQL数据库中。

### API编写

首先使用**PHP PDO**连接数据库，并查询数据，接着将数据转换为JSON数据传向客户端。也可规定请求头格式从而使得API接口更加规范。
最终生成的接口为：http://localhost/菜谱种类.php

### 小程序设计

具体功能分为数据查看和查询。
数据查看点击首页中的家常菜谱、中华菜系、各地小吃、外地菜谱调用PHP接口查看菜谱，点击菜名即可进入相关网页查看具体做菜过程。
查询则调用了原网站的查询接口进行查询。

## 目录结构说明

php文件夹为php接口

python文件夹为python爬虫

weixin为微信小程序

