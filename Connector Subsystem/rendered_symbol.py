"""
rendered_symbol.py
"""
from geometry_types import Position
from connection_types import NodeFace
from symbol import Symbol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tablet import Tablet


class RenderedSymbol:
    """
    Take a position for placement x,y
    Look up symbol point data, choosing appropriate rotation if not a circle
    Translate coordinates by adding to x,y position
    Draw open polygon and supply to tablet with asset name
    """

    def __init__(self, tablet: 'Tablet', face: NodeFace, location: Position, symbol_name: str):
        self.Location = location
        self.Symbol_spec = Symbol.instances[symbol_name]

        if self.Symbol_spec.type == 'arrow':
            # Get the numpy polygon matrix with the rotation pointing toward the Node face
            rotated_arrow = self.Symbol_spec.spec.shape.rotations[face]
            # Add the coordinates to our location
            vertices = [Position(location.x+x, location.y+y) for x, y in rotated_arrow]
            tablet.add_polygon(asset=symbol_name, vertices=vertices)
