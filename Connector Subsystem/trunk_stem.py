"""
trunk_stem.py
"""

from anchored_tree_stem import AnchoredTreeStem


class TrunkStem(AnchoredTreeStem):
    """
    Every tree connector pattern connects a single Node playing the role of a trunk with
    one or more other Nodes playing a leaf role. The Trunk Stem is an Anchored Tree Stem attached
    to the trunk Node.
    """
    def __init__(self, connector, stem_type, semantic, node, face, anchor_position):
        AnchoredTreeStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position)

        # Here we will put the logic to find the stem decoration and have it drawn

