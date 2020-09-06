"""
stem.py
"""

from stem_type import StemType
from geometry_types import Position
from rendered_symbol import RenderedSymbol
from connection_types import NodeFace

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

        - Connector -- Stem is on one end of this Connector
        - Stem_type -- Specifies charactersitics and decoration, if any, of this Stem
        - Node -- Stem is attached to this Node
        - Node_face -- On this face of the Node
        - Root_end -- Where the Stem attaches to the Node face
        - Vine_end -- End of Stem away from Node face with clearance for any decoration

        Relationships

        - Root_rendered_symbol -- R61/Rendered Symbol
        - Vine_rendered_symbol -- R61/Rendered Symbol
    """

    def __init__(self, connector: 'Connector', stem_type: StemType, semantic: str, node: 'Node',
                 face: NodeFace, root_position: Position):
        self.Connector = connector
        self.Stem_type = stem_type
        self.Node = node
        self.Node_face = face
        self.Semantic = semantic
        self.Root_end = root_position
        # There are at most two rendered symbols (one on each end) of a Stem and usually none or one
        self.Root_rendered_symbol = None  # Default assumption until lookup a bit later
        self.Vine_rendered_symbol = None

        # Some stem subclasses will compute their vine end, but for a fixed geometry, we can do it right here
        if self.Stem_type.Geometry == 'fixed':
            # For a fixed geometry, the Vine end is a fixed distance from the Root End
            stem_len = self.Stem_type.Minimum_length
            # Compute the coordinates based on the stem direction using the rooted node face
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
        # TODO: consider Free geometry

    def render(self):
        """
        Draw a symbol at the root, vine, both or neither end of this Stem
        """
        root_symbol_name = self.Stem_type.DecoratedStems[self.Semantic].Root_symbol
        vine_symbol_name = self.Stem_type.DecoratedStems[self.Semantic].Vine_symbol

        if root_symbol_name:
            self.Root_rendered_symbol = RenderedSymbol(
                stem=self,
                end='root', location=self.Root_end,
                symbol_name=root_symbol_name
            )
        if vine_symbol_name:
            self.Vine_rendered_symbol = RenderedSymbol(
                stem=self,
                end='vine', location=self.Vine_end,
                symbol_name=vine_symbol_name
            )
