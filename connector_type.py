"""
connector_type.py

Connector and stem type specification
"""
from enum import Enum
from collections import namedtuple
from diagram_node_types import DiagramTypeName
from flatland_types import Geometry, Stroke, StrokeWidth, StrokeStyle
from notation import Notation


class ConnectorTypeName(Enum):
    """
    These are the names of each supported connector type
    """
    binary_assoc = "binary assocation",
    assoc_class = "association class",
    gen = "generalization",
    init_trans = "initial transition",
    del_trans = "deletion transition",
    trans = "transition",
    bridge = "bridge",
    comm = "communication"


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


connector_types = {
    DiagramTypeName.CD: {
        ConnectorTypeName.binary_assoc: Geometry.B,
        ConnectorTypeName.assoc_class: Geometry.T,
        ConnectorTypeName.gen: Geometry.H
    },
    DiagramTypeName.SMD: {
        ConnectorTypeName.init_trans: Geometry.U,
        ConnectorTypeName.del_trans: Geometry.U,
        ConnectorTypeName.trans: Geometry.B
    }
}

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

stem_type_usages = {
    (ConnectorTypeName.binary_assoc, DiagramTypeName.CD): {StemTypeName.class_mult},
    (ConnectorTypeName.assoc_class, DiagramTypeName.CD): {StemTypeName.class_mult, StemTypeName.assoc_class_mult},
    (ConnectorTypeName.gen, DiagramTypeName.CD): {StemTypeName.gen_superclass, StemTypeName.gen_subclass},
    (ConnectorTypeName.init_trans, DiagramTypeName.SMD): {StemTypeName.to_init_state},
    (ConnectorTypeName.del_trans, DiagramTypeName.SMD): {StemTypeName.from_state},
    (ConnectorTypeName.trans, DiagramTypeName.SMD): {StemTypeName.from_state, StemTypeName.to_state}
}


StemTypeStyle = namedtuple('Stem_Type_Style', 'stem_type dtype notation stroke')

stem_type_styles = {
    # Only one case where a solid line is not drawn and that is the xUML association class dependency
    # which is dashed
    StemTypeStyle(stem_type=StemTypeName.assoc_class_mult, dtype=DiagramTypeName.CD, notation=Notation.xUML,
                  stroke=Stroke(width=StrokeWidth.NORMAL, pattern=StrokeStyle.DASHED))
}