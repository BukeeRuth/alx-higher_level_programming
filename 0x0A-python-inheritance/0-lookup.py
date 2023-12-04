#!/usr/bin/python3

"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns the list of an object's available methods and attributes."""
    return (dir(obj))
