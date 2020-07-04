"""
anchored_branch_stem.py
"""

from anchored_stem import AnchoredStem


class AnchoredBranchStem(AnchoredStem):
    """
    An Anchored Stem used in a Hierarchy Connector. For now we don't do much with this class, but it is on the
    model and it may prove useful in the future.
    """
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position):
        AnchoredStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position)
