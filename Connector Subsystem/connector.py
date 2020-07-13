"""
connector.py

Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram

Attributes
---

"""
from typing import TYPE_CHECKING
from connector_type import ConnectorTypeName

if TYPE_CHECKING:
    from diagram import Diagram


class Connector:
    """
    A Connector is a set of Stems connected by one or more lines to form a contiguous branch bringing
    one or more Nodes into a drawn model level relationship. On a class diagram, for example, a Connector
    is drawn for each binary association, generalization and association class relationship.

    The Connector Type and its Stem Types determine how the Connector should be drawn.

    Attributes
    ---
    Diagram : Connector is drawn on this diagram
    Connector_type : Specifies characteristics of this Connector
    """

    def __init__(self, diagram: 'Diagram', connector_type: ConnectorTypeName):
        self.Diagram = diagram
        self.Connector_type = connector_type
        self.Diagram.Grid.Connectors.append(self)

    def render(self):
        pass  # overriden
