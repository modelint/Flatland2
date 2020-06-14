"""
connector_type.py

Connector and stem type specification
"""
from enum import Enum
from collections import namedtuple
# from diagram_type import DiagramTypeName
from draw_types import Stroke, StrokeWidth, StrokeStyle
from connection_types import Geometry
from notation import Notation




class ConnectionRole(Enum):
    """
    Names of each relative position within a Connector
    """
    opposing = "binary stem to stem",
    tee = "tertiary node to connection line",
    trunk = "node to top of hierarchy",
    branch = "node to bottom of hierarchy",
    free = "unary node to open space"




connector_types = {
    DiagramTypeName.CD: {
        ConnectorTypeName.binary_assoc: Geometry.B,
        ConnectorTypeName.assoc_class: Geometry.T,
        ConnectorTypeName.gen: Geometry.H
    },
    DiagramTypeName.SMD: {
        ConnectorTypeName.init_trans: Geometry.U,
        ConnectorTypeName.del_trans: Geometry.U,
        ConnectorTypeName.trans: Geometry.B
    }
}

