#  -*- coding:utf-8 -*-
import csv
csvfile = open('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['id', 'url', 'keywords'])
data = [
    ('1', 'http://www.xiaoheiseo.com/', '小黑'),
    ('2', 'http://www.baidu.com/', '百度'),
    ('3', 'http://www.jd.com/', '京东')
]
writer.writerows(data)
csvfile.close()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

result = requests.get('https://movie.douban.com/subject/3541415/')
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text, 'html.parser')

try:
    info = soup.select('#info')[0]
    print re.findall(ur'(?<=制片国家/地区: ).+?(?=\n)', info.text)[0]
except Exception, e:
    print e

soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

s = "哈哈"
ss = u'哈哈'

print repr(s)
print repr(ss)

print s.decode('utf-8').encode('gbk')
print ss.encode('gbk')

print s.decode('utf-8')
print ss