"""
tree_connector.py
"""
from connector import Connector
from trunk_stem import TrunkStem
from interpolated_branch import InterpolatedBranch
from command_interface import New_Branch_Set
from connection_types import HorizontalFace
from anchored_leaf_stem import AnchoredLeafStem
from floating_leaf_stem import FloatingLeafStem
from geometry_types import Position
from connector_type import ConnectorTypeName
from diagram import Diagram


class TreeConnector(Connector):
    """
    A Tree Connector connects a trunk Node to one or more branch Nodes in a tree structure. It can be used to
    draw a generalization relationship on a class diagram, for example.

    Attributes:
        Trunk_stem : This Stem attaches the single Node in the trunk position
        Leaf_stems : The Branch Stems organized as a sequence of sets. Each set connects to the same line segment.
    """

    def __init__(self, diagram: Diagram, connector_type: ConnectorTypeName, branches: New_Branch_Set):
        Connector.__init__(self, diagram, connector_type)

        # Create Trunk Stem
        trunk_stem = branches.trunk_branch.trunk_stem
        self.Trunk_stem = TrunkStem(
            connector=self,
            stem_type=trunk_stem.stem_type,
            semantic=trunk_stem.semantic,
            node=trunk_stem.node,
            face=trunk_stem.face,
            anchor_position=trunk_stem.anchor
        )

        # Create Leaf Stems
        self.Leaf_stems = set()
        for lstem in branches.trunk_branch.leaf_stems:
            for s in lstem:
                self.Leaf_stems.add(
                    AnchoredLeafStem(
                        connector=self,
                        stem_type=s.stem_type,
                        semantic=s.semantic,
                        node=s.node,
                        face=s.face,
                        anchor_position=s.anchor
                    )
                )

        anchored_stems = {s for s in self.Leaf_stems}

        fleaf = branches.trunk_branch.floating_leaf_stem
        if fleaf:
            self.Leaf_stems.add(
                FloatingLeafStem(
                    connector=self,
                    stem_type=fleaf.stem_type,
                    semantic=fleaf.semantic,
                    node=fleaf.node,
                    face=fleaf.face
                )
            )

        self.Branches = []

        # Create trunk branch
        if branches.trunk_branch.path:
            pass
        # Create a Rut Branch
        # TODO: Handle this case
        elif branches.trunk_branch.graft:
            pass
            # Create a Grafted Branch
            # TODO: Handle this case
        else:
            # Create an Interpolated Branch between all non-graft, non-floating anchored tree stems
            self.Branches.append(InterpolatedBranch(connector=self, hanging_stems=anchored_stems))

        # Draw self
        self.render()

    def render(self):
        """
        Draw the Branch line segment for a single-branch Tree Connector
        """
        for b in self.Branches:
            b.render()
