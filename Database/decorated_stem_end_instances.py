"""
decorated_stem_end_instances.py
"""
population = [
    # Class diagram

    # Starr notation
    # Binary multiplicity
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'Mc mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1c mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1 mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'M mult', 'End': 'root'},
    # Associative multiplicity
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1 mult', 'End': 'vine'},
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'M mult', 'End': 'vine'},
    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'generalization', 'End': 'root'},

    # xUML notation
    # Binary multiplicity
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'Mc mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': '1c mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': '1 mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'M mult', 'End': 'root'},
    # Associative multiplicity (no notation for 1 multiplicity associative)
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'M mult', 'End': 'vine'},
    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'generalization', 'End': 'root'},

    # Shlaer-Mellor notation
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'Mc mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1c mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1 mult', 'End': 'root'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'M mult', 'End': 'root'},
    # Associative multiplicity
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1 mult', 'End': 'vine'},
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'M mult', 'End': 'vine'},
    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'generalization', 'End': 'root'},

    # State machine diagram
    {'Stem type': 'to state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'target state', 'End': 'root'},

    # Both ends of unary stem are decoreated for xUML initial transition
    {'Stem type': 'to initial state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'initial pseudo state', 'End': 'root'},
    {'Stem type': 'to initial state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'initial pseudo state', 'End': 'vine'},

    {'Stem type': 'from deletion state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'final pseudo state', 'End': 'vine'},

    # Domain diagram
    # Starr
    {'Stem type': 'to service', 'Diagram type': 'state machine', 'Notation': 'Starr',
     'Semantic': 'dependency', 'End': 'root'},
    # xUML
    {'Stem type': 'to service', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'dependency', 'End': 'root'}
]