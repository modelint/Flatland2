"""
open_polygon.py
"""
from draw_types import Line, Stroke, Color, StrokeStyle, StrokeWidth
from typing import TYPE_CHECKING, List
from geometry_types import Position

if TYPE_CHECKING:
    from tablet import Tablet


class OpenPolygon():
    """
    A contiguous series of line segments that can draw itself on the Tablet
    """

    def __init__(self, tablet: 'Tablet', style: StrokeStyle, width: StrokeWidth, points: Position):
        self.Style = style
        self.Width = width
        assert len(points) > 1, "Open polygon has less than two points"
        self.Points = points
        self.Tablet = tablet

    def render(self):
        """
        Add a line segment to the Tablet for each successive pair of Points
        """
        for from_p, to_p in zip(self.Points, self.Points[1:]):
            self.Tablet.Line_segments.append(Line(
                line_style=Stroke(color=Color.CONN_PURPLE, width=self.Width, pattern=self.Style),
                from_here=from_p, to_there=to_p))
