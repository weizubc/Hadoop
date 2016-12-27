#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    if line[5] == "question":
        id = line[0]
        tags = line[2].split()
        for tag in tags:
            print "{0}\t{1}".format(tag,id)


