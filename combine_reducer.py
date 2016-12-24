#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys


outputa={}
outputb={}
for line in sys.stdin:
    data = line.strip().split("\t")
    if data[1]=='"A"':
        outputa[data[0]]=data[2:]
    if data[1]=='"B"':
        outputb[data[0]]=data[2:]

#print outputa,outputb

for item in outputb:
    if item in outputa:
        for i in outputa[item]:
            outputb[item].append(i)
        print " ".join(outputb[item])