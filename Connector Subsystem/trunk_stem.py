"""
trunk_stem.py
"""

from anchored_stem import AnchoredStem


class TrunkStem(AnchoredStem):
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position, branch_axis):
        AnchoredStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position)
