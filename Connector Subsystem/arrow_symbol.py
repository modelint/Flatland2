"""
arrow_head_symbol.py
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem import Stem


class ArrowHeadSymbol:
    def __init__(self, stem: 'Stem', name: str ):
        self.Name = name
        self.Stem = stem