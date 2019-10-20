"""
flatland_types.py
"""

from collections import namedtuple
from enum import Enum


class LineWidth(Enum):
    THIN = 1
    NORMAL = 2
    THICK = 3


Line = namedtuple('Line', 'width from_here to_there')
Rectangle = namedtuple('Rectangle', 'lower_left, size')
Position = namedtuple('Position', 'x y')
Rect_Size = namedtuple('Rect_Size', 'height width')
Alignment = namedtuple('Alignment', 'vertical horizontal')
Padding = namedtuple('Padding', 'top bottom left right')
Node_Type_Attrs = namedtuple('Node_Type_Attrs', 'corner_rounding compartments border_width border_style max_size')
