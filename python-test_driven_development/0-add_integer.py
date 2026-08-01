#!/usr/bin/python3
"""Module that adds two integers.

This module defines a single function, add_integer, which adds
two numbers together after validating and casting their types.
"""


def add_integer(a, b=98):
    """Add two integers.

    Casts floats to integers before adding them.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
