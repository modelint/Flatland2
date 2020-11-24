"""
floating_leaf_stem.py
"""
from stem import StemName
from floating_stem import FloatingStem
from stem_type import StemType
from connection_types import NodeFace
from geometry_types import Position
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector import Connector
    from node import Node
    from grafted_branch import GraftedBranch


class FloatingLeafStem(FloatingStem):
    def __init__(self, connector: 'Connector', stem_type: StemType, semantic: str,
                 node: 'Node', face: NodeFace, grafted_branch: 'GraftedBranch', root_position: Position,
                 name: StemName = None):
        FloatingStem.__init__(self, connector, stem_type, semantic, node, face, root_position, name)
        self.Grafted_branch = grafted_branch
