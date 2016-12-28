#!/usr/bin/python

#Examine if there is a correlation between the length of a post and the length of answers.

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    id = line[0]
    bodylen = len(line[4])
    type = line[5]
    qid = line[6]
    if qid == '\N':
        qid = id
    print "{0}\t{1}\t{2}".format(qid,type,bodylen)


