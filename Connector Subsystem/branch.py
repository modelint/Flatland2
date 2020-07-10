"""
branch.py
"""
from typing import Set
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Line_Segment, Position
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle
from connection_types import Orientation


class Branch:
    def __init__(self, order: int, axis: float, connector, hanging_stems: Set[AnchoredTreeStem],
                 axis_orientation: Orientation):
        self.Order = order
        self.Connector = connector
        self.Hanging_stems = hanging_stems
        self.Axis = axis
        self.Axis_orientation = axis_orientation

    @property
    def Line_segment(self):
        return Line_Segment(Position(0, 0), Position(0, 0))

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
