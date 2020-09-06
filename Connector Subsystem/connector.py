"""
connector.py - Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram
"""
from flatland_exceptions import InvalidNameSide
from connector_type import ConnectorType
from connection_types import Connector_Name
from geometry_types import Rect_Size, Position
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from diagram import Diagram


class Connector:
    """
    A Connector is a set of Stems connected by one or more lines to form a contiguous branch bringing
    one or more Nodes into a drawn model level relationship. On a class diagram, for example, a Connector
    is drawn for each binary association, generalization and association class relationship.

    The Connector Type and its Stem Types determine how the Connector should be drawn.

        Attributes

        - Diagram -- Connector is drawn on this diagram
        - Connector_type -- Specifies characteristics of this Connector
        - Name -- Optional name of this Connector
    """

    def __init__(self, diagram: 'Diagram', name: Optional[Connector_Name], connector_type: ConnectorType):
        """
        Constructor

        :param diagram: Reference to the Diagram
        :param connector_type: Name of this Connector Type
        """
        self.Diagram = diagram
        self.Connector_type = connector_type
        self.Name = name
        self.Name_size = None
        if self.Name:
            if self.Name.side not in {1, -1}:
                raise InvalidNameSide(self.Name.side)
            tablet = self.Diagram.Canvas.Tablet
            # Get size of bounding box
            # We assume that the name is a single line of text so we don't consider leading
            # Since, for now at least, we assume that a Connector name will be short, like 'R314' for example
            line_ink_area, leading = tablet.text_size(asset=self.Connector_type.Name+' name', text_line=self.Name.text)
            self.Name_size = Rect_Size(width=line_ink_area.width, height=line_ink_area.height)

        self.Diagram.Grid.Connectors.append(self)

    def compute_name_position(self, point_t: Position, point_p: Position) -> Position:
        """
        Determine the lower left corner position of this Connector's name

        :param point_t: Point closest to the T Node
        :param point_p: Point closest to the P Node (furthest from the T Node)
        :return: Position of name bounding box lower left corner
        """
        name_spec = self.Connector_type.Name_spec  # For easy access below
        if point_t.y == point_p.y:
            # Bend is horizontal
            center_x = round(abs(point_t.x - point_p.x) / 2) + min(point_t.x, point_p.x)  # Distance type is an integer
            name_x = center_x - round(self.Name_size.width / 2)
            # If box is below the connector, subtract the height of the box as well to get lower left corner y
            height_offset = self.Name_size.height if self.Name.side == -1 else 0
            name_y = point_t.y + name_spec.axis_buffer.vertical * self.Name.side - height_offset
        else:
            # Connector is vertical
            center_y = round(abs(point_t.y - point_p.y) / 2) + min(point_t.y, point_p.y)
            name_y = center_y - round(self.Name_size.height / 2)
            # If box is left of the connector, subtract the width of the box as well to get the lower left corner x
            width_offset = self.Name_size.width if self.Name.side == -1 else 0
            name_x = point_t.x + name_spec.axis_buffer.horizontal * self.Name.side - width_offset
        return Position(name_x, name_y)

    def render(self):
        pass  # overriden

    def __repr__(self):
        return f'ID: {id(self)}, Diagram: {self.Diagram}, Type: {self.Connector_type.Name}, Name: {self.Name}'
