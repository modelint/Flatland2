"""
flatland_types.py
"""

from collections import namedtuple
from enum import Enum


class StrokeWidth(Enum):
    THIN = 1
    NORMAL = 2
    THICK = 3


class StrokeStyle(Enum):
    SOLID = 1
    DASHED = 2


class VertAlign(Enum):
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'


class HorizAlign(Enum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


Line = namedtuple('Line', 'stroke from_here to_there')
Rectangle = namedtuple('Rectangle', 'stroke lower_left, size')
Position = namedtuple('Position', 'x y')
Rect_Size = namedtuple('Rect_Size', 'height width')
Alignment = namedtuple('Alignment', 'vertical horizontal')
Padding = namedtuple('Padding', 'top bottom left right')
Node_Type_Attrs = namedtuple('Node_Type_Attrs', 'corner_rounding compartments border_width border_style max_size')
