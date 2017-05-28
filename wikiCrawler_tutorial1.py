#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request # 取得網頁的回應
from bs4 import BeautifulSoup as bs # 解析網頁內容架構

URL = "https://en.wikipedia.org/wiki/The_Matrix"
new_urls = [URL]
count = 0
while len(new_urls) >0 and count <30: # 設定爬取網頁上限
    count +=1
    new_url = new_urls.pop()
    print("%d: %s", count, new_url)
    response = urllib.request.urlopen(new_url)
    html_cont = response.read()
    soup = bs(html_cont,'html.parser', from_encoding='utf-8')