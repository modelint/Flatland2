"""
diagram_node_types.py
"""
from flatland_types import Node_Type_Attrs, Alignment, Padding, Rect_Size

""" 'corner_rounding compartments border_width border_style max size' """

node_types = {
    'class': Node_Type_Attrs(corner_rounding=0, compartments=3, border_width=1, border_style='solid',
                             max_size=Rect_Size(height=148, width=148)),
    'imported class': Node_Type_Attrs(corner_rounding=0, compartments=2, border_width=1, border_style='dashed',
                                      max_size=Rect_Size(height=148, width=148)),
    'state': Node_Type_Attrs(corner_rounding=4, compartments=1, border_width=1, border_style='solid',
                             max_size=Rect_Size(height=148, width=250)),
    'overview_class': Node_Type_Attrs(corner_rounding=0, compartments=1, border_width=1, border_style='solid',
                                      max_size=Rect_Size(height=40, width=250)),
    'domain': Node_Type_Attrs(corner_rounding=0, compartments=1, border_width=1, border_style='solid',
                              max_size=Rect_Size(height=40, width=80)),
    'ee': Node_Type_Attrs(corner_rounding=0, compartments=1, border_width=1, border_style='solid',
                          max_size=Rect_Size(height=40, width=250))
}

diagram_types = {
    'class': {'class', 'imported_class'},
    'state': {'state'},
    'collab': {'overview_class', 'ee'},
    'domain': {'domain'}
}
