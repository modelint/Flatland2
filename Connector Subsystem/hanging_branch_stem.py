"""
hanging_branch_stem.py
"""

from anchored_branch_stem import AnchoredBranchStem


class HangingBranchStem(AnchoredBranchStem):
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position, branch_axis):
        AnchoredBranchStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)
