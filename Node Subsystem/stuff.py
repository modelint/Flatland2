"""
stuff.py - Something to be imported (to test how import works in Python3)
"""


class Stuff:

    def __init__(self):
        print("initializing Stuff")
        Stuff.Location = "Over there"

Stuff()