#!/usr/bin/python

#Creates an inverted index of all words that can be find in the body of a forum post and node id they can be found in.

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
    id = line[0]
    body = line[4].lower()
    wordlist = re.findall(r"[\w]+", body)
    for char in set(wordlist):
        print "{0}\t{1}".format(char,id)
