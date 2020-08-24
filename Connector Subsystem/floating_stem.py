"""
floating_stem.py
"""

from stem import Stem


class FloatingStem(Stem):
    def __init__(self, connector, stem_type, semantic, node, face, root_position ):
        Stem.__init__(self, connector, stem_type, semantic, node, face, root_position )