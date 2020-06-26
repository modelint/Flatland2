"""
tertiary_stem.py
"""

from anchored_stem import AnchoredStem
from connection_types import HorizontalFace
from geometry_types import Position
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle


class TertiaryStem(AnchoredStem):
    """
    An Anchored Stem that reaches from a Node face at its root end and attaches its vine end to a Binary Connector.
    """
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position, binary_connector_position):
        AnchoredStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)
        # Set vine end tangent to the horizontal or vertical Binary Connector position
        if self.Node_face in HorizontalFace:
            x = self.Root_end.x
            y = binary_connector_position
        else:
            x = binary_connector_position
            y = self.Root_end.y
        self.Vine_end = Position(x,y)
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
