"""
stem_type_instances.py
"""
population = [
    {'Name': 'class mult', 'Diagram type': 'class', 'Connector type': 'binary association',
     'About': 'How many instances may be associated'},
    {'Name': 'associative mult', 'Diagram type': 'class', 'Connector type': 'binary association',
     'About': 'How many association class instances per pair of associated instances'},
    {'Name': 'superclass', 'Diagram type': 'class', 'Connector type': 'generalization',
     'About': 'The superset of all subclass instances'},
    {'Name': 'subclass', 'Diagram type': 'class', 'Connector type': 'generalization',
     'About': 'A disjoint subset of the superclass set of instances'},
    {'Name': 'from state', 'Diagram type': 'state machine', 'Connector type': 'transition',
     'About': 'Points to the source state in a transition'},
    {'Name': 'to state', 'Diagram type': 'state machine', 'Connector type': 'transition',
     'About': 'Points to the destination state in a transition'},
    {'Name': 'to initial state', 'Diagram type': 'state machine', 'Connector type': 'initial transition',
     'About': 'Points to a designated state as an initial state'},
    {'Name': 'from deletion state', 'Diagram type': 'state machine', 'Connector type': 'deletion transition',
     'About': 'Points away from a final state to indicate deletion'},
    {'Name': 'to service', 'Diagram type': 'domain', 'Connector type': 'bridge',
     'About': 'Points toward a domain that fullfills the requirements of a client domain'},
    {'Name': 'on collaborator', 'Diagram type': 'collaboration', 'Connector type': 'collaboration',
     'About': 'Attaches to a communicating entity'}
]