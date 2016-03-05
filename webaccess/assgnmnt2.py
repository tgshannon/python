'''
Access web data using python
Assignment 2 Scrapping html using BeautifulSoup
'''
import urllib
from BeautifulSoup import *

site = raw_input('Site - ')
html = urllib.urlopen(site).read()
soup = BeautifulSoup(html)

count = 0
Y = []
tags = soup('span')
for tag in tags:
    count += 1
    y = tag.contents
    if len(y):
        Y.extend(y)

Y = map(int, Y)
print count
print sum(Y)
    
