'''
Access web data using python
Assignment 3 follow url links
'''
import re
import urllib
from BeautifulSoup import *

site = raw_input('Site - ')
count = int(raw_input('count: '))
position = int(raw_input('position: ')) - 1

for i in range(0, count):
    #print "Retrieving: ", site
    html = urllib.urlopen(site).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    site = tags[position]['href']
 
print tags[position].contents[0]    
