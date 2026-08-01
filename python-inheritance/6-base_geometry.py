#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Represent a base geometry object."""

    def area(self):
        """Raise an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
