"""
stem_type.py

Stem Type and Stem Type Usage classes
"""

from enum import Enum
from diagram_type import DiagramTypeName


class StemTypeName(Enum):
    """
    These are the names of each stem type
    """
    class_mult = "Class multiplicity",  # Rooted on a class
    assoc_class_mult = "Association class multiplicity",  # Rooted in assoc class
    gen_superclass = "Generalization superclass",  # Rooted in a superclass
    gen_subclass = "Generalization subclass",  # Rooted in a subclass
    from_state = "From state",  # Rooted in a source state
    to_state = "To state",  # Rooted in a destination state
    to_init_state = "To initial state",  # Rooted in an intial state
    from_del_state = "From deletion state"  # Rooted in a deletion state


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


