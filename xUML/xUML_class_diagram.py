"""
xUML_class_diagram.py – Generates an xUML diagram for an xUML model using the Flatland draw engine
"""
import sys
from pathlib import Path
from flatland_exceptions import FlatlandIOException, MultipleFloatsInSameBranch
from model_parser import ModelParser
from layout_parser import LayoutParser
from flatlanddb import FlatlandDB
from canvas import Canvas
from single_cell_node import SingleCellNode
from connection_types import ConnectorName, OppositeFace, StemName
from tree_connector import TreeConnector
from text_block import TextBlock
from geometry_types import Alignment, VertAlign, HorizAlign
from command_interface import New_Stem, New_Path, New_Trunk_Branch, New_Offshoot_Branch, New_Branch_Set
from typing import Optional, Set, List, Dict
from collections import namedtuple

BranchLeaves = namedtuple('BranchLeaves', 'leaf_stems local_graft next_graft floating_leaf_stem')


class XumlClassDiagram:

    def __init__(self, xuml_model_path: Path, flatland_layout_path: Path, diagram_file_path: Path):
        """Constructor"""
        self.xuml_model_path = xuml_model_path
        self.flatland_layout_path = flatland_layout_path
        self.diagram_file_path = diagram_file_path

        # Parse the model
        try:
            self.model = ModelParser(model_file_path=self.xuml_model_path, debug=True)
        except FlatlandIOException as e:
            sys.exit(e)
        self.subsys = self.model.parse()

        # Parse the layout
        try:
            self.layout = LayoutParser(layout_file_path=self.flatland_layout_path, debug=True)
        except FlatlandIOException as e:
            sys.exit(e)
        self.layout = self.layout.parse()

        # Load the flatland database
        self.db = FlatlandDB()

        # Draw the blank canvas of the appropriate size, diagram type and presentation style
        self.flatland_canvas = self.create_canvas()

        # Draw all of the classes
        self.nodes = self.draw_classes()

        # If there are any relationships, draw them
        if self.subsys.rels:
            cp = self.layout.connector_placement
            for r in self.subsys.rels:  # r is the model data without any layout info
                rnum = r['rnum']
                rlayout = cp[rnum]  # How this r is to be laid out on the diagram
                if 'superclass' in r.keys():
                    self.draw_generalization(rnum=rnum, generalization=r, tree_layout=rlayout)
                else:
                    self.draw_association(rnum=rnum, association=r, binary_layout=rlayout)

        self.flatland_canvas.render()
        print("No problemo")

    def create_canvas(self) -> Canvas:
        """Create a blank canvas"""
        lspec = self.layout.layout_spec
        return Canvas(
            diagram_type=lspec.dtype,
            presentation=lspec.pres,
            notation=lspec.notation,
            standard_sheet_name=lspec.sheet,
            orientation=lspec.orientation,
            drawoutput=self.diagram_file_path,
            show_margin=True
        )

    def draw_classes(self) -> Dict[str, SingleCellNode]:
        """Draw all of the classes on the class diagram"""
        nodes = {}
        np = self.layout.node_placement
        for c in self.subsys.classes:
            cname = c['name']
            nlayout = np[cname]
            nlayout['wrap'] = nlayout.get('wrap', 1)
            name_block = TextBlock(cname, nlayout['wrap'])
            h = HorizAlign[nlayout.get('halign', 'CENTER')]
            v = VertAlign[nlayout.get('valign', 'CENTER')]
            nodes[cname] = SingleCellNode(
                node_type_name='class',
                content=[name_block.text, c['attributes']],
                grid=self.flatland_canvas.Diagram.Grid,
                row=nlayout['node_loc'][0], column=nlayout['node_loc'][1],
                local_alignment=Alignment(vertical=v, horizontal=h)
            )
        return nodes
        # TODO:  Include method section in content
        # TODO:  Add support for axis offset on stem names

    def draw_association(self, rnum, association, binary_layout):
        """Draw the binary association"""
        pass

    def process_leaf_stems(self, lfaces, preceeding_graft: Optional[New_Stem]) -> BranchLeaves:
        """

        :param lfaces:
        :param preceeding_graft: The trunk stem if this is a trunk branch or some leaf stem from the preceeding branch
        :return: branch_leaves
        """
        # A local graft is a stem that establishes the axis of our branch from which all the nodes hang
        # A next branch graft is a stem that establishes that axis for the succeeding branch
        # A floating leaf stem is one that aligns itself with the branch axis (rather than hanging from it)
        # See the tech note tn.2 in the documentation for helpful illustrations of all this

        leaf_stems = set()  # The set of leaf stems that we will create and return
        next_branch_graft = None  # We'll look for at most one of these
        floating_leaf_stem = None  # And at most one of these
        graft = preceeding_graft  # If supplied, we have our one and only local graft

        for name in lfaces.keys():

            anchor = lfaces[name]['anchor']  # Assume that this is not a floating stem
            if lfaces[name]['anchor'] == 'float':
                if floating_leaf_stem:
                    # At most one floating leaf stem permitted in a branch
                    # The parser should have caught this error, but just in case
                    raise MultipleFloatsInSameBranch(set(lfaces.keys()))
                anchor = None

            # Current leaf stem
            lstem = New_Stem(stem_type='subclass', semantic='subclass', node=self.nodes[name],
                             face=lfaces[name]['face'], anchor=anchor, stem_name=None)
            leaf_stems.add(lstem)

            if lfaces[name]['anchor'] == 'float':
                floating_leaf_stem = lstem  # Set the one and only anchorless stem for this branch

            # Graft status
            # If no graft has been set (trunk stem or leaf in preceeding branch as next_branch_graft)
            if not graft and lfaces[name]['graft'] == 'local':
                # A branch can have at most one graft
                graft = lstem

            # Check next branch graft status of this leaf stem
            if not next_branch_graft and lfaces[name]['graft'] == 'next':
                # There can only be one in a branch and the parser should ensure this, raising errors on duplicates
                # Remember the first next branch found, if any
                # We'll use it to graft the subsequent offshoot branch
                next_branch_graft = lstem

        return BranchLeaves(leaf_stems=leaf_stems, local_graft=graft, next_graft=next_branch_graft,
                            floating_leaf_stem=floating_leaf_stem)

    def draw_generalization(self, rnum, generalization, tree_layout):
        """
        One of the rare times it is a good idea to draw one – LS
        """
        super_name = generalization['superclass']
        trunk_node = self.nodes[super_name]
        trunk_layout = tree_layout['trunk_face']

        # Process trunk branch
        trunk_stem = New_Stem(stem_type='superclass', semantic='superclass', node=trunk_node,
                              face=trunk_layout['face'], anchor=trunk_layout['anchor'], stem_name=None)
        tbranch = tree_layout['branches'][0]  # First branch is required and it is the trunk branch
        path_fields = tbranch.get('path', None)
        tbranch_path = None if not path_fields else New_Path(**path_fields)
        leaves = self.process_leaf_stems(
            lfaces=tbranch['leaf_faces'],
            preceeding_graft=trunk_stem if trunk_layout['graft'] else None
        )
        next_branch_graft = leaves.next_graft  # Has a value if some leaf is the graft for the next offshoot branch

        # Create the trunk branch with all of its leaf stems
        trunk_branch = New_Trunk_Branch(
            trunk_stem=trunk_stem, leaf_stems=leaves.leaf_stems, graft=leaves.local_graft,
            path=tbranch_path, floating_leaf_stem=leaves.floating_leaf_stem
        )

        # Process any other offshoot branches (branches other than the trunk branch)
        obranches = []  # Sequence of offshoot branches (usually ends up empty or with only one or two offshoots)
        for obranch in tree_layout['branches'][1:]:
            path_fields = obranch.get('path', None)
            obranch_path = None if not path_fields else New_Path(**path_fields)
            leaves = self.process_leaf_stems(
                lfaces=obranch['leaf_faces'],
                preceeding_graft=next_branch_graft
            )
            obranches.append(
                New_Offshoot_Branch(leaf_stems=leaves.leaf_stems, graft=leaves.local_graft, path=obranch_path,
                                    floating_leaf_stem=leaves.floating_leaf_stem)
            )

        # Now draw the generalization
        branches = New_Branch_Set(trunk_branch=trunk_branch, offshoot_branches=obranches)
        rnum_data = ConnectorName(text=rnum, side=tree_layout['dir'], bend=None)
        TreeConnector(diagram=self.flatland_canvas.Diagram, connector_type='generalization',
                      branches=branches, name=rnum_data)
