"""
tertiary_stem.py
"""

from symbol import Symbol
from anchored_stem import AnchoredStem
from stem_type import StemType
from connection_types import HorizontalFace, NodeFace, AnchorPosition
from geometry_types import Position
from typing import TYPE_CHECKING, Set

if TYPE_CHECKING:
    from node import Node
    from binary_connector import BinaryConnector


class TertiaryStem(AnchoredStem):
    """
    An Anchored Stem that reaches from a Node face at its root end and attaches its vine end to a Binary Connector.
    """

    def __init__(self, connector: 'BinaryConnector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, anchor_position: AnchorPosition, parallel_segs: Set[tuple]):
        """
        Constructor

        :param connector:
        :param stem_type:
        :param semantic:
        :param node:
        :param face:
        :param anchor_position:
        :param parallel_segs:
        """
        AnchoredStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)

        # Get length of root and vine symbols
        # If no symbol, the stem will be zero length at the corrsponding root/vine end
        root_symbol = stem_type.DecoratedStems[semantic].Root_symbol
        vine_symbol = stem_type.DecoratedStems[semantic].Vine_symbol
        rlen = 0 if not root_symbol else Symbol.instances[root_symbol].length
        vlen = 0 if not vine_symbol else Symbol.instances[vine_symbol].length
        # TODO: implement root start also (even though there is no root symbol on tertiary yet)
        self.Root_start = None
        self.Vine_start = None

        if face in HorizontalFace:
            if face == NodeFace.TOP:
                isegs = {s for s in parallel_segs if s[0].y > self.Root_end.y}
                yval = min({s[0].y for s in isegs})
                scale = -1  # back of symbol is toward top face
            elif face == NodeFace.BOTTOM:
                isegs = {s for s in parallel_segs if s[0].y < self.Root_end.y}
                yval = max({s[0].y for s in isegs})
                scale = 1  # back of symbol is way from bottom face
            self.Vine_start = Position(self.Root_end.x, yval+vlen*scale)
            self.Vine_end = Position(self.Root_end.x, yval)
        else:
            if face == NodeFace.RIGHT:
                isegs = {s for s in parallel_segs if s[0].x > self.Root_end.x}
                xval = min({s[0].x for s in isegs})
                scale = -1  # vine is to the left of the right face
            elif face == NodeFace.LEFT:
                isegs = {s for s in parallel_segs if s[0].x < self.Root_end.x}
                xval = max({s[0].x for s in isegs})
                scale = 1  # vine is to the right of the left face
            self.Vine_start = Position(xval+vlen*scale, self.Root_end.y)
            self.Vine_end = Position(xval, self.Root_end.y)

    def render(self):
        """
        Create line from root end to the vine end attached to the Binary Connector line
        """
        tablet = self.Connector.Diagram.Canvas.Tablet
        print("Drawing tertiary connector")
        # TODO: from here  should be root end - any root symbol length
        # TODO: to there should be vine end - any vine symbol length
        # TODO: - means away along axis from root or vine
        tablet.add_line_segment(asset='assoc stem', from_here=self.Root_end, to_there=self.Vine_start)
        super().render()