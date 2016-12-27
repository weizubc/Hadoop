#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    id = line[0]
    author_id = line[3]
    qid = line[6]
    if qid == '\N':
        qid = id
    print "{0}\t{1}".format(qid,author_id)
