"""
grafted_branch.py
"""
from branch import Branch
from anchored_tree_stem import AnchoredTreeStem
from typing import Set, Optional, TYPE_CHECKING
from connection_types import Orientation, HorizontalFace, NodeFace
from floating_leaf_stem import FloatingLeafStem
from geometry_types import Position
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle, Color
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
        # Unpack any Floating Stem
        self.Floating_stem = self.unpack_floating_leaf(new_floating_stem, grafting_stem)

        # Set the branch axis based on the graft stem x or y depending on face orientation
        if self.Grafting_stem.Node_face in HorizontalFace:
            axis = grafting_stem.Root_end.x
            axis_orientation = Orientation.Vertical
        else:
            axis = grafting_stem.Root_end.y
            axis_orientation = Orientation.Horizontal
        Branch.__init__(self, order, axis, connector, hanging_stems, axis_orientation)

    def unpack_floating_leaf(self, new_floating_leaf, grafting_stem) -> Optional[FloatingLeafStem]:
        if new_floating_leaf:
            return FloatingLeafStem(
                connector=self,
                stem_type=new_floating_leaf.stem_type,
                semantic=new_floating_leaf.semantic,
                node=new_floating_leaf.node,
                face=new_floating_leaf.face,
                grafted_branch=grafting_stem
            )
        else:
            return None

