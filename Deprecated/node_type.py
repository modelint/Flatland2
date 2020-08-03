"""
node_type.py

Defines the types of Nodes that may appear on Diagrams

node_types : dict
    Node Type information specifies data that is the same for all Nodes of a given type
    All Class nodes, for example, have three compartments each with a particular typeface.
    This information would be the same on each class node on any class diagram.

    We use an OrderedDict for compartments to implement the R1 relationship on the modeled
    Compartment Type Class
"""

from names import NodeTypeName
from collections import namedtuple, OrderedDict
from draw_types import Stroke, Text_Style, StrokeWidth, StrokeStyle, TypeFace, FontWeight, FontSlant, Color
from geometry_types import Alignment, VertAlign, HorizAlign, Padding, Rect_Size

Node_Type_Attrs = namedtuple('Node_Type_Attrs',
                             'corner_rounding compartments line_style default_size max_size')

Compartment_Type_Attrs = namedtuple('Compartment_Type_Attrs', 'alignment padding text_style')


node_types = {
    NodeTypeName.M_class: Node_Type_Attrs(corner_rounding=0,
                                          compartments=OrderedDict({
                                              'class name': Compartment_Type_Attrs(
                                                  alignment=Alignment(vertical=VertAlign.CENTER,
                                                                      horizontal=HorizAlign.CENTER),
                                                  padding=Padding(top=5, bottom=10, left=10, right=5),
                                                  text_style=Text_Style(typeface=TypeFace.PALATINO,
                                                                        size=11, slant=FontSlant.NORMAL,
                                                                        weight=FontWeight.NORMAL)),
                                              'attributes': Compartment_Type_Attrs(
                                                  alignment=Alignment(vertical=VertAlign.CENTER,
                                                                      horizontal=HorizAlign.CENTER),
                                                  padding=Padding(top=4, bottom=10, left=10, right=4),
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
                                          line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                          default_size=Rect_Size(height=80, width=110),
                                          max_size=Rect_Size(height=180, width=144)),
    NodeTypeName.I_class: Node_Type_Attrs(corner_rounding=0,
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
                                          line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED),
                                          default_size=Rect_Size(height=80, width=110),
                                          max_size=Rect_Size(height=180, width=144)),
    NodeTypeName.State: Node_Type_Attrs(corner_rounding=4,
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
                                        line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                        default_size=Rect_Size(height=50, width=110),
                                        max_size=Rect_Size(height=108, width=300)),
    NodeTypeName.O_class: Node_Type_Attrs(corner_rounding=0,
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
                                          line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                          default_size=Rect_Size(height=25, width=100),
                                          max_size=Rect_Size(height=60, width=300)),
    NodeTypeName.Domain: Node_Type_Attrs(corner_rounding=0,
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
                                         line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                         default_size=Rect_Size(height=60, width=100),
                                         max_size=Rect_Size(height=110, width=300)),
    NodeTypeName.EE: Node_Type_Attrs(corner_rounding=0,
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
                                     line_style=Stroke(color=Color.BLACK, width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID),
                                     default_size=Rect_Size(height=25, width=100),
                                     max_size=Rect_Size(height=60, width=300))
}
