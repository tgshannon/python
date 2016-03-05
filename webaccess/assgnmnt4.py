import urllib
import xml.etree.ElementTree as ET

while True:
    Y = []

    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)

    results = tree.findall('.//count')
    for result in results:
        Y.append(result.text)

    Y = map(int, Y)
    print sum(Y)

    
