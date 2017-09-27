#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import json
import operator

from collections import Counter
from flask import Flask
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth("Token")
cont = Counter()
result = {}
fileopen = open('arq.csv', 'rt')


@auth.verify_token
def verify_token(token):
    return token == os.getenv("MP_PASS")

@app.route("/")
@auth.login_required
def main_route():
    filename = csv.reader(fileopen)
    read_csv(filename)

def read_csv(reader):
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
       json_print(firesult)

def json_print(csv_result):
    json_encoded = json.dumps(csv_result)
    return json_encoded
        
if __name__ == '__main__':
    app.run("0.0.0.0", port=8090)