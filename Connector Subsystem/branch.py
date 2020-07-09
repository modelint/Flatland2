"""
branch.py
"""
from typing import Set
from anchored_tree_stem import AnchoredTreeStem
from geometry_types import Line_Segment, Position
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle


class Branch:
    def __init__(self, order: int, axis: float, hanging_stems: Set[ AnchoredTreeStem ]):
        self.Order = order
        self.Connector = None  # Overriden
        self.Hanging_stems = hanging_stems
        self.Axis = axis

    @property
    def Line_segment(self):
        return Line_Segment( Position(0, 0), Position(0, 0))

    def render(self):
        tablet = self.Connector.Diagram.Canvas.Tablet
        tablet.Lines.append(Line(
            line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
            from_here=self.Line_segment.from_position, to_there=self.Line_segment.to_position)
        )
