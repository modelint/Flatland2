""" anchored_stem.py """

from stem import Stem
from stem_type import StemType
from connection_types import NodeFace, AnchorPosition
from layout_specification import default_stem_positions
from geometry_types import Position
from linear_geometry import step_edge_distance
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from node import Node
    from connector import Connector


def anchor_to_position(node: 'Node', face: NodeFace, anchor_position: AnchorPosition) -> Position:
    """
    Compute the x or y coordinate of the user supplied anchor position.
    Using a static function since we can't initiale the superclass instance until we compute
    the anchor position
    :param node:  Anchor is attached to this Node
    :param face:  Anchor is attached to this face
    :param anchor_position:  Relative user specified distance on face relative to center position
    :return:  x, y canvas coordinate of the anchor position
    """
    # Return either an x or y value where the root end is placed
    if face == NodeFace.LEFT or face == NodeFace.RIGHT:
        face_extent = node.Size.height
    else:
        face_extent = node.Size.width

    edge_offset = step_edge_distance(num_of_steps=default_stem_positions, extent=face_extent, step=anchor_position)

    if face == NodeFace.LEFT:
        x = node.Canvas_position.x
        y = node.Canvas_position.y + edge_offset
    elif face == NodeFace.RIGHT:
        x = node.Canvas_position.x + node.Size.width
        y = node.Canvas_position.y + edge_offset
    elif face == NodeFace.TOP:
        y = node.Canvas_position.y + node.Size.height
        x = node.Canvas_position.x + edge_offset
    else:
        assert (face == NodeFace.BOTTOM)
        y = node.Canvas_position.y
        x = node.Canvas_position.x + edge_offset

    return Position(x, y)


class AnchoredStem(Stem):
    """
    A Stem on a Connector that it positioned by a Face Placement value
    specified by the user relative to the center of the Mode face.

        Attributes

        - Anchor position -– The user specified relative postion on the Node Face
    """

    def __init__(self, connector: 'Connector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, anchor_position: AnchorPosition):
        """
        Constructor

        :param connector: Reference to the Stem's Connector
        :param stem_type: Name of the Stem Type
        :param semantic: Name of the Stem's Semantic
        :param node: Reference to the Node where the Stem's root is attached
        :param face: Attached to this face of the Node
        :param anchor_position: The user specified point on the Node face where the Stem is attached
        """
        anchor = anchor_to_position(node, face, anchor_position)

        # Anchored position is used to compute the root end position
        Stem.__init__(self, connector=connector, stem_type=stem_type,
                      semantic=semantic, node=node, face=face, root_position=anchor)
