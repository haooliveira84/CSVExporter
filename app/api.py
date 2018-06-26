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



app = Flask(__name__)
auth = HTTPTokenAuth("Token")

@auth.verify_token
def verify_token(token):
    return token == os.getenv("MP_PASS")

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/api', methods=['GET', 'POST'])
@auth.login_required
def main_route():
    if request.json:
        json_data = request.get_json()
        firesult = main_process(json_data)
        return firesult
    else:
        return "No json received"

def main_process(json_data):
    values = []
    data = sorted(json_data, key=lambda k: k['estado'])
    for value in data:
        values.append((value['estado'], value['nome']))
    for estado, nome in values:
        cont[estado] += 1
        customers = sorted(cont.items())
    return jsonify(customers)

if __name__ == "__main__":
	app.run("0.0.0.0",use_reloader=True,port=9900)