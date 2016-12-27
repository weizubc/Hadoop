#!/usr/bin/python

import sys

totlength = 0
count = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, type, length = data_mapped

    if oldKey and oldKey != thisKey:
        if count >0:
            alength = totlength/count
        else:
            alength = 0
        print oldKey, "\t", qlength, "\t", alength
        totlength = 0
        count = 0
    
    oldKey = thisKey
    if type == "question":
        qlength = length
    else:
        totlength += float(length)
        count  += 1

if oldKey != None:
    if count >0:
        alength = totlength/count
    else:
        alength = 0
    print oldKey, "\t", qlength, "\t", alength

