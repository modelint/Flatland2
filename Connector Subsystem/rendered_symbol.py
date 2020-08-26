"""
rendered_symbol.py
"""
from open_polygon import OpenPolygon
from connection_types import NodeFace
from symbol import Symbol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem import Stem


class RenderedSymbol:
    """
    Take a position for placement x,y
    Look up symbol point data, choosing appropriate rotation if not a circle
    Translate coordinates by adding to x,y position
    Draw open polygon and supply to tablet with asset name
    """

    def __init__(self, face: NodeFace, end: str, symbol: Symbol):
        self.End = end
        self.Symbol = symbol
        # self.Growth = growth TODO: compute this




        self.render()

    def create_points(self, face: NodeFace):
        """

        """
        if face == NodeFace.RIGHT:
            pass

    def render(self):
        print(f'Rendering symbol: {self}')

    def __repr__(self):
        return f'Stem: {self.Stem}, End: {self.End}, Symbol: {self.Symbol}'
