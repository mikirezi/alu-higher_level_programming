#!/usr/bin/python3
"""Script that displays the value of X-Request-Id header."""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
