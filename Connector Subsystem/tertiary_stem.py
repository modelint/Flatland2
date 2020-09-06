"""
tertiary_stem.py
"""

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
    An Anchored Stem that reaches from a Node face at its root end and attaches its vine end to the
    line segment drawn for a Binary Connector.
    """

    def __init__(self, connector: 'BinaryConnector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, anchor_position: AnchorPosition, parallel_segs: Set[tuple]):
        """
        Constructor

        :param connector:  Part of this Binary Connector
        :param stem_type: Specifies universal characteristics of this Stem
        :param semantic: Meaning of this Stem
        :param node: Is rooted on this Node
        :param face: Is rooted from this Node face
        :param anchor_position: Position of the Root as specified by the user
        :param parallel_segs: All binary connector line segments parallel to the rooted Node face
        """
        AnchoredStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position)

        self.Root_start = None
        self.Vine_start = None

        # Compute the vine end so that it touches the closest Binary Connector bend line segment
        # away from the root node face
        if face in HorizontalFace:
            if face == NodeFace.TOP:
                # Find all parallel line segments above node face
                isegs = {s for s in parallel_segs if s[0].y > self.Root_end.y}
                # Get y value of line segment closest to the node face
                yval = min({s[0].y for s in isegs})
            elif face == NodeFace.BOTTOM:
                isegs = {s for s in parallel_segs if s[0].y < self.Root_end.y}
                yval = max({s[0].y for s in isegs})
            self.Vine_end = Position(self.Root_end.x, yval)
        else:
            if face == NodeFace.RIGHT:
                isegs = {s for s in parallel_segs if s[0].x > self.Root_end.x}
                xval = min({s[0].x for s in isegs})
            elif face == NodeFace.LEFT:
                isegs = {s for s in parallel_segs if s[0].x < self.Root_end.x}
                xval = max({s[0].x for s in isegs})
            self.Vine_end = Position(xval, self.Root_end.y)

    def render(self):
        """
        Create line from root end to the vine end attached to the Binary Connector line
        """
        tablet = self.Connector.Diagram.Canvas.Tablet
        tablet.add_line_segment(asset=self.Stem_type.Name+' stem', from_here=self.Root_end, to_there=self.Vine_end)
        super().render()