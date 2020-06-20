"""
binary_connector.py
"""
from connector import Connector
from names import ConnectorTypeName


class BinaryConnector(Connector):
    """
    Connects two Stems in a straight line or with a Bend Route. There may be a tertiary stem attached
    to the connecting line.

    Attributes:
    ---
    Tertiary_stem – An optional Tertiary Stem may be supplied with a user specified anchor position
    """
    def __init__(self, diagram, tertiary_stem):
        Connector.__init__(self, diagram, connector_type=ConnectorTypeName.binary_assoc)
