"""
diagram_node_types.py
"""
from flatland_types import Node_Type_Attrs, Rect_Size, Stroke, StrokeWidth, StrokeStyle

node_types = {
    'class': Node_Type_Attrs(corner_rounding=0, compartments=3,
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=80, width=110),
                             max_size=Rect_Size(height=180, width=144)),
    'imported_class': Node_Type_Attrs(corner_rounding=0, compartments=2,
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED),
                                      default_size=Rect_Size(height=80, width=110),
                                      max_size=Rect_Size(height=180, width=144)),
    'state': Node_Type_Attrs(corner_rounding=4, compartments=1,
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=50, width=110),
                             max_size=Rect_Size(height=108, width=300)),
    'overview_class': Node_Type_Attrs(corner_rounding=0, compartments=1,
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                      default_size=Rect_Size(height=25, width=100),
                                      max_size=Rect_Size(height=60, width=300)),
    'domain': Node_Type_Attrs(corner_rounding=0, compartments=1,
                              line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                              default_size=Rect_Size(height=60, width=100),
                              max_size=Rect_Size(height=110, width=300)),
    'external entity': Node_Type_Attrs(corner_rounding=0, compartments=1,
                                       line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                       default_size=Rect_Size(height=25, width=100),
                                       max_size=Rect_Size(height=60, width=300))
}

diagram_types = {
    'class': {'class', 'imported_class'},
    'state': {'state'},
    'collab': {'overview_class', 'ee'},
    'domain': {'domain'}
}
