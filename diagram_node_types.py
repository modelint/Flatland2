"""
diagram_node_types.py

Covers the Node Type and Diagram Type classes in the Flatland Class Diagram.

Attributes
---
node_types : dict
    Node Type information specifies data that is the same for all Nodes of a given type
    All Class nodes, for example, have three compartments each with a particular typeface.
    This information would be the same on each class node on any class diagram.

    We use an OrderedDict for compartments to implement the R1 relationship on the modeled
    Compartment Type Class

diagram_types : dict
    Here we specify what kinds of nodes may appear on a given type of diagram.  You cannot, put a state
    node on a class diagram, for example.

"""
from flatland_types import *
from collections import OrderedDict

node_types = {
    'class': Node_Type_Attrs(corner_rounding=0,
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
    'class': {
        'nodes': {'class', 'imported class'},
        'connectors': {'binary association', 'ternary association', 'generalization'},
        'notations' : {'Shlaer-Mellor', 'xUML', 'Starr'}
    },
    'state': {
        'nodes': {'state'},
        'connectors': {'itransition', 'deletion state', 'initial state'},
        'notations' : {'xUML'}
    },
    'collab': {
        'nodes': {'overview class', 'ee'},
        'connectors': {'communication'},
        'notations': {'xUML'}
    },
    'domain': {
        'nodes': {'domain'},
        'connectors': {'bridge'},
        'notations': {'xUML', 'Shlaer-Mellor', 'Starr'}
    }
}

