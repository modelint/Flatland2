""" layout_specification.py – These are the default values used for layout"""

from flatland_types import Padding, Position, Alignment, VertAlign, HorizAlign

default_margin = Padding(top=10, bottom=10, left=10, right=10)
default_diagram_origin = Position(x=0, y=0)  # Relative to the Canvas margin
default_cell_padding = Padding(top=5, bottom=5, left=5, right=5)
default_cell_alignment = Alignment(vertical=VertAlign.CENTER, horizontal=HorizAlign.CENTER)
default_stem_length = 10