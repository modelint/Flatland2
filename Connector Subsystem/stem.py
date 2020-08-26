"""
stem.py
"""

from sqlalchemy import select, and_
from symbol import Symbol
from stem_type import StemType
from geometry_types import Position
from rendered_symbol import RenderedSymbol
from connection_types import NodeFace
from flatlanddb import FlatlandDB as fdb

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector import Connector
    from node import Node


class Stem:
    """
    This is a line drawn from a face on a Node outward. The terminator on the node face is the root and the
    terminator on the other side of the line is the vine. A Stem may be decorated on either, both or neither end.
    A decoration consists of a graphic symbol such as an arrowhead or a circle or a fixed text label such as the
    UML '0..1' multiplicity label. A graphic symbol may be combined with a text symbol such as the Shlaer-Mellor
    arrow head 'c' conditionality combination.

    Attributes
    ---
    Connector : Stem is on one end of this Connector
    Stem_type : Specifies charactersitics and decoration, if any, of this Stem
    Node : Stem is attached to this Node
    Node_face : On this face of the Node
    Root_end : Where the Stem attaches to the Node face
    Vine_end : End of Stem away from Node face with clearance for any decoration
    """

    def __init__(self,
                 connector: 'Connector', stem_type: StemType, semantic: str, node: 'Node',
                 face: NodeFace, root_position: Position):
        self.Connector = connector
        self.Stem_type = stem_type
        self.Node = node
        self.Node_face = face
        self.Semantic = semantic
        self.Root_end = root_position

        # Check to see if Vine needs to be computed (fixed) geometry
        if self.Stem_type.Geometry == 'fixed':
            root_symbol = stem_type.DecoratedStems[semantic].Root_symbol
            vine_symbol = stem_type.DecoratedStems[semantic].Vine_symbol
            rlen = 0 if not root_symbol else Symbol.instances[root_symbol].length
            vlen = 0 if not vine_symbol else Symbol.instances[vine_symbol].length
            stem_len = rlen + vlen

            x, y = self.Root_end
            if face == NodeFace.RIGHT:
                x = x + stem_len
            elif face == NodeFace.LEFT:
                x = x - stem_len
            elif face == NodeFace.TOP:
                y = y + stem_len
            elif face == NodeFace.BOTTOM:
                y = y - stem_len
            self.Vine_end = Position(x, y)
        # Otherwise, Vine_end should have been overridden

    def render(self):
        """
        Draw a symbol at the root, vine, both or neither end of this Stem
        """
        root_symbol_name = self.Stem_type.DecoratedStems[self.Semantic].Root_symbol
        vine_symbol_name = self.Stem_type.DecoratedStems[self.Semantic].Vine_symbol
        if root_symbol_name:
            RenderedSymbol(stem=self, end='root', symbol=Symbol.instances[root_symbol_name])

