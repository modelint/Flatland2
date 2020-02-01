"""
flatland_types.py
"""

from collections import namedtuple
from enum import Enum


class StemEnd(Enum):
    ROOT = 0,
    VINE = 1

class NodeFace(Enum):
    TOP = 'top'
    BOTTOM = 'bottom'
    RIGHT = 'right'
    LEFT = 'left'


class StrokeWidth(Enum):
    THIN = 1
    NORMAL = 2
    THICK = 3


class StrokeStyle(Enum):
    SOLID = 1
    DASHED = 2


class TypeFace(Enum):
    """We'll start with a limited selection of typefaces that work nicely for drawing models"""
    PALATINO = 'Palatino Sans Informal LT Pro'
    GILLSANS = 'Gill Sans'
    FUTURA = 'Futura'
    HELVETICA = 'Helvetica'
    VERDANA = 'Verdana'


class FontWeight(Enum):
    NORMAL = 1
    BOLD = 2


class FontSlant(Enum):
    NORMAL = 1
    ITALIC = 2


class VertAlign(Enum):
    """The numeric values are low to high in the axis direction"""
    BOTTOM = 0
    CENTER = 1
    TOP = 2


class HorizAlign(Enum):
    """The numeric values are low to high in the axis direction"""
    LEFT = 0
    CENTER = 1
    RIGHT = 2


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
    U = "unary",
    B = "binary",
    T = "ternary",
    H = "hierarchical"


Stroke = namedtuple('Stroke', 'width pattern')
Line = namedtuple('Line', 'line_style from_here to_there')
Text_Style = namedtuple('Text_Style', 'typeface size slant weight')
Text_Line = namedtuple('Text_Line', 'lower_left style content')
Rectangle = namedtuple('Rectangle', 'line_style lower_left, size')
Position = namedtuple('Position', 'x y')
Rect_Size = namedtuple('Rect_Size', 'height width')
Alignment = namedtuple('Alignment', 'vertical horizontal')
Padding = namedtuple('Padding', 'top bottom left right')
Node_Type_Attrs = namedtuple('Node_Type_Attrs',
                             'corner_rounding compartments line_style default_size max_size')
Compartment_Type_Attrs = namedtuple('Compartment_Type_Attrs', 'alignment padding text_style')
New_Stem = namedtuple('New_Stem', 'stem_type connector_semantic node face position')

