""" single_cell_node.py """

from linear_geometry import align_on_axis
from node import Node
from flatland_types import Position


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
        """Calculate position on the Canvas"""
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

    def render(self):
        """Calculate final position on the Canvas and register my rectangle in the Tablet"""

        # To get our position inside the Cell, we need to resolve the coordinates of our lower left corner.
        # That's easy to do once we have the height of the cell floor and the horizontal position of
        # the left boundary.
        #
        # If we are in the bottom row, the floor is zero relative to our Grid/Diagram
        # We have to subtract two from our Row, one to index into the array – that gets us
        # to our Row height, which is the ceiling boundary.  But we really want the ceiling
        # boundary of the Row below us, hence we subtract one more.  Careful, though since
        # the bottom-most Row has no lower row.  In that case, the floor is at zero.
        # Similar logic applies when obtaining the left boundary, but with Columns.
        # cell_floor_boundary = self.Grid.Row_boundaries[self.Row - 1]
        # cell_left_boundary = self.Grid.Col_boundaries[self.Column - 1]

        # Now we create a position coordinate for our lower left corner
        # To obtain Canvas coordinates for this position, we add our relative location in our Cell
        # to our Diagram origin which has already been resolved to Canvas coordinates.
        # lower_left_corner = Position(
        #     x=cell_left_boundary + self.Grid.Cell_padding.left + self.Grid.Diagram.Origin.x,
        #     y=cell_floor_boundary + self.Grid.Cell_padding.bottom + self.Grid.Diagram.Origin.y
        # )

        comp_y = self.Canvas_position.y
        for c in self.Compartments[::-1]:
            c.render(Position(x=self.Canvas_position.x, y=comp_y))
            comp_y += c.Size.height
