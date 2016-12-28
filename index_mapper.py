#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    id = line[0]
    body = line[4].lower()
    wordlist = re.findall(r"[\w]+", body)
    for char in wordlist:
        print "{0}\t{1}".format(char,id)
