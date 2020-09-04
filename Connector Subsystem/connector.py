"""
connector.py - Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram
"""
from flatland_exceptions import InvalidNameSide
from connector_type import ConnectorType
from connection_types import Connector_Name
from geometry_types import Rect_Size
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

    def render(self):
        pass  # overriden

    def __repr__(self):
        return f'ID: {id(self)}, Diagram: {self.Diagram}, Type: {self.Connector_type.Name}, Name: {self.Name}'
