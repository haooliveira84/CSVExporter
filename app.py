#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import sys
import operator

from collections import Counter


cont = Counter()
result = {}
fileopen = open(sys.argv[1], 'rt')


def verify_token(token):
    if token == os.getenv("MP_PASS"):
        process_file(fileopen)
    else:
        print "ERR"
        quit()

def process_file(fileopen):
    reader = csv.reader(fileopen)
    next(reader, None)
    sort = sorted(reader, key=operator.itemgetter(0)) 
    for Estado, Cidade, Nome in sort:
        if Estado in result:
            result[Estado].append(Nome)
        else:
            result[Estado] = [Nome]
    for row in sort:
        Estado, Cidade, Nome = row[0], row[1], row[2]
        cont[Estado] += 1
    for firesult in sorted(cont.items()):
        print firesult

verify_token(sys.argv[2])