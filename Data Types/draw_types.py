"""
draw_types.py

Flatland drawing data types
"""
from enum import Enum
from collections import namedtuple

Stroke = namedtuple('Stroke', 'width pattern')
Line = namedtuple('Line', 'line_style from_here to_there')
Text_Style = namedtuple('Text_Style', 'typeface size slant weight')
Text_Line = namedtuple('Text_Line', 'lower_left style content')


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
