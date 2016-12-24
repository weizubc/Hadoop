#!/usr/bin/python
import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
count=0
a=[]
for line in reader:
    b=line[4].lower()
    if  "fantastic" in b:
        count+=b.count('fantastic')
        count-=b.count('fantastically')
    if "fantastically" in b:
        a.append(int(line[0]))

a.sort()
print count,a


