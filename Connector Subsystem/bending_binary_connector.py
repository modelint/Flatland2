"""
bending_binary_connector.py
"""
from binary_connector import BinaryConnector
from anchored_stem import AnchoredStem
from connection_types import HorizontalFace
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle
from geometry_types import Position


class BendingBinaryConnector(BinaryConnector):
    """
    This is a Binary Connector that must turn one or more corners to connect its opposing Binary Stems.
    In such a case the two Binary Stems will be counterparts and we can arbitrarily start drawing a line
    from one of the Counterpart Binary Stems to the other. In fact, we could start from both ends and work
    toward the middle or start from the middle and work our way out. So the terms “start” and “end” could
    just as easily have been labeled “A” and “B”.
    """

    def __init__(self, diagram, anchored_stem_t, anchored_stem_p, bends=[], tertiary_stem=None):
        BinaryConnector.__init__(self, diagram, tertiary_stem)

        self.T_stem = AnchoredStem(
            connector=self,
            stem_type=anchored_stem_t.stem_type,
            semantic=anchored_stem_t.semantic,
            node=anchored_stem_t.node,
            face=anchored_stem_t.face,
            anchor_position=anchored_stem_t.anchor
        )
        self.P_stem = AnchoredStem(
            connector=self,
            stem_type=anchored_stem_p.stem_type,
            semantic=anchored_stem_p.semantic,
            node=anchored_stem_p.node,
            face=anchored_stem_p.face,
            anchor_position=anchored_stem_p.anchor
        )

        self.T_stem.render()
        self.P_stem.render()
        self.render()

    def render(self):
        # Create line from vine end of T_stem to vine end of P_stem, bending along the way
        tablet = self.Diagram.Canvas.Tablet

        # TODO: accommodate multiple corners
        # For now assume only one corner, find that point
        if self.T_stem.Node_face in HorizontalFace:
            corner_x = self.T_stem.Root_end.x
            corner_y = self.P_stem.Root_end.y
        else:
            corner_x = self.P_stem.Root_end.x
            corner_y = self.T_stem.Root_end.y
        corner = Position(corner_x, corner_y)

        # Draw line from T stem root to corner
        tablet.Lines.append(Line(
            line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
            from_here=self.T_stem.Root_end, to_there=corner))

        # Draw line from P stem root to corner
        tablet.Lines.append(Line(
            line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
            from_here=self.P_stem.Root_end, to_there=corner))
