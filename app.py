#!/usr/bin/python
import csv
import sys

fileopen = open(sys.argv[1], 'rt')

try:
    reader = csv.reader(fileopen)
    for row in reader:
        print row
finally:
    fileopen.close()