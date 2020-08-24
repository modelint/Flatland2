"""
connector.py - Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram
"""
from connector_type import ConnectorType
from typing import TYPE_CHECKING

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
    """

    def __init__(self, diagram: 'Diagram', connector_type: ConnectorType):
        """
        Constructor

        :param diagram: Reference to the Diagram
        :param connector_type: Name of this Connector Type
        """
        self.Diagram = diagram
        self.Connector_type = connector_type

        self.Diagram.Grid.Connectors.append(self)

    def render(self):
        pass  # overriden

    def __repr__(self):
        return f'ID: {id(self)}, Diagram: {self.Diagram}, Type: {self.Connector_type.Name}'
