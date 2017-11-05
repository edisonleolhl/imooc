## baike_spider

- 慕课网学到的简单爬虫 demo，课程地址：http://www.imooc.com/learn/563

- 使用爬虫三大模块进行爬取：URL管理器、网页下载器（urllib）、网页解析器（BeautifulSoup）

- 最后进行输出，将爬取到的百度百科词条的 URL、标题、摘要，输出到 output.html 中。

- 具体介绍请看笔记：http://www.jianshu.com/p/8b2712d8b29b

## IEEEXplore_get_article

- 利用校园网登录 IEEE Xplore 网站（已有校园账户），因为该网站采用异步加载，文章列表爬取困难，所以利用 自动化工具 selenium 模仿浏览器爬取某位学者的所有文章（名字，来源，关键字）。

- while 循环内是翻页操作，如果到了最后一页则跳出循环

- 最后把数据保存为 csv 格式