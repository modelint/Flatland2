"""
stem.py
"""

from connection_types import NodeFace, StemEnd
from geometry_types import Position
from layout_specification import default_unary_branch_length, undecorated_stem_clearance
from connector_type import ConnectionRole
from decorated_stem_end import decorated_stem_ends, DecoratedStemEndID


def compute_vine_position(connector_type, diagram_type, stem_type):
    # We need the distance of the Vine end away from the node face
    # This is determined by the Stem Type Usage role, so we look that up first
    # For a free usage, this is just the standard length
    # For an opposing usage, this is the clearance distance
    # For a tee usage, this is determined after working out where the connector is drawn
    # for a trunk usage, it is the clearance distance
    # for a branch usage, it is the clearance distance
    # We factor in the direction (horizontal or vertical) and add to either the Root_end x or y coordinate

    # Look up the role that this Stem Type plays in the specified Connector Type
    role = stem_type_usages[
        StemTypeUsageID(
            connector_type=connector_type, diagram_type=diagram_type,
            stem_type=stem_type
        )]

    if role == ConnectionRole.free:
        stem_length = default_unary_branch_length

    return 1  # TODO: Not the real value, just for testing. Not used for rendering


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
                 connector, stem_type, semantic, node, node_face, root_position):
        self.Connector = connector
        self.Stem_type = stem_type
        self.Node = node
        self.Node_face = node_face
        self.Semantic = semantic
        self.Root_end = root_position
        self.Vine_end = self.Root_end  # Should be overridden by the subclasses

    def render(self):
        """
        Draw self
        """
        # Overriden by the subclass
        pass
