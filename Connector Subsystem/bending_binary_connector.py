"""
bending_binary_connector.py
"""
from binary_connector import BinaryConnector
from tertiary_stem import TertiaryStem
from anchored_stem import AnchoredStem
from connection_types import HorizontalFace, LaneOrientation, OppositeFace
from draw_types import StrokeWidth, StrokeStyle
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

        self.Tertiary_stem = None
        if tertiary_stem:
            # Find all line segments in the bending connector parallel to the tertiary node face
            # Where the tertiary stem is attached
            points = [self.T_stem.Vine_end] + self.Corners + [self.P_stem.Vine_end]
            segs = set(zip(points, points[1:]))
            horizontal_segs = {s for s in segs if s[0].y == s[1].y}
            parallel_segs = horizontal_segs if tertiary_stem.face in HorizontalFace else segs - horizontal_segs
            self.Tertiary_stem = TertiaryStem(
                connector=self,
                stem_type=tertiary_stem.stem_type,
                semantic=tertiary_stem.semantic,
                node=tertiary_stem.node,
                face=tertiary_stem.face,
                anchor_position=tertiary_stem.anchor,
                parallel_segs=parallel_segs
            )

        self.render()

    def compute_corners(self):
        if not self.Paths:  # Only one corner
            return [ self.node_to_node() ]
        else:
            corners = []
            to_horizontal_path = self.T_stem.Node_face in HorizontalFace
            first_path = True
            for p in self.Paths:
                if to_horizontal_path:  # Row
                    self.Diagram.Grid.add_lane(lane=p.lane, orientation=LaneOrientation.ROW)
                    previous_x = self.T_stem.Vine_end.x if first_path else corners[-1].x
                    rut_y = self.Diagram.Grid.get_rut(lane=p.lane, rut=p.rut, orientation=LaneOrientation.ROW)
                    x, y = previous_x, rut_y
                else:  # Column
                    self.Diagram.Grid.add_lane(lane=p.lane, orientation=LaneOrientation.COLUMN)
                    previous_y = self.T_stem.Vine_end.y if first_path else corners[-1].y
                    rut_x = self.Diagram.Grid.get_rut(lane=p.lane, rut=p.rut, orientation=LaneOrientation.COLUMN)
                    x, y = rut_x, previous_y
                corners.append(Position(x,y))
                to_horizontal_path = not to_horizontal_path  # toggle the orientation
                first_path = False
            # Cap final path with last corner
            if to_horizontal_path:
                x = corners[-1].x
                y = self.P_stem.Vine_end.y
            else:
                x = self.P_stem.Vine_end.x
                y = corners[-1].y
            corners.append(Position(x,y))
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

