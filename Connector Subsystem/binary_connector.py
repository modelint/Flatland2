"""
binary_connector.py
"""
from connector import Connector
from connector_type import ConnectorType
from connection_types import Connector_Name
from geometry_types import Position
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from diagram import Diagram


class BinaryConnector(Connector):
    """
    Connects two Stems in a straight line or with a Bend Route. There may be a tertiary stem attached
    to the connecting line.

        Attributes

        - Tertiary_stem -– Currently managed in each subclass, but should be promted eventually
    """
    # TODO: Promote tertiary stem

    def __init__(self, diagram: 'Diagram', name: Optional[Connector_Name], connector_type: ConnectorType):
        """
        Constructor

        :param diagram: Reference to the Diagram
        :param connector_type: Name of the Connector Type
        """
        Connector.__init__(self, diagram=diagram, name=name, connector_type=connector_type)

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
        pass  # Overridden
