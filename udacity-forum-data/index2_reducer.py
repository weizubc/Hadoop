#!/usr/bin/python

import sys

oldKey = None
idlist = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, id = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", idlist
        idlist = []

    oldKey = thisKey
    idlist.append(int(id))

if oldKey != None:
    print oldKey, "\t", idlist

