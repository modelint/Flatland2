"""
diagram_type.py

Represents the Diagram Type class structure and populates it

Attributes
---

diagram_types : dict
    Here we specify what kinds of nodes and connectors may appear on a given type of diagram. You cannot, put a state
    node on a class diagram, for example. Also we show what notations are supported for each Diagram Type.

"""

from names import DiagramTypeName, ConnectorTypeName, NodeTypeName
from notation import Notation


diagram_types = {
    DiagramTypeName.CD: {
        'nodes': {NodeTypeName.M_class, NodeTypeName.I_class},
        'connectors': {ConnectorTypeName.binary_assoc, ConnectorTypeName.assoc_class, ConnectorTypeName.gen},
        'notations': {Notation.SM, Notation.xUML, Notation.Starr}
    },
    DiagramTypeName.SMD: {
        'nodes': {NodeTypeName.State},
        'connectors': {ConnectorTypeName.init_trans, ConnectorTypeName.del_trans, ConnectorTypeName.init_trans},
        'notations': {Notation.xUML}
    },
    DiagramTypeName.CCD: {
        'nodes': {NodeTypeName.O_class, NodeTypeName.EE},
        'connectors': {ConnectorTypeName.comm},
        'notations': {Notation.xUML, Notation.Starr}
    },
    DiagramTypeName.DD: {
        'nodes': {NodeTypeName.Domain},
        'connectors': {ConnectorTypeName.bridge},
        'notations': {Notation.xUML, Notation.Starr}
    }
}
