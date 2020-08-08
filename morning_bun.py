"""
morning_bun.py – Just here to play around and test something, not part of Flatland!
"""

from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2



class MorningBun:
    temp = ''
    flavor = ''

    def __init__(self):
        print("Cooking a morning bun!")
        MorningBun.temp = 'warm'
        MorningBun.flavor = 'orange'
