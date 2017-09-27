#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import sys
import operator

from collections import Counter
from collections import defaultdict
from flask import Flask
from flask_httpauth import HTTPTokenAuth


app = Flask(__name__)
auth = HTTPTokenAuth("Token")
contador = Counter()
result = {}
fileopen = open(sys.argv[1], 'rt')

def verify_token(token):
    return token == os.getenv("MP_PASS")

try:
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
        contador[Estado] += 1
    for firesult in sorted(contador.items()):
        print firesult
finally:
    fileopen.close()