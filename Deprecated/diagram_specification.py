""" diagram_specification.py - Defines all of the known node types and their properties """

from collections import namedtuple
from enum import Enum
from flatland_types import StrokeStyle, Rect_Size


class DiagramTypeName(Enum):
    CLASS_DIAGRAM = 'class'
    STATE_DIAGRAM = 'state'
    COLLABORATION_DIAGRAM = 'collaboration'
    DOMAIN_DIAGRAM = 'domain'


NodeTypeTuple = namedtuple('Node_Type', 'rounded, compartments, border, default_size, max_size')
node_types = {
    'class': NodeTypeTuple(rounded=False, compartments=3, border=StrokeStyle.SOLID,
                           default_size=Rect_Size(width=110, height=80), max_size=Rect_Size(width=144, height=180)),

    'imported class': NodeTypeTuple(rounded=False, compartments=2, border=StrokeStyle.DASHED,
                                    default_size=Rect_Size(width=110, height=80),
                                    max_size=Rect_Size(width=144, height=180)),

    'state': NodeTypeTuple(rounded=True, compartments=2, border=StrokeStyle.SOLID,
                           default_size=Rect_Size(width=110, height=50), max_size=Rect_Size(width=300, height=108)),

    'external entity': NodeTypeTuple(rounded=False, compartments=1, border=StrokeStyle.SOLID,
                                     default_size=Rect_Size(width=100, height=25),
                                     max_size=Rect_Size(width=300, height=60)),

    'class overview': NodeTypeTuple(rounded=False, compartments=1, border=StrokeStyle.SOLID,
                                    default_size=Rect_Size(width=100, height=25),
                                    max_size=Rect_Size(width=300, height=60)),

    'domain': NodeTypeTuple(rounded=True, compartments=1, border=StrokeStyle.SOLID,
                            default_size=Rect_Size(width=100, height=60), max_size=Rect_Size(width=300, height=110))
}

node_type_usages = {
    'class': {'class', 'imported class'},
    'state machine': {'state'},
    'collaboration': {'class overview', 'extneral entity'},
    'domain': {'domain'}
}
