#!/usr/bin/python3
"""Displays X-Request-Id header using requests"""
import requests
import sys

response = requests.get(sys.argv[1])
print(response.headers.get('X-Request-Id'))
