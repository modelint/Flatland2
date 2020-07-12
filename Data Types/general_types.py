"""
general_types.py - Model level types that are used across multiple domains
"""

from typing import NewType

Index = NewType('Index', int)  # A numeric array index (a positive integer)


def ok_index(i: int) -> bool:
    return i >= 0
