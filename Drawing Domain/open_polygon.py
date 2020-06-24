"""
open_polygon.py
"""
from draw_types import Line, Stroke


class OpenPolygon():
    """
    A contiguous series of line segments that can draw itself on the Tablet
    """
    def __init__(self, tablet, style, width, points):
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
            self.Tablet.Lines.append(Line(
                        line_style=Stroke(self.Width, pattern=self.Style),
                        from_here=from_p, to_there=to_p))


