"""
binary_connector.py
"""
from connector import Connector
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from diagram import Diagram


class BinaryConnector(Connector):
    """
    Connects two Stems in a straight line or with a Bend Route. There may be a tertiary stem attached
    to the connecting line.

    Attributes:
    ---
    Tertiary_stem – An optional Tertiary Stem may be supplied with a user specified anchor position
    """

    def __init__(self, diagram: 'Diagram', connector_type: str):
        Connector.__init__(self, diagram, connector_type)

    def render(self):
        pass  # Overridden
