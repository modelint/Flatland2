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
    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'


class HorizAlign(Enum):
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


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
