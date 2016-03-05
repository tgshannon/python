'''
Read json data
'''

import urllib
import json

while True:
    Y = []

    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()

    info = json.loads(data)
    for item in info['comments']:
        Y.append(item['count'])
    
    Y = map(int, Y)
    print sum(Y)

    
