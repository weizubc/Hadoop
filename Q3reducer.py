#!/usr/bin/python

import sys
import operator

count = 0
oldKey = None
top10 = {}
lowest_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, id = data_mapped

    if oldKey and oldKey != thisKey:
        if len(top10) < 10:
            top10[oldKey] = count
            lowest_count = min(top10.values())
        elif  count > lowest_count :
             top10[oldKey] = count
             sorted_top10 = sorted(top10.items(),key=operator.itemgetter(1),reverse=True)
             sorted_top10.pop()
             top10 = dict(sorted_top10)
             lowest_count = sorted_top10[-1][1]
        count = 0
    
    oldKey = thisKey
    count  += 1

if oldKey != None:
    if len(top10) < 10:
        top10[oldKey] = count
        sorted_top10 = sorted(top10.items(),key=operator.itemgetter(1),reverse=True)
    elif count > lowest_count :
        top10[oldKey] = count
        sorted_top10 = sorted(top10.items(),key=operator.itemgetter(1),reverse=True)
        sorted_top10.pop()
        top10 = dict(sorted_top10)

for key, value in sorted_top10:
    print "{0}\t{1}".format(key,value)
