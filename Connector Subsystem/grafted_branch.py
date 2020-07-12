"""
grafted_branch.py
"""
from branch import Branch
from anchored_tree_stem import AnchoredTreeStem
from typing import Set, Optional, TYPE_CHECKING
from connection_types import Orientation
from floating_leaf_stem import FloatingLeafStem
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
        # TODO: These are dummy values waiting for this type of branch to be implemeneted
        self.Floating_stem = self.unpack_floating_leaf(new_floating_stem, grafting_stem)
        axis = 0
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
