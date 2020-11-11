"""
anchored_tree_stem.py
"""

from anchored_stem import AnchoredStem
from connection_types import AnchorPosition, NodeFace
from stem_type import StemType

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector import Connector
    from node import Node


class AnchoredTreeStem(AnchoredStem):
    """
    Any Stem within a Tree Connector attached to a user specified anchor position is an Anchored Tree Stem.
    """
    def __init__(self, connector: 'Connector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, anchor_position: AnchorPosition):
        AnchoredStem.__init__(self, connector, stem_type, semantic, node, face, anchor_position, name=None)

        # Nothing special going on here yet

