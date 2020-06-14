""" floating_binary_stem.py """

from stem import Stem
from flatland_types import NodeFace


class FloatingBinaryStem(Stem):
    """
    A Stem on a Straight Binary Connector that it positioned laterally on a Node face
    so that it lines up with an opposing Anchored Stem. Consequenlty, no anchor position
    is specified, just an x or y location representing where the straight connector line intersects
    the floating stem's attached node face.

    """
    def __init__(self, connector, stem_type, semantic, node, face, projecting_stem):
        # We will use either the x or y of our opposing Anchored Stem and then set the other coordinate
        # to coincide with the Node face position attached to Floating Stem since this is a Straight Binary
        # Connector

        # Initially set the Floating Stem root end to match the Projecting Stem root end
        x, y = projecting_stem.Root_end

        # left and right faces are vertical, so they determine the x coordinate
        if face == NodeFace.LEFT:
            x = node.Canvas_position.x
        elif face == NodeFace.RIGHT:
            x = node.Canvas_position.x + node.Size.Rect_Size.width
        # top and bottom faces are horizontal, so they determine the y coordinate
        elif face == NodeFace.TOP:
            y = node.Canvas_position.y + node.Size.Rect_Size.height
        elif face == NodeFace.BOTTOM:
            y = node.Canvas_position.y

        # Stem initialized with our computed root end
        Stem.__init__(
            connector, stem_type, semantic, node, face, root_position=(x, y))

    def render(self):
        """
        Draw self
        """
        pass
