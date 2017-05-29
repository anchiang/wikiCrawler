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
            if furl not in new_urls and url not in old_urls:
                new_urls.append(furl)

URL = "https://en.wikipedia.org/wiki/The_Matrix"
new_urls=[URL]
old_urls=[]
count = 0
fout = open('output.csv', 'w', encoding='utf-8')
while len(new_urls)>0 and count <5:
    count += 1
    new_url = new_urls.pop()
    old_urls.append(new_url)
    short_url = re.search(r"/wiki/(\w+)",new_url).group(1)
    print("%d: %s " % (count,short_url))
    fout.write("%d, %s \n" % (count,short_url))
    get_new_urls(new_url)
fout.close()
print("Data is written on output.csv")    