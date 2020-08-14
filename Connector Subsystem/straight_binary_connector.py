"""
straight_binary_connector.py
"""
from binary_connector import BinaryConnector
from anchored_stem import AnchoredStem
from connection_types import HorizontalFace
from floating_binary_stem import FloatingBinaryStem
from tertiary_stem import TertiaryStem
from typing import TYPE_CHECKING
from command_interface import New_Stem

if TYPE_CHECKING:
    from diagram import Diagram


class StraightBinaryConnector(BinaryConnector):
    """
    Connects two Stems with a straight line. One plays the role of a Projecting Binary Stem and the other is
    a Floating Binary Stem.

    The user has specified an anchor position (Face Placement value) for the projecting stem. Its root end will
    be placed at this position. For the floating stem, either the x or y value will be shared with the projecting
    stem with the other value coinciding with the axis of the attached Node face.

    Because, if the user specified two separate anchor positions, they might not line up vertically or
    horizontally and we would end up with a diagonal line which we never want.

    If a Tertiary Stem is supplied, it will anchor to some Node face and extend in a straight line to a position
    on the Binary Connector line between the two vine ends of the Binary Stems. Since it must be a straight line,
    the Tertiary Stem may not be attached to a face on any Node attached to the Binary Stems.

        Attributes

        - Projecting_stem -– The Binary Stem that is anchored to a user specified position on one Node Face
        - Floating_stem -– The opposite Binary Stem that is placed on a direct line opposite the Projecting stem
        where it touches the opposing face of its attached Node
    """

    def __init__(self, diagram: 'Diagram', connector_type: str, projecting_stem: New_Stem,
                 floating_stem: New_Stem, tertiary_stem=None):
        BinaryConnector.__init__(self, diagram, connector_type)

        self.Projecting_stem = AnchoredStem(
            connector=self,
            stem_type=projecting_stem.stem_type,
            semantic=projecting_stem.semantic,
            node=projecting_stem.node,
            face=projecting_stem.face,
            anchor_position=projecting_stem.anchor
        )
        self.Floating_stem = FloatingBinaryStem(
            connector=self,
            stem_type=floating_stem.stem_type,
            semantic=floating_stem.semantic,
            node=floating_stem.node,
            face=floating_stem.face,
            projecting_stem=self.Projecting_stem
        )
        self.Tertiary_stem = None
        if tertiary_stem:
            self.Tertiary_stem = TertiaryStem(
                connector=self,
                stem_type=tertiary_stem.stem_type,
                semantic=tertiary_stem.semantic,
                node=tertiary_stem.node,
                face=tertiary_stem.face,
                anchor_position=tertiary_stem.anchor,
                parallel_segs={(self.Projecting_stem.Vine_end, self.Floating_stem.Vine_end)}
            )

        self.Projecting_stem.render()
        self.Floating_stem.render()

    def compute_axis(self):
        """
        Determines the x or y axis of the straight connector line where the Tertiary Stem attaches.
        The Tertiary Stem will know whether or not the returned value is x or y based on its own orientation.
        :return: x_or_y_axis
        """
        if self.Projecting_stem.Node_face in HorizontalFace:
            return self.Projecting_stem.Root_end.x
        else:
            return self.Projecting_stem.Root_end.y

    def render(self):
        # Create line from vine end of Projecting Binary Stem to vine end of Floating Binary Stem
        tablet = self.Diagram.Canvas.Tablet
        print("Drawing binary connector")
        tablet.add_line_segment(
            asset='binary connector', from_here=self.Projecting_stem.Vine_end, to_there=self.Floating_stem.Vine_end)
        if self.Tertiary_stem:
            self.Tertiary_stem.render()
