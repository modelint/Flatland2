"""
connection_types.py

Data types to support Connectors and Stems
"""

from enum import Enum


class LaneOrientation(Enum):
    """
    Two possible Lane orientations
    """
    ROW = 0
    COLUMN = 1


class StemEnd(Enum):
    ROOT = 0
    VINE = 1


class NodeFace(Enum):
    """
    Values are multiplied by absolute distance to get an x or y coordinate.
    """
    TOP = 0
    BOTTOM = 1
    RIGHT = 2
    LEFT = 3

HorizontalFace = {NodeFace.TOP, NodeFace.BOTTOM}

OppositeFace = {
    NodeFace.TOP: NodeFace.BOTTOM,
    NodeFace.BOTTOM: NodeFace.TOP,
    NodeFace.LEFT: NodeFace.RIGHT,
    NodeFace.RIGHT: NodeFace.LEFT
}


class Geometry(Enum):
    """
    This describes the way that a Connector is drawn, pulling together all of its Stems. Many geometries are possible,
    but only a handful are supported which should cover a wide range of diagramming possibilities.

    Unary (U) – Relationship is rooted in some Node on one end and not connected on the other end. An initial
    transition on a state machine diagram is one example where the target state is connected and the other end
    of the transition just has a dark circle drawn at the other end (not a Node). It consists of a single Stem.

    Binary (B) – Relationship is drawn from one Node face position to another on the same or a different Node.
    This could be a state transition with a from and to state or a binary association from one class to another
    or a reflexive relationship starting and ending on the same class or state. It consists of two Stems, one
    attached to each Node face position connected together with a line.

    Ternary (T) – This is a binary relationship with an additional Stem connecting to the line between the binary
    relationship Stems. A typical example is a class diagram association class where a third Stem emanates from the
    association class Node connecting to the line between the binary relationship Stems.

    Hierarchical (H) – Here one Node is a root connecting to two or more other Nodes. A Stem emanates from the root
    Node and another type of Stem emanates from each of the subsidiary Nodes and one or more lines are drawn to
    connect all the Stems. A class diagram generalization relationship is a typical case.
    """
    U = "unary"
    B = "binary"
    T = "ternary"
    H = "hierarchical"


