"""
diagram_node_types.py
"""
from flatland_types import *
from collections import OrderedDict

node_types = {
    'class': Node_Type_Attrs(corner_rounding=0,
                             compartments=OrderedDict({
                                 'class name': Compartment_Type_Attrs(
                                     alignment=Alignment(vertical=VertAlign.CENTER,
                                                         horizontal=HorizAlign.CENTER),
                                     padding=Padding(top=5, bottom=5, left=5, right=5),
                                     text_style=Text_Style(typeface=TypeFace.PALATINO,
                                                           size=11, slant=FontSlant.NORMAL,
                                                           weight=FontWeight.NORMAL)),
                                 'attributes': Compartment_Type_Attrs(
                                     alignment=Alignment(vertical=VertAlign.CENTER,
                                                         horizontal=HorizAlign.CENTER),
                                     padding=Padding(top=4, bottom=4, left=4, right=4),
                                     text_style=Text_Style(typeface=TypeFace.PALATINO,
                                                           size=9, slant=FontSlant.NORMAL,
                                                           weight=FontWeight.NORMAL)),
                                 'methods': Compartment_Type_Attrs(
                                     alignment=Alignment(vertical=VertAlign.CENTER,
                                                         horizontal=HorizAlign.CENTER),
                                     padding=Padding(top=4, bottom=4, left=4, right=4),
                                     text_style=Text_Style(typeface=TypeFace.PALATINO,
                                                           size=9, slant=FontSlant.NORMAL,
                                                           weight=FontWeight.NORMAL))

                             }),
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=80, width=110),
                             max_size=Rect_Size(height=180, width=144)),
    'imported_class': Node_Type_Attrs(corner_rounding=0,
                                      compartments=OrderedDict({
                                          'class name': Compartment_Type_Attrs(
                                              alignment=Alignment(vertical=VertAlign.CENTER,
                                                                  horizontal=HorizAlign.CENTER),
                                              padding=Padding(top=5, bottom=5, left=5, right=5),
                                              text_style=Text_Style(
                                                  typeface=TypeFace.PALATINO,
                                                  size=11, slant=FontSlant.NORMAL,
                                                  weight=FontWeight.NORMAL)),
                                          'attributes': Compartment_Type_Attrs(
                                              alignment=Alignment(vertical=VertAlign.CENTER,
                                                                  horizontal=HorizAlign.CENTER),
                                              padding=Padding(top=4, bottom=4, left=4, right=4),
                                              text_style=Text_Style(
                                                  typeface=TypeFace.PALATINO,
                                                  size=9, slant=FontSlant.NORMAL,
                                                  weight=FontWeight.NORMAL))

                                      }),
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED),
                                      default_size=Rect_Size(height=80, width=110),
                                      max_size=Rect_Size(height=180, width=144)),
    'state': Node_Type_Attrs(corner_rounding=4,
                             compartments=OrderedDict({
                                 'state name': Compartment_Type_Attrs(
                                     alignment=Alignment(vertical=VertAlign.CENTER,
                                                         horizontal=HorizAlign.CENTER),
                                     padding=Padding(top=5, bottom=5, left=5, right=5),
                                     text_style=Text_Style(
                                         typeface=TypeFace.PALATINO,
                                         size=11, slant=FontSlant.NORMAL,
                                         weight=FontWeight.NORMAL)),
                                 'activity': Compartment_Type_Attrs(
                                     alignment=Alignment(vertical=VertAlign.CENTER,
                                                         horizontal=HorizAlign.CENTER),
                                     padding=Padding(top=4, bottom=4, left=4, right=4),
                                     text_style=Text_Style(
                                         typeface=TypeFace.PALATINO,
                                         size=9, slant=FontSlant.NORMAL,
                                         weight=FontWeight.NORMAL))
                             }),
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=50, width=110),
                             max_size=Rect_Size(height=108, width=300)),
    'overview_class': Node_Type_Attrs(corner_rounding=0,
                                      compartments=OrderedDict({
                                          'class name': Compartment_Type_Attrs(
                                              alignment=Alignment(vertical=VertAlign.CENTER,
                                                                  horizontal=HorizAlign.CENTER),
                                              padding=Padding(top=5, bottom=5, left=5, right=5),
                                              text_style=Text_Style(
                                                  typeface=TypeFace.PALATINO,
                                                  size=11, slant=FontSlant.NORMAL,
                                                  weight=FontWeight.NORMAL))
                                      }),
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                      default_size=Rect_Size(height=25, width=100),
                                      max_size=Rect_Size(height=60, width=300)),
    'domain': Node_Type_Attrs(corner_rounding=0,
                              compartments=OrderedDict({
                                  'domain name': Compartment_Type_Attrs(
                                      alignment=Alignment(vertical=VertAlign.CENTER,
                                                          horizontal=HorizAlign.CENTER),
                                      padding=Padding(top=5, bottom=5, left=5, right=5),
                                      text_style=Text_Style(
                                          typeface=TypeFace.PALATINO,
                                          size=11, slant=FontSlant.NORMAL,
                                          weight=FontWeight.NORMAL))
                              }),
                              line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                              default_size=Rect_Size(height=60, width=100),
                              max_size=Rect_Size(height=110, width=300)),
    'external entity': Node_Type_Attrs(corner_rounding=0,
                                       compartments=OrderedDict({
                                           'ee name': Compartment_Type_Attrs(
                                                                             alignment=Alignment(
                                                                                 vertical=VertAlign.CENTER,
                                                                                 horizontal=HorizAlign.CENTER),
                                                                             padding=Padding(top=5, bottom=5, left=5,
                                                                                             right=5),
                                                                             text_style=Text_Style(
                                                                                 typeface=TypeFace.PALATINO,
                                                                                 size=11, slant=FontSlant.NORMAL,
                                                                                 weight=FontWeight.NORMAL))
                                       }),
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
