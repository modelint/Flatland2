"""
flatland_types.py
"""

from collections import namedtuple

Position = namedtuple('Position', 'x y')
Rect_Size = namedtuple('Rect_Size', 'height width')
Alignment = namedtuple('Alignment', 'vertical horizontal')
Padding = namedtuple('Padding', 'top bottom left right')
Node_Type_Attrs = {'Node_Type_Attrs', 'corner_rounding compartments border_width border_style max_size'}