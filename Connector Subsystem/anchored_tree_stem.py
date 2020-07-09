"""
anchored_tree_stem.py
"""

from anchored_stem import AnchoredStem


class AnchoredTreeStem(AnchoredStem):
    """
    Any Stem within a Tree Connector attached to a user specified anchor position is an Anchored Tree Stem.
    """
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position):
        AnchoredStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position)

        # Nothing special going on here yet

