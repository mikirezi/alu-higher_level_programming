#!/usr/bin/python3
"""Displays the value of X-Request-Id header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
