"""
node.py
"""
from flatland_types import Position, Rectangle
from diagram_node_types import node_types
import flatland_exceptions


class Node:
    def __init__(self, node_type_name, content, grid, row, column):
        self.content = content
        try:
            self.node_type = node_types[node_type_name]
        except IndexError:
            raise flatland_exceptions.UnknownNodeType
        self.Size = self.node_type.default_size # Rect_Size
        self.Grid = grid
        self.Row = row
        self.Column = column

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
        cell_floor_boundary = 0 if self.Row-2 < 0 else self.Grid.Row_heights[self.Row-2]
        cell_left_boundary = 0 if self.Column-2 < 0 else self.Grid.Col_widths[self.Column-2]

        # Now we create a position coordinate for our lower left corner
        # To obtain Canvas coordinates for this position, we add our relative location in our Cell
        # to our Diagram origin which has already been resolved to Canvas coordinates.
        lower_left_corner = Position(
            x=cell_left_boundary + self.Grid.Cell_padding.left + self.Grid.Diagram.Origin.x,
            y=cell_floor_boundary + self.Grid.Cell_padding.bottom + self.Grid.Diagram.Origin.y
        )
        # We already know our node height and width. For the rectanble border, we look up
        # the style defined for the associated node type. So now we can register our rectangle in the Tablet.
        self.Grid.Diagram.Canvas.Tablet.Rectangles.append(
           Rectangle(line_style=self.node_type.line_style, lower_left=lower_left_corner, size=self.Size)
        )
