"""
rut_branch.py
"""

from branch import Branch
from connection_types import Path, NodeFace, HorizontalFace, Orientation
from typing import Set
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Position, Line_Segment


class RutBranch(Branch):
    def __init__(self, order: int, connector, path: Path, hanging_stems: Set[AnchoredTreeStem]):
        """
        The user may specify placment of a Branch along a Branch Path which defines a Lane
        (Row or Column, depending on orientation) in a rut position (center, off-center +1, etc).

        :param order: Ordinal value used as index into the Tree Connector branch sequence
        :param connector: The Tree Connector
        :param path: Lane and rut where the Branch axis is drawn
        :param hanging_stems: A set of Anchored Tree Stems hanging on the Rut Branch
        """

        # Compute the branch axis and orientation so we can init the superclass
        axis_orientation = Orientation.Horizontal \
            if list(hanging_stems)[0].Node_face in HorizontalFace else Orientation.Vertical
        axis_position = connector.Diagram.Grid.get_rut(path.lane, path.rut, axis_orientation)
        Branch.__init__(self, order, axis_position, connector, hanging_stems, axis_orientation)

