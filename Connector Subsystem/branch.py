"""
branch.py
"""
from typing import Set, TYPE_CHECKING
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Line_Segment, Position, Coordinate
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle
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

    def render(self):
        print(self.Line_segment)
        tablet = self.Connector.Diagram.Canvas.Tablet
        # Draw the axis
        tablet.Lines.append(Line(
            line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
            from_here=self.Line_segment.from_position, to_there=self.Line_segment.to_position)
        )
        # Draw the stems
        for s in self.Hanging_stems:
            if self.Axis_orientation == Orientation.Horizontal:
                x = s.Vine_end.x
                y = self.Axis
            else:
                x = self.Axis
                y = s.Vine_end.y

            tablet.Lines.append(Line(
                line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                from_here=s.Vine_end, to_there=Position(x, y))
            )
