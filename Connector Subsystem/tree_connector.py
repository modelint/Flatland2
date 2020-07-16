"""
tree_connector.py
"""
from connector import Connector
from trunk_stem import TrunkStem
from grafted_branch import GraftedBranch
from interpolated_branch import InterpolatedBranch
from rut_branch import RutBranch
from command_interface import New_Branch_Set, New_Stem
from anchored_leaf_stem import AnchoredLeafStem
from connector_type import ConnectorTypeName
from diagram import Diagram
from collections import namedtuple
from typing import Set
from general_types import Index

StemGroup = namedtuple('StemGroup', 'hanging_stems grafting_stem new_floating_stem, path')
LeafGroup = namedtuple('LeafGroup', 'hleaves gleaf')


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

        # Unpack new trunk spec and create its Anchored Trunk Stem
        new_tstem = branches.trunk_branch.trunk_stem
        self.Trunk_stem = self.unpack_trunk(new_tstem)
        # If the trunk stem has been specified as a grafting stem, make it this branch's gstem
        gstem = self.Trunk_stem if branches.trunk_branch.graft == new_tstem else None

        # Unpack the leaf stems for the trunk branch (there must be at least one leaf)
        assert len(branches.trunk_branch.leaf_stems) > 0, "No leaf stems specified for trunk branch"
        unpacked_hanging_stems = self.unpack_hanging_leaves(
            branches.trunk_branch.leaf_stems,
            branches.trunk_branch.graft
        )
        self.Leaf_stems = unpacked_hanging_stems.hleaves
        assert not (gstem and unpacked_hanging_stems.gleaf), "Both trunk and a leaf stem grafts in the same branch"
        gstem = unpacked_hanging_stems.gleaf if unpacked_hanging_stems.gleaf else None

        anchored_tree_stems = {s for s in self.Leaf_stems}
        anchored_tree_stems.add(self.Trunk_stem)

        trunk_branch_stem_group = StemGroup(
            hanging_stems=anchored_tree_stems,
            grafting_stem=gstem,
            new_floating_stem=branches.trunk_branch.floating_leaf_stem,
            path=branches.trunk_branch.path
        )
        branches_to_make = [trunk_branch_stem_group]  # first branch in the sequence
        # We will loop through these further down and, for each,
        # create the appropriate branch type

        # Now go through any offshoot branches to complete the branches_to_make sequence

        for o in branches.offshoot_branches:
            unpacked_hanging_stems = self.unpack_hanging_leaves(o.leaf_stems, o.graft)
            self.Leaf_stems = self.Leaf_stems.union(unpacked_hanging_stems.hleaves)
            trunk_branch_stem_group = StemGroup(
                hanging_stems=unpacked_hanging_stems.hleaves,
                grafting_stem=unpacked_hanging_stems.gleaf,
                new_floating_stem=o.floating_leaf_stem,
                path=o.path
            )
            branches_to_make.append(trunk_branch_stem_group)

        # Create all of the branches
        assert len(branches_to_make) > 0, "No branches to make"

        self.Branches = []
        for i, b in enumerate(branches_to_make):
            order = Index(i)  # Cast int to Index type
            if b.path:
                this_branch = RutBranch(order, connector=self, path=b.path, hanging_stems=b.hanging_stems)
            elif b.grafting_stem:
                this_branch = GraftedBranch(order, connector=self, hanging_stems=b.hanging_stems,
                                            grafting_stem=b.grafting_stem, new_floating_stem=b.new_floating_stem)
            else:
                this_branch = InterpolatedBranch(order, connector=self, hanging_stems=b.hanging_stems)
            self.Branches.append(this_branch)

    def unpack_hanging_leaves(self, new_leaves: Set[New_Stem], new_graft_leaf: New_Stem) -> LeafGroup:
        """
        Unpack all new anchored leaves for a branch
        :param new_graft_leaf: The optional user designated grafting leaf stem for the Branch
        :param new_leaves:  A set of new leaf specifications provided by the user
        :return: The newly created Anchored Leave Stems and a reference to the one grafting stem, if any
        """
        hanging_leaves = set()
        hanging_graft_leaf = None
        # Create Leaf Stems
        for leaf_stem in new_leaves:
            anchored_hanging_leaf = AnchoredLeafStem(
                connector=self,
                stem_type=leaf_stem.stem_type,
                semantic=leaf_stem.semantic,
                node=leaf_stem.node,
                face=leaf_stem.face,
                anchor_position=leaf_stem.anchor
            )
            hanging_leaves.add(anchored_hanging_leaf)
            # Check to see if this is a grafting stem, if so register this newly created leaf as such
            if not hanging_graft_leaf and leaf_stem == new_graft_leaf:
                # There can only be one, so do this assignment at most once per new_leaves set
                hanging_graft_leaf = anchored_hanging_leaf
        return LeafGroup(hanging_leaves, hanging_graft_leaf)

    def unpack_trunk(self, new_trunk: New_Stem) -> TrunkStem:
        """
        Unpack the trunk stem specification for this Tree Connector
        :param new_trunk:
        :return:
        """
        return TrunkStem(
            connector=self,
            stem_type=new_trunk.stem_type,
            semantic=new_trunk.semantic,
            node=new_trunk.node,
            face=new_trunk.face,
            anchor_position=new_trunk.anchor
        )

    def render(self):
        """
        Draw the Branch line segment for a single-branch Tree Connector
        """
        for b in self.Branches:
            b.render()
