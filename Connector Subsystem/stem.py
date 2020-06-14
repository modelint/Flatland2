"""
stem.py
"""

from flatland_types import NodeFace, Position, StemEnd
from layout_specification import default_unary_branch_length, undecorated_stem_clearance
from connector_type import StemTypeUsageID, stem_type_usages, ConnectionRole
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

    return 1


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
        self.Vine_end = compute_vine_position(
            connector_type=connector.Connector_type, diagram_type=connector.Diagram.Diagram_type,
            stem_type=stem_type
        )

    def compute_vine_end(self):
        # We need the distance of the Vine end away from the node face
        # This is determined by the Stem Type Usage role, so we look that up first
        # For a free usage, this is just the standard length
        # For an opposing usage, this is the clearance distance
        # For a tee usage, this is determined after working out where the connector is drawn
        # for a trunk usage, it is the clearance distance
        # for a branch usage, it is the clearance distance
        # We factor in the direction (horizontal or vertical) and add to either the Root_end x or y coordinate

        stkey = StemTypeUsageID(
            connector_type=self.Connector.Connector_type, diagram_type=self.Connector.Diagram.Diagram_type,
            stem_type=self.Stem_type
        )
        usage = stem_type_usages[stkey]
        # Compute distance along x or y axis
        if usage == ConnectionRole.free:
            stem_length = default_unary_branch_length
        else:
            # Get root and vine decoration stems if any
            vine_query = DecoratedStemEndID(
                stem_type=self.Stem_type, semantic=self.Semantic, dtype=self.Connector.Diagram.Diagram_type,
                notation=self.Connector.Diagram.Notation, end=StemEnd.VINE)
            vine_decoration = decorated_stem_ends[vine_query].get()
            vine_clearance = 0 if not vine_decoration else vine_decoration.clearance
            root_query = DecoratedStemEndID(
                stem_type=self.Stem_type, semantic=self.Semantic, dtype=self.Connector.Diagram.Diagram_type,
                notation=self.Connector.Diagram.Notation, end=StemEnd.ROOT)
            root_decoration = decorated_stem_ends[root_query].get()
            root_clearance = 0 if not root_decoration else root_decoration.clearance
            stem_length = root_clearance + vine_clearance or undecorated_stem_clearance

        if usage != ConnectionRole.tee:
            # In the tee case, we need to figure out where the vine meets the connector line first

            if self.Node_face == NodeFace.TOP or self.Node_face == NodeFace.BOTTOM:
                return Position(self.Root_end.x, self.Node_face.value * (self.Root_end.y + stem_length))
            else:
                return Position(self.Root_end.y, self.Node_face.value * (self.Root_end.x + stem_length))
        else:
            # For now we will just return the root position with no change
            return self.Root_end

    def render(self):
        """
        Draw self
        """
        # Draw the root if any
        # Start with node face and position
        # Draw the root end decoration if any

        # Draw the vine end if any
        # Cases: Binary (just draw it), Unary, just draw it, Tertiary (need connector position)
        pass
