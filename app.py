#!/usr/bin/python
import csv
import sys

fileopen = open(sys.argv[1], 'rt')

try:
    reader = csv.DictReader(fileopen)
    for rows in reader:
        rows = str(rows["Estado"])
        print rows
finally:
    fileopen.close()