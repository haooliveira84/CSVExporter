#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import operator
import json

import requests
from flask import Flask, make_response, request, Response, jsonify
from flask_httpauth import HTTPTokenAuth


from collections import Counter

cont = Counter()
result = {}


app = Flask(__name__)
auth = HTTPTokenAuth("Token")

@auth.verify_token
def verify_token(token):
    return token == os.getenv("MP_PASS")

@app.route('/api', methods=['GET', 'POST'])
@auth.login_required
def main_route(query=None):
    json_dict = request.get_json()
    if request.headers.get('query'):
		query = request.headers.get('query')
    else:
		query = json_dict['query'] 
    print query

def main_process(query):
    req = query.json()
    Estado = (req['estado'])
    Cidade = (req['cidade'])
    Nome = (req['nome'])
    for Estado, Cidade, Nome in sort:
        if Estado in result:
            result[Estado].append(Nome)
        else:
            result[Estado] = [Nome]
    for row in sort:
        Estado, Cidade, Nome = row[0], row[1], row[2]
        cont[Estado] += 1
        firesult = sorted(cont.items())
    print firesult
    
if __name__ == "__main__":
	app.run("0.0.0.0",use_reloader=True)