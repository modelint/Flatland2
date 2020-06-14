"""
binary_connector.py
"""
from connector import Connector

class BinaryConnector(Connector):
    """
    Connects two Stems in a straight line or with a Bend Route. There may be a tertiary stem attached
    to the connecting line.

    Attributes:
    ---
    Tertiary_stem – An optional Tertiary Stem may be supplied with a user specified anchor position
    """
    def __init__(self, diagram, connector_type, tertiary_stem):
        Connector.__init__(diagram, connector_type)
