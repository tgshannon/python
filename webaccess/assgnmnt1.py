'''Access web data using python assignment 1'''

import re

f = raw_input('enter file: ')
hand = open(f, 'r')
Y =[]

for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y):
        Y.extend(y)

Y = map(int, Y)
print sum(Y)
