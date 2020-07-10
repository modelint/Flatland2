"""
sheet.py – Standard and non-standard sheet sizes

"""

# All sheet and canvas related constants are kept together here for easy review and editing
us_sheet_sizes = {
    'letter': (8.5, 11),  # 612 x 792 pts
    'tabloid': (11, 17),
    'C': (17, 22),
    'D': (22, 34),
    'E': (34, 44)
}

default_us_sheet = 'tabloid'

euro_sheet_A_sizes = {
    'A4': (210, 297),
    'A3': (297, 420),
    'A2': (420, 594),
    'A1': (594, 841)
}

default_euro_sheet = 'A3'
