#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import operator
import json

import requests
from flask import Flask, make_response, request, Response, jsonify
from flask_httpauth import HTTPTokenAuth


from collections import Counter

