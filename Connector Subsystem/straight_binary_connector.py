"""
straight_binary_connector.py
"""
from flatland_exceptions import UnsupportedConnectorType
from binary_connector import BinaryConnector
from anchored_stem import AnchoredStem
from connection_types import HorizontalFace, Connector_Name
from floating_binary_stem import FloatingBinaryStem
from tertiary_stem import TertiaryStem
from geometry_types import Rect_Size, Position
from typing import TYPE_CHECKING, Optional
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
        - Tertiary_stem -- A Stem that connects from a separate a Node (other than the one attached to the Projecting
          or Floating Stems) and extending until its Vine end attaches to the Binary Connector line
    """

    def __init__(self, diagram: 'Diagram', connector_type: str, projecting_stem: New_Stem,
                 floating_stem: New_Stem, name: Optional[Connector_Name] = None, tertiary_stem=None):
        """
        Constructor – see class description for meaning of the attributes

        :param diagram: Reference to the Diagram
        :param connector_type: Name of connector type
        :param projecting_stem: A user supplied form requesting a projecting stem
        :param floating_stem: A user supplied form requesting a floating stem
        :param tertiary_stem: An optional user supplied form requesting a tertiary stem
        """
        # Verify that the specified connector type name corresponds to a supported connector type
        # found in our database
        try:
            ct = diagram.Diagram_type.ConnectorTypes[connector_type]
        except IndexError:
            raise UnsupportedConnectorType(
                connector_type_name=connector_type, diagram_type_name=diagram.Diagram_type.Name)
        # Extract the user supplied connector name if any
        BinaryConnector.__init__(self, diagram=diagram, name=name, connector_type=ct)

        # Look up the stem type loaded from our database
        projecting_stem_type = self.Connector_type.Stem_type[projecting_stem.stem_type]
        floating_stem_type = self.Connector_type.Stem_type[floating_stem.stem_type]
        tertiary_stem_type = None
        if tertiary_stem:
            tertiary_stem_type = self.Connector_type.Stem_type[tertiary_stem.stem_type]

        self.Projecting_stem = AnchoredStem(
            connector=self,
            stem_type=projecting_stem_type,
            semantic=projecting_stem.semantic,
            node=projecting_stem.node,
            face=projecting_stem.face,
            anchor_position=projecting_stem.anchor
        )
        self.Floating_stem = FloatingBinaryStem(
            connector=self,
            stem_type=floating_stem_type,
            semantic=floating_stem.semantic,
            node=floating_stem.node,
            face=floating_stem.face,
            projecting_stem=self.Projecting_stem
        )
        self.Tertiary_stem = None
        if tertiary_stem:
            self.Tertiary_stem = TertiaryStem(
                connector=self,
                stem_type=tertiary_stem_type,
                semantic=tertiary_stem.semantic,
                node=tertiary_stem.node,
                face=tertiary_stem.face,
                anchor_position=tertiary_stem.anchor,
                parallel_segs={(self.Projecting_stem.Vine_end, self.Floating_stem.Vine_end)}
            )

        self.Projecting_stem.render()
        self.Floating_stem.render()
        if self.Tertiary_stem:
            self.Tertiary_stem.render()

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
        """

        """
        # Create line from vine end of Projecting Binary Stem to vine end of Floating Binary Stem
        tablet = self.Diagram.Canvas.Tablet
        print("Drawing binary connector")
        tablet.add_line_segment(
            asset='binary connector', from_here=self.Projecting_stem.Vine_end, to_there=self.Floating_stem.Vine_end
        )
        if self.Tertiary_stem:
            self.Tertiary_stem.render()

        # Get size of bounding box
        # We assume that the name is a single line of text so we don't consider leading
        # Since, for now at least, we assume that a Connector name will be short, like 'R314' for example
        line_ink_area, leading = tablet.text_size(asset=self.Connector_type.Name+' name', text_line=self.Name.text)
        name_bounding_box = Rect_Size(width=line_ink_area.width, height=line_ink_area.height)
        name_spec = self.Connector_type.Name_spec

        # We will center the name bounding box with respect to the full length of the Connector
        # So we measure between root ends (node faces)
        p_end, f_end = self.Projecting_stem.Root_end, self.Floating_stem.Root_end
        if p_end.y == f_end.y:
            # Connector is horizontal
            center_x = round(abs(p_end.x - f_end.x)/2) + min(p_end.x, f_end.x)  # Distance type is an integer
            name_x = center_x - round(name_bounding_box.width/2)
            # If box is below the connector, subtract the height of the box as well to get lower left corner y
            height_offset = name_bounding_box.height if self.Name.side == -1 else 0
            name_y = p_end.y + name_spec.axis_buffer.vertical*self.Name.side - height_offset
        else:
            # Connector is vertical
            center_y = round(abs(p_end.y - f_end.y)/2) + min(p_end.y, f_end.y)
            name_y = center_y - round(name_bounding_box.height/2)
            # If box is left of the connector, subtract the width of the box as well to get the lower left corner x
            width_offset = name_bounding_box.width if self.Name.side == -1 else 0
            name_x = p_end.x + name_spec.axis_buffer.horizontal*self.Name.side - width_offset

        tablet.add_text(asset=self.Connector_type.Name+' name', lower_left=Position(name_x, name_y), text=self.Name.text)





        # TODO: Draw the connector name, if any
