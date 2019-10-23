""" sheet.py – Standard and non-standard sheet sizes """

from flatland_types import Padding, Alignment, Rect_Size, Position, Rectangle, StrokeWidth

# All sheet and canvas related constants are kept together here for easy review and editing
us_sheet_sizes = {
    'letter': (8.5, 11),
    'tabloid': (11, 17),
    'C': (17, 22),
    'D': (22, 34),
    'E': (34, 44)
}

euro_sheet_A_sizes = {
    'A4': (210, 297),
    'A3': (297, 420),
    'A2': (420, 594),
    'A1': (594, 841)
}
