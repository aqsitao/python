"""
get some u-know-it kind of image from website
"""
import re
import urllib.request
import time


def craw(url, page):
    headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Host': 'www.mtupian.com',
               'Referer': 'http://www.188pp.com/ktdm/'+str(34061-i),
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/60.0.3112.90 Safari/537.36'}
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div class=content>.+?<div class=pagea>'
    result1 = re.compile(pat1).findall(html1)
    pat2 = 'src="(http://www\.\w+\.[\w|/]*\.jpg)"'
    result1 = result1[0]
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = str(page)+str(x)+'.jpg'
        try:
            req = urllib.request.Request(imageurl, None, headers)
            data = urllib.request.urlopen(req).read()
            time.sleep(1)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1
        x += 1
        with open(imagename, 'wb') as f:
            f.write(data)
        f.close


for i in range(1, 10):
    url1 = "http://www.188pp.com/ktdm/" + str(34061-i)
    craw(url1, i)
