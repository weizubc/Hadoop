#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)


for line in reader:
    if len(line)== 5:
        if line[1] == "reputation":
            continue
        else:
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(line[0],"A",line[1],line[2],line[3],line[4])
    else:
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(line[3],"B",line[0],line[1],line[2],line[5],line[6],line[7],line[8],line[9])
