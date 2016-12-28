#!/usr/bin/env python

#Find the number of hits to the site made by each IP.

import sys

for line in sys.stdin:
    data = line.split("\"")#split by "
    if len(data) < 2:
        # Something has gone wrong. Skip this line.
        continue
    data2 = data[1].strip()
    data22 = data2.split()
    if len(data22) < 2:
        continue
    web = data22[1]
    data3 = data[0].strip()
    ip = data3.split()[0]
    print "{0}\t{1}".format(ip,web)
