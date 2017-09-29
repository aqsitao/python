"""
Download text from qiushibaike.com
"""

import urllib.request
import re


def getcontent(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/60.0.3112.90 '
                      'Safari/537.36'}
    req = urllib.request.Request(url, None, headers)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    userpat = '<h2>(.*?)</h2>'
    contentpat = '<div class="content">\n<span>(.*?)</span>'
    userlist = re.compile(userpat, re.S).findall(data)
    contentlist = re.compile(contentpat, re.S).findall(data)
    Idx = 1
    contentdata = []
    for content in contentlist:
        content = content.replace('\n', '')
        contentdata.append(content)
        Idx += 1
    Idy = 1
    with open('qiubai.txt', 'w') as f:
        for j, user in enumerate(userlist):
            user = user.replace('\n', '')
            text = '用户' + str(page) + str(Idy) + '是' + user + '\n' + '内容是:' + '\n' + contentdata[j] + '\n'
            f.write(text)
            Idy += 1
    f.close()


for i in range(1, 2):
    url = 'https://www.qiushibaike.com/8hr/page/' + str(i)
    getcontent(url, i)
