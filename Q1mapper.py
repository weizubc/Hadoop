#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    author_id =line[3]
    time = line[8]
    puretime = time.split('.')[0]
    hour = datetime.strptime(puretime,"%Y-%m-%d %H:%M:%S").hour
    print "{0}\t{1}".format(author_id, hour)


