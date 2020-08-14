"""
rendered_symbol.py
"""
from connection_types import StemEnd
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem import Stem


class RenderedSymbol:

    def __init__(self, stem: 'Stem', end: StemEnd, symbol: str):
        self.Stem = stem
        self.End = end
        self.Symbol = symbol
        # self.Growth = growth TODO: compute this
        self.render()

    def render(self):
        print(f'Rendering symbol: {self}')

    def __repr__(self):
        return f'Stem: {self.Stem}, End: {self.End}, Symbol: {self.Symbol}'
