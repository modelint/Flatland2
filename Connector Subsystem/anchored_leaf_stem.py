"""
anchored_leaf_stem.py
"""

from anchored_tree_stem import AnchoredTreeStem
from connection_types import NodeFace, AnchorPosition
from stem_type import StemType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector import Connector
    from node import Node


class AnchoredLeafStem(AnchoredTreeStem):
    def __init__(self, connector: 'Connector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, anchor_position: AnchorPosition):
        AnchoredTreeStem.__init__(
            self, connector, stem_type, semantic, node, face, anchor_position)
