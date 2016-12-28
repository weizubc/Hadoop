#!/usr/bin/python

import sys
import operator

count = 0
oldKey = None
top10 = []
lowest_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, id = data_mapped

    if oldKey and oldKey != thisKey:
        if len(top10) < 10:
            top10.append((oldKey,count))
            lowest_count = min(top10,key=lambda x:x[1])[1]
        elif count > lowest_count :
            top10.append((oldKey,count))
            top10.sort(key=lambda x:x[1],reverse=True)
            top10.pop()
            lowest_count = top10[-1][1]
        count = 0
    
    oldKey = thisKey
    count  += 1

if oldKey != None:
    if len(top10) < 10:
        top10.append((oldKey,count))
    elif count > lowest_count :
        top10.append((oldKey,count))
        top10.sort(key=lambda x:x[1],reverse=True)
        top10.pop()

for key, value in top10:
    print "{0}\t{1}".format(key,value)
