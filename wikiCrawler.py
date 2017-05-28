#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.parse  # 正則表達式，處理字串
import urllib.request # 取得網頁的回應
import re # 解析網址
from bs4 import BeautifulSoup as bs # 解析網頁內容架構

def get_new_urls(page_url,soup): #取得網頁內的超連結
    find_new_urls=[]
    links = soup.find_all('a', href=re.compile(r"^/wiki/\w+"))
    for link in links[:3]:
        if not re.search("\w+:\w+",link['href']):
            new_full_url = urllib.parse.urljoin(page_url,link['href'])
            find_new_urls.append(new_full_url)
    return find_new_urls

URL = "https://en.wikipedia.org/wiki/The_Matrix"
new_urls = [URL]
old_urls = []
count = 0
while len(new_urls) >0 and count <30: # 設定爬取網頁上限
    count +=1
    new_url = new_urls.pop()
    old_urls.append(new_url)
    print("%d: %s", count, new_url)
    response = urllib.request.urlopen(new_url)
    html_cont = response.read()
    soup = bs(html_cont,'html.parser', from_encoding='utf-8')
    find_urls = get_new_urls(new_url, soup)
    for url in find_urls:
        if url not in new_urls and url not in old_urls:
            new_urls.append(url)     