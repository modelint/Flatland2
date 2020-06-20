"""
names.py

For classes in all subsystems that require descriptive names, here are enums of the available
names.
"""

from enum import Enum


class DiagramTypeName(Enum):
    """
    These are the names of the supported diagram types
    """
    CD = 'Class diagram',
    SMD = 'State machine diagram',
    CCD = 'Class collaboration diagram',
    DD = 'Domain diagram'


user_diagram_names = {
    'class': DiagramTypeName.CD,
    'state': DiagramTypeName.SMD,
    'cc': DiagramTypeName.CCD,
    'domain': DiagramTypeName.DD
}


class NodeTypeName(Enum):
    """
    These are the names of all supported node types
    """
    M_class = "Class",  # A normal class
    I_class = "Imported class",  # Class from a different subsystem
    State = "State",
    O_class = "Overview class",  # For collaboration diagram
    Domain = "Domain",  # For domain chart
    EE = "External entity"  # For collaboration diagram


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
