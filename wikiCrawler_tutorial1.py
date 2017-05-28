#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup as bs

URL = "https://en.wikipedia.org/wiki/The_Matrix"
response = urllib.request.urlopen(URL)
html_cont = response.read()
soup = bs(html_cont,'html.parser',from_encoding='utf-8')
print(soup.title)
#print(soup.prettify())
print(soup.get_text())
urls = soup.find_all('a')
for url in urls[:5]:
    print(url)