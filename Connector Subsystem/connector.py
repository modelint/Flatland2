"""
connector.py

Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram

Attributes
---

"""
from flatland_exceptions import UnknownConnectorType, IncompatibleConnectorType
from collections import namedtuple
from typing import TYPE_CHECKING
from flatlanddb import FlatlandDB as fdb

if TYPE_CHECKING:
    from diagram import Diagram

ConnectorType = namedtuple('ConnectorType', 'Name About Geometry')


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

    def __init__(self, diagram: 'Diagram', connector_type: str):
        self.Diagram = diagram

        # Validate connector type
        ctypes = fdb.MetaData.tables['Connector Type']
        q = ctypes.select(ctypes.c['Name'] == connector_type)
        i = fdb.Connection.execute(q).fetchone()
        if not i:
            raise UnknownConnectorType
        # if i['Diagram type'] != self.Diagram.Diagram_type:
        #     raise IncompatibleConnectorType

        self.Connector_type = ConnectorType(Name=i['Name'], About=i['About'], Geometry=i['Geometry'])
        self.Diagram.Grid.Connectors.append(self)

    def render(self):
        pass  # overriden

    def __repr__(self):
        return f'ID: {id(self)}, Diagram: {self.Diagram}, Type: {self.Connector_type.Name}'
