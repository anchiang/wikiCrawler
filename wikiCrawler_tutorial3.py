#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import re

def get_new_urls(nurl):
    response = urllib.request.urlopen(nurl)
    html_cont = response.read()
    soup = bs(html_cont,'html.parser',from_encoding='utf-8')
    urls = soup.find_all('a',href=re.compile("^/wiki/\w+"))
    for url in urls[:10]:
        if not re.search("\w:\w", url['href']):
            furl = urllib.parse.urljoin(nurl,url['href'])
            new_urls.append(furl)

URL = "https://en.wikipedia.org/wiki/The_Matrix"
new_urls=[URL]
count = 0
while len(new_urls)>0 and count <10:
    count += 1
    new_url = new_urls.pop()
    print(count, new_url)
    get_new_urls(new_url)