"""
bending_binary_connector.py
"""
from binary_connector import BinaryConnector
from anchored_stem import AnchoredStem
from connection_types import HorizontalFace, LaneOrientation
from draw_types import Line, Stroke, StrokeWidth, StrokeStyle
from geometry_types import Position
from open_polygon import OpenPolygon


class BendingBinaryConnector(BinaryConnector):
    """
    This is a Binary Connector that must turn one or more corners to connect its opposing Binary Stems.
    In such a case the two Binary Stems will be counterparts and we can arbitrarily start drawing a line
    from one of the Counterpart Binary Stems to the other. In fact, we could start from both ends and work
    toward the middle or start from the middle and work our way out. So the terms “start” and “end” could
    just as easily have been labeled “A” and “B”.
    """

    def __init__(self, diagram, anchored_stem_t, anchored_stem_p, paths=None, tertiary_stem=None):
        BinaryConnector.__init__(self, diagram, tertiary_stem)

        self.Paths = paths if not None else []

        self.T_stem = AnchoredStem(
            connector=self,
            stem_type=anchored_stem_t.stem_type,
            semantic=anchored_stem_t.semantic,
            node=anchored_stem_t.node,
            face=anchored_stem_t.face,
            anchor_position=anchored_stem_t.anchor
        )
        self.P_stem = AnchoredStem(
            connector=self,
            stem_type=anchored_stem_p.stem_type,
            semantic=anchored_stem_p.semantic,
            node=anchored_stem_p.node,
            face=anchored_stem_p.face,
            anchor_position=anchored_stem_p.anchor
        )
        self.Corners = self.compute_corners()
        self.render()

    def compute_corners(self):
        if not self.Paths:  # Only one corner
            return [ self.node_to_node() ]
        else:
            corners = []
            # Add first corner of first path
            path_horizontal = self.T_stem.Node_face in HorizontalFace
            first_path = self.Paths[0]  # First path yields two corners
            if path_horizontal:  # Row
                self.Diagram.Grid.add_lane(lane=first_path.lane, orientation=LaneOrientation.ROW)
                x1 = self.T_stem.Vine_end.x
                x2 = self.P_stem.Vine_end.x
                y = self.Diagram.Grid.get_rut(lane=first_path.lane, rut=first_path.rut, orientation=LaneOrientation.ROW)
                corners.append(Position(x=x1,y=y))
                corners.append(Position(x=x2,y=y))
            else:  # Column
                self.Diagram.Grid.add_lane(lane=first_path.lane, orientation=LaneOrientation.COLUMN)
                y1 = self.T_stem.Vine_end.y
                y2 = self.P_stem.Vine_end.y
                x = self.Diagram.Grid.get_rut(lane=first_path.lane, orientation=LaneOrientation.COLUMN)
                corners.append(Position(x=x, y=y1))
                corners.append(Position(x=x, y=y2))

            for p in self.Paths[1:]: # If any, each following path yields one corner
                # TODO: Recheck before running this code for double bend case
                path_horizontal = not path_horizontal  # toggle the orientation
                if path_horizontal:  # Row
                    # TODO: Refactor so that add lanes are not repeated for first and subsequent paths
                    self.Diagram.Grid.add_lane(lane=p.lane, orientation=LaneOrientation.ROW)
                    x = self.Diagram.Grid.get_rut(lane=p.lane, rut=p.rut, orientation=LaneOrientation.ROW)
                    y = corners[-1].y
                else:  # Column
                    self.Diagram.Grid.add_lane(lane=p.lane, orientation=LaneOrientation.COLUMN)
                    x = corners[-1].x
                    y = self.Diagram.Grid.get_rut(lane=p.lane, rut=p.rut, orientation=LaneOrientation.COLUMN)
            return corners

    def node_to_node(self):
        """
        Create a single corner between two Nodes
        :return: Corner
        """
        if self.T_stem.Node_face in HorizontalFace:
            corner_x = self.T_stem.Root_end.x
            corner_y = self.P_stem.Root_end.y
        else:
            corner_x = self.P_stem.Root_end.x
            corner_y = self.T_stem.Root_end.y

        return Position(corner_x, corner_y)

    def render(self):
        """
        Draw a line frome the vine end of the T node stem to the vine end of the P node stem
        """
        # Create line from vine end of T_stem to vine end of P_stem, bending along the way
        OpenPolygon(tablet=self.Diagram.Canvas.Tablet, style=StrokeWidth.THIN, width=StrokeStyle.SOLID,
                    points=[self.T_stem.Vine_end] + self.Corners + [self.P_stem.Vine_end]).render()

