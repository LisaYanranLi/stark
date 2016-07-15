# -*- coding:utf-8 -*-
# import urllib
import urllib2
import re

url = 'http://www.job.sjtu.edu.cn/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&zpxxType=new'
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
#     print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

content = response.read().decode('utf-8')
# print content
pattern = re.compile('<div.*?350.*?><a.*?>(.*?)</a>.*?500.*?><a.*?>(.*?)</a>.*?<div style="float:right;">(.*?)</div>',re.S)
items = pattern.findall(content)
# print items
for item in items:
    print item[0],'    ',item[1],'    ',item[2]
# pattern1 = '<div.*?350.*?><a.*?>(.*?)</a></div>'
# pattern2 = '<div.*?500.*?><a.*?>(.*?)</a></div>'
# pattern3 = '<div style="float:right;">(.*?)</div>'
# items1 = re.findall(pattern1,content)
# items2 = re.findall(pattern2,content)
# items3 = re.findall(pattern3,content)
# for item in items1:
#     print item
# for item in items2:
#     print item
# for item in items3:
#     print item
#     [0],item[1],item[2]