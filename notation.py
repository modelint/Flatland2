"""
notation.py

Where you specify your diagram type and notation

"""
from enum import Enum


class Notation(Enum):
    """
    These are the supported diagram notations
    """
    SM = 'Shlaer-Mellor',  # Easiest whiteboard notation
    Starr = 'Starr',  # Similar to SM, but least diagram clutter
    xUML = 'Executable UML'  # For those who need the standard, subset of UML with some annotations


class ConnectorSemantic(Enum):
    """
    Supported semantics for a decorated stem end
    No entry for plain, non-decorated stem ends such as subclass/specialization
    """
    Target_state = 'Target state',
    Final_state = 'Final pseudo state',
    Initial_state = 'Initial pseudo state',
    Mult_Mc = 'Many conditional multiplicity',
    Mult_1 = '1 unconditional multiplicity',
    Mult_M = 'Many unconditional multiplicity',
    Mult_1c = '1 conditional multiplicity',
    Gen = 'Generalization',
    Dependency = 'Dependency'








