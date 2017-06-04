#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs #取得網頁內容架構
import re #regular Expression

def get_new_urls(nurl): #抓取新的網頁連結
    response = urllib.request.urlopen(nurl)
    html_cont = response.read()
    soup = bs(html_cont,'html.parser',from_encoding='utf-8')
    urls = soup.find_all('a',href=re.compile("^/wiki/\w+"))
    # 尋找新的網址
    for url in urls[:10]:
        if not re.search("\w:\w", url['href']):
            furl = urllib.parse.urljoin(nurl,url['href'])
            if furl not in new_urls and furl not in old_urls:
                new_urls.append(furl)

URL = "https://en.wikipedia.org/wiki/The_Matrix"
new_urls = [URL]
old_urls = []
count = 0
fout = open('output.csv','w',encoding='utf-8')
while len(new_urls)>0 and count < 10:
    count +=1
    new_url = new_urls.pop()
    old_urls.append(new_url)
    short_url = re.search(r"/wiki/(\w+)",new_url).group(1)
    print("%d, %s" %(count,short_url))
    fout.write("%d, %s \n" %(count,new_url))
    get_new_urls(new_url)    
fout.close()