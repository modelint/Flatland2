"""
tertiary_stem.py
"""

from anchored_stem import AnchoredStem
from connection_types import HorizontalFace, NodeFace
from geometry_types import Position
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle


class TertiaryStem(AnchoredStem):
    """
    An Anchored Stem that reaches from a Node face at its root end and attaches its vine end to a Binary Connector.
    """
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position, parallel_segs):
        AnchoredStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)

        if face in HorizontalFace:
            if face == NodeFace.TOP:
                isegs = {s for s in parallel_segs if s[0].y > self.Root_end.y}
                yval = min({s[0].y for s in isegs})
            elif face == NodeFace.BOTTOM:
                isegs = {s for s in parallel_segs if s[0].y < self.Root_end.y}
                yval = max({s[0].y for s in isegs})
            self.Vine_end = Position(x=self.Root_end.x, y=yval)
        else:
            if face == NodeFace.RIGHT:
                isegs = {s for s in parallel_segs if s[0].x > self.Root_end.x}
                xval = min({s[0].x for s in isegs})
            elif face == NodeFace.LEFT:
                isegs = {s for s in parallel_segs if s[0].x < self.Root_end.x}
                xval = max({s[0].x for s in isegs})
            self.Vine_end = Position(x=xval, y=self.Root_end.y)

        self.render()

    def render(self):
        """
        Create line from root end to the vine end attached to the Binary Connector line
        """
        tablet = self.Connector.Diagram.Canvas.Tablet
        # TODO: Look up the notation specified line style, for now always using UML dashed style
        tablet.Lines.append(Line(
            line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.DASHED),
            from_here=self.Root_end, to_there=self.Vine_end))
