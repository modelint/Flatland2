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


user_notation_names = {
    'SM' : Notation.SM,
    'Starr' : Notation.Starr,
    'xUML' : Notation.xUML
}


class StemSemantic(Enum):
    """
    These are the notation independent semantics. Each notation may or may not
    specify a decoration for corresponding stem ends.
    """
    # For state machines
    From_state = 'From state',  # Typically no decoration
    Target_state = 'Target state',
    Final_pstate = 'Final pseudo state',
    Initial_pstate = 'Initial pseudo state',

    # For class models
    Mult_1 = '1 unconditional multiplicity',
    Mult_M = 'Many unconditional multiplicity',
    Mult_Mc = 'Many conditional multiplicity',
    Mult_1c = '1 conditional multiplicity',
    Super_class = 'Superclass',
    Sub_class = 'Subclass'  # Typically no decoration







