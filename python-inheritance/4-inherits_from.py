#!/usr/bin/python3
"""Defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherits (directly or indirectly)
    from a_class, but is not a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
