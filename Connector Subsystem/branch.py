"""
branch.py
"""
from typing import Set, TYPE_CHECKING
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Line_Segment, Position, Coordinate
from connection_types import Orientation
from general_types import Index

if TYPE_CHECKING:
    from tree_connector import TreeConnector


class Branch:
    def __init__(self, order: Index, axis: Coordinate, connector: 'TreeConnector', hanging_stems: Set[AnchoredTreeStem],
                 axis_orientation: Orientation):
        self.Order = order
        self.Connector = connector
        self.Hanging_stems = hanging_stems
        self.Axis = axis
        self.Axis_orientation = axis_orientation

    @property
    def Shoot(self) -> Line_Segment:
        branches = self.Connector.Branches
        prev_axis = None if self.Order == 0 else branches[self.Order - 1].Axis
        next_axis = None if self.Order == len(branches) - 1 else branches[self.Order + 1].Axis
        positions = {a for a in {prev_axis, next_axis} if a}
        if self.Axis_orientation == Orientation.Horizontal:
            y = self.Axis
            positions = positions.union({s.Vine_end.x for s in self.Hanging_stems})
            x1 = min(positions)
            x2 = max(positions)
            return Line_Segment(from_position=Position(x1, y), to_position=Position(x2, y))
        else:
            x = self.Axis
            positions = positions.union({s.Vine_end.y for s in self.Hanging_stems})
            y1 = min(positions)
            y2 = max(positions)
        return Line_Segment(from_position=Position(x, y1), to_position=Position(x, y2))

    def render(self):
        print("Line segment is:", self.Shoot)
        tablet = self.Connector.Diagram.Canvas.Tablet
        # Draw the axis
        print("Drawing branch axis")
        tablet.add_line_segment(
            asset='gen connector', from_here=self.Shoot.from_position, to_there=self.Shoot.to_position
        )

        # Draw the stems
        for s in self.Hanging_stems:
            if self.Axis_orientation == Orientation.Horizontal:
                x = s.Vine_end.x
                y = self.Axis
            else:
                x = self.Axis
                y = s.Vine_end.y

            print("Drawing branch stem")
            tablet.add_line_segment(
                asset='gen connector', from_here=s.Vine_end, to_there=Position(x, y)
            )

