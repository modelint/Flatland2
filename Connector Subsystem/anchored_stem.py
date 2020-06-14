""" anchored_stem.py """

from stem import Stem
from flatland_types import NodeFace
from layout_specification import default_stem_positions


def anchor_to_position(node, face, anchor_position):
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
        face_extent = node.Size.Rect_Size.height
    else:
        face_extent = node.Size.Rect_Size.width

    # Compute center relative position to edge relative position by shifting the number line
    stem_step_size = face_extent / (default_stem_positions + 1)
    edge_relative_step = round(default_stem_positions / 2) + anchor_position
    edge_relative_distance = edge_relative_step * stem_step_size

    if face == NodeFace.LEFT:
        x = node.Canvas_position.x
        y = node.Canvas_position.y + edge_relative_distance
    elif face == NodeFace.RIGHT:
        x = node.Canvas_position.x + node.Size.Rect_Size.width
        y = node.Canvas_position.y + edge_relative_distance
    elif face == NodeFace.TOP:
        y = node.Canvas_position.y + node.Size.Rect_Size.height
        x = node.Canvas_position.x + edge_relative_distance
    else:
        assert (face == NodeFace.BOTTOM)
        y = node.Canvas_position.y
        x = node.Canvas_position.x + edge_relative_distance

    return x, y


class AnchoredStem(Stem):
    """
    A Stem on a Connector that it positioned by a Face Placement value
    specified by the user relative to the center of the Mode face.

    Attributes:
        Anchor position – The user specified relative postion on the Node Face
    """

    def __init__(self, connector, stem_type, semantic, node, face, anchor_position):
        self.Anchor_position = anchor_position  # We may need to refer back to this value in a future release

        # Anchored position is used to compute the root end position
        Stem.__init__(self, connector, stem_type, semantic, node, face,
                      root_position=anchor_to_position(node, face, anchor_position))
