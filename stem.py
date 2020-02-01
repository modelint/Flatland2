"""
stem.py
"""


class Stem:
    """

    """

    def __init__(self,
                 connector, stem_type, node, node_face, lateral_position, connector_semantic):
        self.Connector = connector
        self.Stem_type = stem_type
        self.Node = node
        self.Node_face = node_face
        self.Lateral_position = lateral_position
        # For connector semantic, look up the Stem End
        self.Root_end
        self.Vine_end
        pass
