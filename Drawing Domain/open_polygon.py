"""
open_polygon.py
"""
from typing import TYPE_CHECKING
from geometry_types import Position

if TYPE_CHECKING:
    from tablet import Tablet


class OpenPolygon:
    """
    A contiguous series of line segments that can draw itself on the Tablet
    """

    def __init__(self, tablet: 'Tablet', asset: str, points: Position):
        """
        Constructor

        :param tablet: Reference to the Tablet
        :param asset: Used by Tablet to look up the line style
        :param points: A sequence of Points
        """
        assert len(points) > 1, "Open polygon has less than two points"
        self.Asset = asset
        self.Points = points
        self.Tablet = tablet

    def render(self):
        """
        Add a line segment to the Tablet for each successive pair of Points
        """
        for from_p, to_p in zip(self.Points, self.Points[1:]):
            self.Tablet.add_line_segment(asset=self.Asset, from_here=from_p, to_there=to_p)
