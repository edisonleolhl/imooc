from selenium import webdriver
import time
import re
import csv
from pprint import pprint

driver = webdriver.Chrome(executable_path='chromedriver.exe')
article_links = []
article_names = []
article_sources = []
article_keywords = []

# URL 特殊字符转义
# "\"单反斜杠  %5C
# "|"      %7C
# 回车  %0D%0A
# 空格  %20
# 双引号 %22
# "&" %26

pageNumber = 1
while(True):
    driver.get(
        'http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22Authors%22:Zhang%20Bo)&refinements=4224983357&matchBoolean=true&pageNumber=' + str(pageNumber) + '&searchField=Search_All')
    time.sleep(5)
    print("start to check if this is the last page !!!")
    try:
        driver.find_element_by_css_selector("p.List-results-none--lg.u-mb-0") # if this is NOT the last page, this will raise exception
    except Exception as e:
        print("This page is good to go !!!")
    else:
        print("The last page !!!")
        break

    article_name_ele_list = driver.find_elements_by_css_selector("h2 a.ng-binding.ng-scope")
    for article_name_ele in article_name_ele_list:
        article_name = article_name_ele.text
        article_link = article_name_ele.get_attribute('href')
        article_names.append(article_name)
        print("article_name = ", article_name)
        article_links.append(article_link)
        print("article_link = ", article_link)

    article_source_ele_list = driver.find_elements_by_css_selector("div.description.u-mb-1 a.ng-binding.ng-scope")
    for article_source_ele in article_source_ele_list:
        article_source = article_source_ele.text
        article_sources.append(article_source)
        print("article_source =", article_source)

    pageNumber += 1

# get into articles page
for article_link in article_links:
    driver.get(article_link + "keywords")
    article_id = re.findall("[0-9]+", article_link)[0]
    time.sleep(3)

    # get into keywords page
    dic = {}
    dic['IEEE Keywords'] = []
    dic['INSPEC: Controlled Indexing'] = []
    dic['INSPEC: Non-Controlled Indexing'] = []
    dic['Author Keywords'] = []

    keywords_type_list = driver.find_elements_by_css_selector("li.doc-keywords-list-item.ng-scope strong.ng-binding")  # ['IEEE Keywords', 'INSPEC: Controlled Indexing', 'INSPEC: Non-Controlled Indexing', 'Author Keywords']
    for i in range(len(keywords_type_list)):
        # 定位每个关键字种类，然后提取该关键字种类下的所有关键字
        li = []
        keywords_ele_list = driver.find_elements_by_xpath(
            ".//*[@id=" + article_id + "]/div/ul/li[" + str(i+1) +"]/strong/following-sibling::*/li/a")
        for j in keywords_ele_list:
            li.append(j.text)
        dic[keywords_type_list[i].text] = li
    article_keywords.append(dic)

driver.close()

# already get all data, now output to the csv file
pprint(article_keywords)
with open("ieee_zhangbo_.csv", "w", newline="")as f:
    csvwriter = csv.writer(f, dialect=("excel"))
    csvwriter.writerow(['article_name', 'article_source', 'article_link',
                            'IEEE Keywords', 'INSPEC: Controlled Indexing',
                            'INSPEC: Non-Controlled Indexing', 'Author Keywords'])
    for i in range(len(article_names)):
        csvwriter.writerow([article_names[i], article_sources[i], article_links[i],
                            article_keywords[i]['IEEE Keywords'], article_keywords[i]['INSPEC: Controlled Indexing'],
                            article_keywords[i]['INSPEC: Non-Controlled Indexing'], article_keywords[i]['Author Keywords']])