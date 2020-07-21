"""
connector_type_instances.py
"""

population = [
    {'Name': 'binary association', 'Diagram type': 'class', 'Geometry': 'binary',
     'About': 'Connects an anchor point on one node to an anchor point on the same or another node'},
    {'Name': 'associative relationship', 'Diagram type': 'class', 'Geometry': 'tertiary',
     'About': 'Same properties as a binary association with an added association class'},
    {'Name': 'generalization', 'Diagram type': 'class', 'Geometry': 'tree',
     'About': 'A superset class compeletely split into disjoint subset classes'},
    {'Name': 'initial transition', 'Diagram type': 'state machine', 'Geometry': 'unary',
     'About': 'Designates an initial state'},
    {'Name': 'deletion transition', 'Diagram type': 'state machine', 'Geometry': 'unary',
     'About': 'Designates implicit instance deletion after a state executes its activity'},
    {'Name': 'transition', 'Diagram type': 'state machine', 'Geometry': 'binary',
     'About': 'Defines a path from one state to another'},
    {'Name': 'bridge', 'Diagram type': 'domain', 'Geometry': 'binary',
     'About': 'Defines a dependency on requirements from one domain to another'},
    {'Name': 'collaboration', 'Diagram type': 'collaboration', 'Geometry': 'binary',
     'About': 'Represents a path of communication between two nodes on a collaboration diagram'}
]