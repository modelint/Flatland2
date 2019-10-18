"""
grid.py
"""
from exceptions import *
from node import Node
from collections import namedtuple
from flatland_types import Position

# Row = namedtuple('Row', 'position nodes')
# Column = namedtuple('Col', 'position')


class Grid:
    """
    Positioning nodes in a drawing tool typically involves pixel level placement which
    is overkill for most types of model drawings. To get straight lines you need to fidget
    the pixel level position and alignment. Some tools let you snap to a grid, but the grid
    is usually fine grained to make it possible to position the node connectors.

    In Flatland, we use a single Grid laid out across a Canvas like a spreadsheet. Rows and
    Columns in the Grid can be any width, but are generally small, medium or large node-sized.
    In a class diagram, for example, each Column is roughly the size of one class-width and each Row
    is roughly the height of a single class-height. This makes it easy to specify position using
    a text markup language. Each Node is placed at a grid coordinate with a default or specified alignment.
    For particularly large nodes, you can position them on a single Cell of the Grid and then have
    them span multiple Rows or Columns.

    So the Grid defines a coordinate system for the placement of Nodes.

    It starts out empty, with no Rows or Columns and only an origin. Each loaded Node specifies a desired
    placement coordinate. The Grid then extends by the necessary (if any) Rows and Columns to create a place
    to position the Node.

    Attributes
    ---
    Origin : Position(x,y)
        The lower left corner of the Grid is positioned here in point coordinates relative to the Sheet
    Cells : 2D array of Nodes
    Heights : List of Row heights
    Widths : List of Column widths
    Diagram : The Diagram that this Grid is laid out on
    """
    def __init__(self, diagram):
        self.Origin = Position(x=diagram.Canvas.Padding.left, y=diagram.Canvas.Padding.right)
        self.Cells = []  # No rows or columns yet
        self.Heights = []
        self.Widths = []
        self.Diagram = diagram

    def add_row(self, height):
        """Adds an empty row upward with the given height"""
        # Add the row height
        if height + sum(self.Heights) > self.Diagram.Size.height:
            raise SheetHeightExceededFE
        self.Rows.append(height)
        # Insert an empty node for each column
        empty_row = [None for _ in range(self.Widths)]
        self.Cells.append(empty_row)

    def add_col(self, width):
        """Adds an empty column rightward with the given width"""
        if width + sum(self.Widths) > self.Diagram.Size.width:
            raise SheetWidthExceededFE
        self.Columns.append(width)
        # For each row, add a column
        [row.append(None) for row in self.Cells]

    def place_node(self, row, column, node_type, content):
        """Places the node adding any required rows or columns"""

        new_node = Node(node_type, content)
        # If the number of rows or columns is less than the amount already there, don't add anything new
        rows_to_add = max(0, row - len(self.Heights))
        columns_to_add = max(0, column - len(self.Widths))

        # If there is already a node at that location, raise an exception
        if not rows_to_add and not columns_to_add and self.Cells[row][column]:
            raise CellOccupiedFE

        # Add necessary rows and columns, if any
        [self.add_row(node_type.max_size.height) for _ in range(rows_to_add)]
        [self.add_column(node_type.max_size.width) for _ in range(columns_to_add)]

        # Ensure that the cell is large enough to fit the node
        cell_height = self.Heights[row]
        cell_width = self.Widths[column]
        padding = self.Diagram.Canvas.Padding
        needed_height = padding.top + padding.bottom + new_node.Size.height
        needed_width = padding.top + padding.bottom + new_node.Size.width
        if needed_height > self.Rows[-1] and




        new_location = new_node

        # If necessary, resize the row, columno or both
        # and put the node there (up to a maximum size)

        # If the maximum size is exceeded and no span is specified, raise an exception
        # If there is a span, but it overlaps other content in adjacent cells, raise an exception

        # If the location does not exist, expand the grid

        # If the grid exceeds the sheet size, raise an exception
