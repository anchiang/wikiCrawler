#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import re
import urllib.parse
import urllib.request

def get_new_urls(page_url,soup):
    find_new_urls=[]
    links = soup.find_all('a', href=re.compile(r"^/wiki/\w+"))
    for link in links[:3]:
        if not re.search("\w+:\w+",link['href']):
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            find_new_urls.append(new_full_url)
    return find_new_urls

def add_url(new_urls, url):
    if url is None:
        return None
    if url not in new_urls and url not in old_urls:
        new_urls.append(url)
        
if __name__=="__main__":
    URL = "https://en.wikipedia.org/wiki/The_Matrix"
    new_urls = []
    old_urls = []
    new_urls.append(URL)
    response = urllib.request.urlopen(URL)
    soup = bs(response,'html.parser',from_encoding='UTF-8')
    count = 0;
    while len(new_urls) >0 and count <20:
        count +=1
        new_url = new_urls.pop()
        old_urls.append(new_url)
        print("%d: %s", count, new_url)
        response = urllib.request.urlopen(new_url)
        html_cont = response.read()
        soup = bs(html_cont,'html.parser',from_encoding='utf-8')
        find_urls = get_new_urls(new_url, soup)
        for url in find_urls:
            add_url(new_urls,url)     