"""
stem_type_instances.py
"""
population = [
    # Class diagram
    {'Name': 'class mult', 'Diagram type': 'class', 'Connector type': 'binary association',
     'About': 'How many instances may be associated', 'Length': 24},
    {'Name': 'associative mult', 'Diagram type': 'class', 'Connector type': 'binary association',
     'About': 'How many association class instances per pair of associated instances', 'Length': 24},
    {'Name': 'superclass', 'Diagram type': 'class', 'Connector type': 'generalization',
     'About': 'The superset of all subclass instances', 'Length': 24},
    {'Name': 'subclass', 'Diagram type': 'class', 'Connector type': 'generalization',
     'About': 'A disjoint subset of the superclass set of instances', 'Length': 10},

    # State machine diagram
    {'Name': 'from state', 'Diagram type': 'state machine', 'Connector type': 'transition',
     'About': 'Points to the source state in a transition', 'Length': 10},
    {'Name': 'to state', 'Diagram type': 'state machine', 'Connector type': 'transition',
     'About': 'Points to the destination state in a transition', 'Length': 15},
    {'Name': 'to initial state', 'Diagram type': 'state machine', 'Connector type': 'initial transition',
     'About': 'Points to a designated state as an initial state', 'Length': 60},
    {'Name': 'from deletion state', 'Diagram type': 'state machine', 'Connector type': 'deletion transition',
     'About': 'Points away from a final state to indicate deletion', 'Length': 50},

    # Domain diagram
    {'Name': 'to service', 'Diagram type': 'domain', 'Connector type': 'bridge',
     'About': 'Points toward a domain that fullfills the requirements of a client domain', 'Length': 15},

    # Collaboration diagram
    {'Name': 'on collaborator', 'Diagram type': 'collaboration', 'Connector type': 'collaboration',
     'About': 'Attaches to a communicating entity', 'Length': 10}
]