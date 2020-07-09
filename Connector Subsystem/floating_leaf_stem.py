"""
floating_leaf_stem.py
"""
from floating_stem import FloatingStem


class FloatingLeafStem(FloatingStem):
    def __init__(self, connector, stem_type, semantic, node, face, grafted_branch):
        FloatingStem.__init__(connector, stem_type, semantic, node, face, )
        self.Grafted_branch = grafted_branch
