"""
sheet.py – Standard and non-standard sheet sizes

"""
from geometry_types import Rect_Size


# All sheet and canvas related constants are kept together here for easy review and editing
us_sheet_sizes = {
    'letter': Rect_Size(width=8.5, height=11),  # 612 x 792 pts
    'tabloid': Rect_Size(height=11, width=17),
    'C': Rect_Size(height=17, width=22),
    'D': Rect_Size(height=22, width=34),
    'E': Rect_Size(height=34, width=44)
}

default_us_sheet = 'tabloid'

euro_sheet_A_sizes = {
    'A4': Rect_Size(width=210, height=297),
    'A3': Rect_Size(width=297, height=420),
    'A2': Rect_Size(width=420, height=594),
    'A1': Rect_Size(width=594, height=841)
}

default_euro_sheet = 'A3'
