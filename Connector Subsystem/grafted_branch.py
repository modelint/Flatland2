"""
grafted_branch.py
"""
from branch import Branch
from anchored_tree_stem import AnchoredTreeStem
from typing import Set, Optional, TYPE_CHECKING
from connection_types import Orientation, HorizontalFace, NodeFace
from floating_leaf_stem import FloatingLeafStem
from geometry_types import Line_Segment, Position
from general_types import Index

if TYPE_CHECKING:
    from tree_connector import TreeConnector


# Here we take a new leaf spec, create a floating leaf stem and attach it to our grafted branch
# which specifies the grafting anchored tree stem


class GraftedBranch(Branch):
    """
    Grafted Branch
    """

    def __init__(self, order: Index, connector: 'TreeConnector', hanging_stems: Set[AnchoredTreeStem],
                 grafting_stem: AnchoredTreeStem, new_floating_stem):

        self.Grafting_stem = grafting_stem

        # Set the branch axis based on the graft stem x or y depending on face orientation
        if self.Grafting_stem.Node_face in HorizontalFace:
            axis = grafting_stem.Root_end.x
            axis_orientation = Orientation.Vertical
        else:
            axis = grafting_stem.Root_end.y
            axis_orientation = Orientation.Horizontal

        # Unpack any Floating Stem
        self.Floating_stem = None if not new_floating_stem else self.unpack_floating_leaf(new_floating_stem,
                                                                                          grafting_stem,
                                                                                          axis_orientation, axis)

        Branch.__init__(self, order, axis, connector, hanging_stems, axis_orientation)

    def unpack_floating_leaf(self, new_floating_leaf, grafting_stem,
                             axis_orientation, axis) -> FloatingLeafStem:
        if axis_orientation == Orientation.Horizontal:
            x = new_floating_leaf.node.Face_position(new_floating_leaf.face)
            y = axis
        else:
            x = axis
            y = new_floating_leaf.node.Face_position(new_floating_leaf.face)
        vine_position = root_position = Position(x, y)

        return FloatingLeafStem(
            connector=self,
            stem_type=new_floating_leaf.stem_type,
            semantic=new_floating_leaf.semantic,
            node=new_floating_leaf.node,
            face=new_floating_leaf.face,
            grafted_branch=grafting_stem,
            root_position=root_position,
            vine_position=vine_position
        )

    @property
    def Shoot(self) -> Line_Segment:
        """
        The Shoot is simply a line segment from the vine end of the grafting Anchored Tree Stem to the
        vine end of the Floating Leaf Stem
        :return: The line segment to draw
        """
        if self.Floating_stem:
            return Line_Segment(from_position=self.Grafting_stem.Vine_end, to_position=self.Floating_stem.Vine_end)
        else:
            return super().Shoot
