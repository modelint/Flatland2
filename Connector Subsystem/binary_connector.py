"""
binary_connector.py
"""
from connector import Connector
from connector_type import ConnectorType
from typing import TYPE_CHECKING

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

    def __init__(self, diagram: 'Diagram', connector_type: ConnectorType):
        """
        Constructor

        :param diagram: Reference to the Diagram
        :param connector_type: Name of the Connector Type
        """
        Connector.__init__(self, diagram=diagram, connector_type=connector_type)

    def render(self):
        pass  # Overridden
