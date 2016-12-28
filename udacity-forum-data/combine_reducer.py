#!/usr/bin/python

import sys

count = 0
oldKey = None
tempAsave = None
tempBsave = []


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0]
    type = data_mapped[1]
    rest = "\t".join(data_mapped[2:])

    if oldKey and oldKey != thisKey:
        if count > 1:
            for row in tempBsave:
                print row, "\t", oldKey,"\t",tempAsave
        count = 0
        tempAsave = None
        tempBsave = []

    oldKey = thisKey
    if type == "A":
        tempAsave = rest
    else:
        tempBsave.append(rest)
    count += 1


if oldKey != None:
    if count > 1:
        for row in tempBsave:
            print row, "\t", oldKey,"\t",tempAsave


