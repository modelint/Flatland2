"""
stem_type.py

Stem Type and Stem Type Usage classes
"""

from names import StemTypeName
from diagram_type import DiagramTypeName


stem_types = {
    DiagramTypeName.CD: {
        StemTypeName.class_mult,
        StemTypeName.assoc_class_mult,
        StemTypeName.gen_superclass,
        StemTypeName.gen_subclass,
    },
    DiagramTypeName.SMD: {
        StemTypeName.from_state,
        StemTypeName.from_del_state,
        StemTypeName.to_init_state,
        StemTypeName.to_state
    }
}


