"""
rendered_symbol.py
"""
from open_polygon import OpenPolygon
from geometry_types import Position
from connection_types import NodeFace
from symbol import SymbolSpec
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

    def __init__(self, face: NodeFace, location: Position, symbol_spec: SymbolSpec):
        self.Location = location
        self.Symbol_spec = symbol_spec

        if symbol_spec.type == 'arrow':
            # Get the numpy polygon matrix with the rotation pointing toward the Node face
            rotated_arrow = symbol_spec.spec.shape.rotations[face]
            # Add the coordinates to our location
            OpenPolygon()





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
