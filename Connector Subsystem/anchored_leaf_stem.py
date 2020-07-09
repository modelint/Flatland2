"""
anchored_leaf_stem.py
"""

from anchored_tree_stem import AnchoredTreeStem


class AnchoredLeafStem(AnchoredTreeStem):
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position):
        AnchoredTreeStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)
