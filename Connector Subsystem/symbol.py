"""
symbol.py

Modeled class: Symbol

Here you define all text and graphical symbols drawn on the ends
of Connectors (Stems) in each supported notation.
"""
from flatland_types import Stroke, StrokeStyle, StrokeWidth
from collections import namedtuple
from enum import Enum


class Symbol(Enum):
    """
    Symbols where names are unique and values are either text to be displayed
    or the total length of the symbol. For text, use graphic library
    function to compute text dimensions. Note that the enum values are
    NOT unique values.
    """
    # Text symbols
    UML_1c = "0..1",
    UML_1 = "1",
    UML_M = "1..*",
    UML_Mc = "0..*",
    UML_assoc_M = "{M}",
    SM_cond = "c",
    SM_isa = "is a",
    XUML_Gtag = "{ disjoint, complete }",
    # Simple shape symbols
    Solid_arrow = 9,  # height of arrow
    Hollow_arrow = 9,
    Open_arrow = 9,
    Gen_arrow = 12,
    Solid_UML_dot = 8.5,  # UML initial state circle diameter
    Open_UML_circle = 14.5,  # UML final state circle diameter
    # Compound shape symbols
    Double_solid_arrow = 18,  # height of arrow * 2
    Double_hollow_arrow = 18,
    Double_open_arrow = 18,
    Bounded_UML_dot = 8.5  # UML solid circle inside larger circle in final state


class ArrowFill(Enum):
    """
    Arrow fill styles
    """
    Hollow = 0,
    Solid = 1,
    Open = 2


Arrowhead_Shape = namedtuple('Arrowhead_Shape', 'base height stroke fill')
Circle_Shape = namedtuple('Circle_Shape', 'radius solid stroke')

simple_shape_symbols = {
    Symbol.Solid_arrow: Arrowhead_Shape(
        base=7, height=9, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID), fill=ArrowFill.Solid
    ),
    Symbol.Hollow_arrow: Arrowhead_Shape(
        base=7, height=9, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID), fill=ArrowFill.Hollow
    ),
    Symbol.Open_arrow: Arrowhead_Shape(
        base=7, height=9, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID), fill=ArrowFill.Open
    ),
    Symbol.Gen_arrow: Arrowhead_Shape(
        base=15, height=12, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID), fill=ArrowFill.Hollow
    ),
    Symbol.Solid_UML_dot: Circle_Shape(
        radius=8.5, solid=True, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID)
    ),
    Symbol.Open_UML_circle: Circle_Shape(
        radius=14.5, solid=False, stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.SOLID)
    )
}


class StackDir(Enum):
    """
    Relative placment of two Simple Shape Symbols
    """
    Below = 0,  # Vertically stacked
    Next_to = 1  # Side by side


Stack_Method = namedtuple("Stack_Method", "shape1 arrange shape2")

compound_shape_symbols = {
    # Listed in draw order where arrows are drawn side by side along the x or y axis
    # with circles stacked on the z-axis
    Symbol.Double_solid_arrow: [
        Stack_Method(shape1=Symbol.Solid_arrow, arrange=StackDir.Next_to, shape2=Symbol.Solid_arrow)
    ],
    Symbol.Double_hollow_arrow: [
        Stack_Method(shape1=Symbol.Hollow_arrow, arrange=StackDir.Next_to, shape2=Symbol.Hollow_arrow)
    ],
    Symbol.Double_open_arrow: [
        Stack_Method(shape1=Symbol.Open_arrow, arrange=StackDir.Next_to, shape2=Symbol.Open_arrow)
    ],
    Symbol.Bounded_UML_dot: [
        Stack_Method(shape1=Symbol.Open_UML_circle, arrange=StackDir.Below, shape2=Symbol.Bounded_UML_dot)
    ]
}



