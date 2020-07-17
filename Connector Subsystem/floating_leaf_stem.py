"""
floating_leaf_stem.py
"""
from floating_stem import FloatingStem


class FloatingLeafStem(FloatingStem):
    def __init__(self, connector, stem_type, semantic, node, face, grafted_branch, root_position, vine_position):
        FloatingStem.__init__(self, connector, stem_type, semantic, node, face, root_position, vine_position)
        self.Grafted_branch = grafted_branch
