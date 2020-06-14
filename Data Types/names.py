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
