"""
diagram_node_types.py
"""
from flatland_types import *

node_types = {
    'class': Node_Type_Attrs(corner_rounding=0,
                             compartments=[
                                 Compartment_Type_Attrs(name='class name',
                                                        alignment=Alignment(vertical=VertAlign.CENTER,
                                                                            horizontal=HorizAlign.CENTER),
                                                        padding=Padding(top=5, bottom=5, left=5, right=5),
                                                        text_style=Text_Style(typeface=TypeFace.PALATINO,
                                                                              size=11, slant=FontSlant.NORMAL,
                                                                              weight=FontWeight.NORMAL)),
                                 Compartment_Type_Attrs(name='attributes',
                                                        alignment=Alignment(vertical=VertAlign.CENTER,
                                                                            horizontal=HorizAlign.CENTER),
                                                        padding=Padding(top=4, bottom=4, left=4, right=4),
                                                        text_style=Text_Style(font=TypeFace.PALATINO,
                                                                              size=9, slant=FontSlant.NORMAL,
                                                                              weight=FontWeight.NORMAL)),
                                 Compartment_Type_Attrs(name='methods',
                                                        alignment=Alignment(vertical=VertAlign.CENTER,
                                                                            horizontal=HorizAlign.CENTER),
                                                        padding=Padding(top=4, bottom=4, left=4, right=4),
                                                        text_style=Text_Style(font=TypeFace.PALATINO,
                                                                              size=9, slant=FontSlant.NORMAL,
                                                                              weight=FontWeight.NORMAL))

                             ],
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=80, width=110),
                             max_size=Rect_Size(height=180, width=144)),
    'imported_class': Node_Type_Attrs(corner_rounding=0,
                                      compartments=[
                                          Compartment_Type_Attrs(name='class name',
                                                                 alignment=Alignment(vertical=VertAlign.CENTER,
                                                                                     horizontal=HorizAlign.CENTER),
                                                                 padding=Padding(top=5, bottom=5, left=5, right=5),
                                                                 text_style=Text_Style(
                                                                     typeface=TypeFace.PALATINO,
                                                                     size=11, slant=FontSlant.NORMAL,
                                                                     weight=FontWeight.NORMAL)),
                                          Compartment_Type_Attrs(name='attributes',
                                                                 alignment=Alignment(vertical=VertAlign.CENTER,
                                                                                     horizontal=HorizAlign.CENTER),
                                                                 padding=Padding(top=4, bottom=4, left=4, right=4),
                                                                 text_style=Text_Style(
                                                                     typeface=TypeFace.PALATINO,
                                                                     size=9, slant=FontSlant.NORMAL,
                                                                     weight=FontWeight.NORMAL))

                                      ],
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED),
                                      default_size=Rect_Size(height=80, width=110),
                                      max_size=Rect_Size(height=180, width=144)),
    'state': Node_Type_Attrs(corner_rounding=4,
                             compartments=[
                                 Compartment_Type_Attrs(name='state name',
                                                        alignment=Alignment(vertical=VertAlign.CENTER,
                                                                            horizontal=HorizAlign.CENTER),
                                                        padding=Padding(top=5, bottom=5, left=5, right=5),
                                                        text_style=Text_Style(
                                                            typeface=TypeFace.PALATINO,
                                                            size=11, slant=FontSlant.NORMAL,
                                                            weight=FontWeight.NORMAL)),
                                 Compartment_Type_Attrs(name='activity',
                                                        alignment=Alignment(vertical=VertAlign.CENTER,
                                                                            horizontal=HorizAlign.CENTER),
                                                        padding=Padding(top=4, bottom=4, left=4, right=4),
                                                        text_style=Text_Style(
                                                            typeface=TypeFace.PALATINO,
                                                            size=9, slant=FontSlant.NORMAL,
                                                            weight=FontWeight.NORMAL))

                             ],
                             line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                             default_size=Rect_Size(height=50, width=110),
                             max_size=Rect_Size(height=108, width=300)),
    'overview_class': Node_Type_Attrs(corner_rounding=0,
                                      compartments=[
                                          Compartment_Type_Attrs(name='class name',
                                                                 alignment=Alignment(vertical=VertAlign.CENTER,
                                                                                     horizontal=HorizAlign.CENTER),
                                                                 padding=Padding(top=5, bottom=5, left=5, right=5),
                                                                 text_style=Text_Style(
                                                                     typeface=TypeFace.PALATINO,
                                                                     size=11, slant=FontSlant.NORMAL,
                                                                     weight=FontWeight.NORMAL))
                                      ],
                                      line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                      default_size=Rect_Size(height=25, width=100),
                                      max_size=Rect_Size(height=60, width=300)),
    'domain': Node_Type_Attrs(corner_rounding=0,
                              compartments=[
                                  Compartment_Type_Attrs(name='domain name',
                                                         alignment=Alignment(vertical=VertAlign.CENTER,
                                                                             horizontal=HorizAlign.CENTER),
                                                         padding=Padding(top=5, bottom=5, left=5, right=5),
                                                         text_style=Text_Style(
                                                             typeface=TypeFace.PALATINO,
                                                             size=11, slant=FontSlant.NORMAL,
                                                             weight=FontWeight.NORMAL))
                              ],
                              line_style=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                              default_size=Rect_Size(height=60, width=100),
                              max_size=Rect_Size(height=110, width=300)),
    'external entity': Node_Type_Attrs(corner_rounding=0,
                                       compartments=[
                                           Compartment_Type_Attrs(name='ee name',
                                                                  alignment=Alignment(vertical=VertAlign.CENTER,
                                                                                      horizontal=HorizAlign.CENTER),
                                                                  padding=Padding(top=5, bottom=5, left=5, right=5),
                                                                  text_style=Text_Style(
                                                                      typeface=TypeFace.PALATINO,
                                                                      size=11, slant=FontSlant.NORMAL,
                                                                      weight=FontWeight.NORMAL))
                                       ],
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
