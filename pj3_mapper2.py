#!/usr/bin/env python

import sys

for line in sys.stdin:
    data = line.split("\"")
    if len(data) < 2:
        # Something has gone wrong. Skip this line.
        continue
    data2= data[1].strip()
    data22= data2.split()
    if len(data22) < 2:
        continue
    web= data22[1]
    word="http://www.the-associates.co.uk"
    if web[:len(word)]==word:
        web=web[len(word):]
    data3= data[0].strip()
    ip= data3.split()[0]
    print "{0}\t{1}".format(web,ip)
