""" single_cell_node.py """

from linear_geometry import align_on_axis
from node import Node
from geometry_types import Position


class SingleCellNode(Node):
    """
    A node enveloped by a single Cell

    Attributes
    ---
    Row : Placed in this row
    Column : Placed at this column
    """

    def __init__(self, node_type_name, content, grid, row, column, local_alignment=None):
        super().__init__(node_type_name, content, grid, local_alignment)
        assert row > 0, "Negative row"
        assert column > 0, "Negative column"
        self.Row = row
        self.Column = column
        self.Grid.place_single_cell_node(self)

    @property
    def Canvas_position(self):
        """Position of lower left corner on the Canvas"""
        # Workout alignment within Cell
        lower_left_x = align_on_axis(
            axis_alignment=self.Local_alignment.horizontal.value,
            boundaries=self.Grid.Col_boundaries, from_grid_unit=self.Column, to_grid_unit=self.Column,
            from_padding=self.Grid.Cell_padding.left, to_padding=self.Grid.Cell_padding.right,
            node_extent=self.Size.width
        ) + self.Grid.Diagram.Origin.x # +  self.Grid.Col_boundaries[self.Column-1]
        lower_left_y = align_on_axis(
            axis_alignment=self.Local_alignment.vertical.value,
            boundaries=self.Grid.Row_boundaries, from_grid_unit=self.Row, to_grid_unit=self.Row,
            from_padding=self.Grid.Cell_padding.bottom, to_padding=self.Grid.Cell_padding.top,
            node_extent=self.Size.height
        ) + self.Grid.Diagram.Origin.y # + self.Grid.Row_boundaries[self.Row-1]
        return Position(x=lower_left_x, y=lower_left_y)
