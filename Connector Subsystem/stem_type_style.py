"""
stem_type_style.py

Stem Type Style class
"""

from collections import namedtuple
from stem_type import StemTypeName
from draw_types import Stroke, StrokeWidth, StrokeStyle
from notation import Notation
from diagram_type import DiagramTypeName


StemTypeStyle = namedtuple('Stem_Type_Style', 'stem_type dtype notation stroke')

stem_type_styles = {
    # Only one case where a solid line is not drawn and that is the xUML association class dependency
    # which is dashed
    StemTypeStyle(stem_type=StemTypeName.assoc_class_mult, dtype=DiagramTypeName.CD, notation=Notation.xUML,
                  stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED))
}
