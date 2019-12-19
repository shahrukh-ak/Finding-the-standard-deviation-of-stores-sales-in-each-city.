#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    print("%s\t%s"%(line[2], line[4]))

