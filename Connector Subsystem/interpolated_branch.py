"""
interpolated_branch.py
"""

from branch import Branch
from connection_types import NodeFace, HorizontalFace, Orientation
from typing import Set
from flatland_exceptions import BranchCannotBeInterpolated
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Position, Line_Segment


class InterpolatedBranch(Branch):
    def __init__(self, order: int, connector, hanging_stems: Set[AnchoredTreeStem]):
        # The axis of this branch is either an x or y canvas coordinate value
        # An Interpolated Branch is always drawn between sets of opposing stems
        # The stems either rise and descend vertically to meet on a horizontal axis
        # or extend rightward and leftward to meet on a vertical axis

        # If an interpolated branch was specified by the user but there are no opposing stems/faces
        # there is a user error

        # All node faces for downward or leftward stems will have the highest y or x values
        # The opposing faces will then have the lowest y or x values
        # We then take the middle point between the lowest high value and the highest of the low values
        # By adding this to the highest low value we get the canvas coordinate of the branch axis

        downward_stems = {s for s in hanging_stems if s.Node_face == NodeFace.BOTTOM}
        axis_orientation = Orientation.Horizontal if downward_stems else Orientation.Vertical
        high_stems = downward_stems if downward_stems else {s for s in hanging_stems if s.Node_face == NodeFace.LEFT}
        low_stems = hanging_stems - high_stems
        if not low_stems and high_stems:
            raise BranchCannotBeInterpolated
        lowest_high_face = min({s.Node.Face_position(s.Node_face) for s in high_stems})
        highest_low_face = max({s.Node.Face_position(s.Node_face) for s in low_stems})
        assert highest_low_face < lowest_high_face
        axis = highest_low_face + (lowest_high_face - highest_low_face) / 2
        Branch.__init__(self, order, axis, connector, hanging_stems, axis_orientation)

    @property
    def Line_segment(self):
        branches = self.Connector.Branches
        prev_axis = None if self.Order == 0 else branches[self.Order-1].Axis
        next_axis = None if self.Order == len(branches)-1 else branches[self.Order+1].Axis
        if self.Axis_orientation == Orientation.Horizontal:
            y = self.Axis
            x1 = prev_axis if prev_axis else min({s.Vine_end.x for s in self.Hanging_stems})
            x2 = next_axis if next_axis else max({s.Vine_end.x for s in self.Hanging_stems})
            return Line_Segment( from_position=Position(x=x1, y=y), to_position=Position(x=x2, y=y) )
        else:
            x = self.Axis
            y1 = prev_axis if prev_axis else min({s.Vine_end.y for s in self.Hanging_stems})
            y2 = next_axis if next_axis else max({s.Vine_end.y for s in self.Hanging_stems})
            return Line_Segment( from_position=Position(x=x, y=y1), to_position=Position(x=x, y=y2) )

