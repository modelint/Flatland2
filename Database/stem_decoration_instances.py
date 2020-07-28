"""
stem_decoration_instances.py
"""

population = [
    # Class diagram

    # Starr notation
    # Binary multiplicity
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'Mc mult', 'End': 'root', 'Symbol': 'double hollow arrow', 'Shape': 'Compound'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1c mult', 'End': 'root', 'Symbol': 'hollow arrow', 'Shape': 'Arrow'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1 mult', 'End': 'root', 'Symbol': 'solid arrow', 'Shape': 'Arrow'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'M mult', 'End': 'root', 'Symbol': 'double solid arrow', 'Shape': 'Compound'},

    # Associative multiplicity
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': '1 mult', 'End': 'vine', 'Symbol': 'solid arrow', 'Shape': 'Arrow'},
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'M mult', 'End': 'vine', 'Symbol': 'double solid arrow', 'Shape': 'Compound'},

    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'Starr',
     'Semantic': 'generalization', 'End': 'root', 'Symbol': 'gen arrow', 'Shape': 'Arrow'},

    # xUML notation
    # Binary multiplicity
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'Mc mult', 'End': 'root', 'Symbol': '0..*', 'Shape': 'Text'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': '1c mult', 'End': 'root', 'Symbol': '0..1', 'Shape': 'Text'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': '1 mult', 'End': 'root', 'Symbol': '1', 'Shape': 'Text'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'M mult', 'End': 'root', 'Symbol': '1..*', 'Shape': 'Text'},

    # Associative multiplicity (no notation for 1 multiplicity associative)
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'M mult', 'End': 'vine', 'Symbol': '{M}', 'Shape': 'Text'},

    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'generalization', 'End': 'root', 'Symbol': 'gen arrow', 'Shape': 'Arrow'},
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'xUML',
     'Semantic': 'generalization', 'End': 'vine', 'Symbol': '{disjoint, complete}', 'Shape': 'Text'},

    # Shlaer-Mellor notation
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'Mc mult', 'End': 'root', 'Symbol': 'double open arrow', 'Shape': 'Compound'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'Mc mult', 'End': 'vine', 'Symbol': 'c', 'Shape': 'Text'},

    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1c mult', 'End': 'root', 'Symbol': 'open arrow', 'Shape': 'Arrow'},
    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1c mult', 'End': 'vine', 'Symbol': 'c', 'Shape': 'Text'},

    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1 mult', 'End': 'root', 'Symbol': 'open arrow', 'Shape': 'Arrow'},

    {'Stem type': 'class mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'M mult', 'End': 'root', 'Symbol': 'double open arrow', 'Shape': 'Compound'},

    # Associative multiplicity
    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': '1 mult', 'End': 'vine', 'Symbol': 'open arrow', 'Shape': 'Arrow'},

    {'Stem type': 'associative mult', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'M mult', 'End': 'vine', 'Symbol': 'double open arrow', 'Shape': 'Compound'},

    # Generalization
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'generalization', 'End': 'root', 'Symbol': 'superclass cross', 'Shape': 'Cross'},
    {'Stem type': 'superclass', 'Diagram type': 'class', 'Notation': 'Shlaer-Mellor',
     'Semantic': 'generalization', 'End': 'vine', 'Symbol': 'is a', 'Shape': 'Text'},

    # State machine diagram
    {'Stem type': 'to state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'target state', 'End': 'root', 'Symbol': 'solid arrow', 'Shape': 'Arrow'},

    # Both ends of unary stem are decoreated for xUML initial transition
    {'Stem type': 'to initial state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'initial pseudo state', 'End': 'root', 'Symbol': 'solid arrow', 'Shape': 'Arrow'},
    {'Stem type': 'to initial state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'initial pseudo state', 'End': 'vine', 'Symbol': 'solid small dot', 'Shape': 'Circle'},

    {'Stem type': 'from deletion state', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'final pseudo state', 'End': 'vine', 'Symbol': 'circled dot', 'Shape': 'Compound'},

    # Domain diagram
    # Starr
    {'Stem type': 'to service', 'Diagram type': 'state machine', 'Notation': 'Starr',
     'Semantic': 'dependency', 'End': 'root', 'Symbol': 'solid arrow', 'Shape': 'Arrow'},
    # xUML
    {'Stem type': 'to service', 'Diagram type': 'state machine', 'Notation': 'xUML',
     'Semantic': 'dependency', 'End': 'root', 'Symbol': 'hollow arrow', 'Shape': 'Arrow'}
]