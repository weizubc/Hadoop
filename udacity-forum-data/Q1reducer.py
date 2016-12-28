#!/usr/bin/python

import sys

count = 0
maxcount = 0
oldKey = None
oldHour = None
maxHour = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
        if count > maxcount:
            maxHour = []
            maxHour.append(oldHour)
        if count == maxcount:
            maxHour.append(oldHour)

        for hour in maxHour:
            print oldKey, "\t", hour
        maxHour = []
        count = 0
        maxcount = 0
        oldHour = None

    if oldHour and oldHour != thisHour:
        if count == maxcount:
            maxHour.append(oldHour)
        if count > maxcount:
            maxcount = count
            maxHour = []
            maxHour.append(oldHour)
        count = 0

    oldKey = thisKey
    oldHour = thisHour
    count += 1

if oldKey != None:
    for hour in maxHour:
        print oldKey, "\t", hour

