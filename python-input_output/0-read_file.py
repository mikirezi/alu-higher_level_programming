#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
