#!/usr/bin/python3
"""Sends a POST request with an email parameter"""
import urllib.request
import urllib.parse
import sys

data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
with urllib.request.urlopen(sys.argv[1], data) as response:
    print(response.read().decode('utf-8'))
