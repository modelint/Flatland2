"""
hierarchy_connector.py
"""
from connector import Connector
from trunk_stem import TrunkStem
from command_interface import New_Branch_Set
from connection_types import NodeFace, HorizontalFace
from hanging_branch_stem import HangingBranchStem
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle
from geometry_types import Position


class HierarchyConnector(Connector):
    """
    A Hierarchy Connector connects a trunk Node to one or more branch Nodes in a tree structure. It can be used to
    draw a generalization relationship on a class diagram, for example.

    Attributes:
        Trunk_stem : This Stem attaches the single Node in the trunk position
        Branches : The Branch Stems organized as a sequence of sets. Each set connects to the same line segment.
    """

    def __init__(self, diagram, connector_type, branches: New_Branch_Set ):
        Connector.__init__(self, diagram, connector_type=connector_type)

        # TODO: Create offshoot branches, only single branch, laneless branch handled for now

        # Create trunk branch
        trunk_stem = branches.trunk_branch.trunk_stem
        tface_position = trunk_stem.node.Face_position(trunk_stem.face)
        bface_positions = [bstem.node.Face_position(b.face) for bstem in branches.trunk_branch.branch_stems]
        if trunk_stem.face == NodeFace.BOTTOM or trunk_stem.face == NodeFace.LEFT:
            closest_bface_position = max(bface_positions)
            branch_axis = (tface_position - closest_bface_position) / 2
        else:
            closest_bface_position = min(bface_positions)
            branch_axis = (closest_bface_position - tface_position) / 2

        # Create Trunk Stem
        self.Trunk_stem = TrunkStem(
            connector=self,
            stem_type=trunk_stem.stem_type,
            semantic=trunk_stem.semantic,
            node=trunk_stem.node,
            face=trunk_stem.face,
            anchor_position=trunk_stem.anchor,
            branch_axis=branch_axis
        )

        # Create Branch Stems
        self.Branches = []
        for bstem in branches.trunk_branch.branch_stems:
            branch_stems = set()
            for s in b:
                branch_stems.add(
                    HangingBranchStem(
                        connector=self,
                        stem_type=s.stem_type,
                        semantic=s.semantic,
                        node=s.node,
                        face=s.face,
                        anchor_position=s.anchor,
                        branch_axis=branch_axis
                    )
                )
            self.Branches.append(branch_stems)

        # Draw self
        self.render()

    def render(self):
        """
        Draw the Branch line segment for a single Branch Hierarchy Connector
        """
        if self.Trunk_stem.Node_face in HorizontalFace:
            y1 = y2 = self.Trunk_stem.Vine_end.y
            xvals = [b.Vine_end.x for b in self.Branches[0]]
            x1, x2 = min(xvals), max(xvals)
        else:
            x1 = x2 = self.Trunk_stem.Vine_end.x
            yvals = [b.Vine_end.x for b in self.Branches[0]]
            y1, y2 = min(yvals), max(yvals)

        tablet = self.Diagram.Canvas.Tablet
        tablet.Lines.append(Line(
            line_style=Stroke(StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
            from_here=Position(x1, y1), to_there=Position(x2,y2))
        )
