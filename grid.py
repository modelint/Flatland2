"""
grid.py
"""
import flatland_exceptions
from node import Node
from layout_specification import default_cell_alignment, default_cell_padding
from flatland_types import Position, Line, Stroke, StrokeStyle, StrokeWidth


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
    Cells : 2D array of Nodes
    Row_heights : List of Row heights
    Col_widths : List of Column widths
    Diagram : The Diagram that this Grid is laid out on
    """
    def __init__(self, diagram):
        self.Cells = []  # No rows or columns yet
        self.Row_heights = []
        self.Cell_padding = default_cell_padding
        self.Cell_alignment = default_cell_alignment
        self.Col_widths = []
        self.Diagram = diagram
        self.Nodes = []

    def render(self):
        """Draw self on tablet for diagnostic purposes"""

        tablet = self.Diagram.Canvas.Tablet

        # Draw rows
        left_extent = self.Diagram.Origin.x
        right_extent = self.Diagram.Origin.x + self.Diagram.Size.width
        this_height = self.Diagram.Origin.y
        for h in self.Row_heights:
            this_height += h
            tablet.Lines.append( Line(
                    line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                    from_here=Position(left_extent, this_height), to_there=Position(right_extent, this_height)
                )
            )

        # Draw columns
        bottom_extent = self.Diagram.Origin.y
        top_extent = bottom_extent + self.Diagram.Size.height
        this_width = self.Diagram.Origin.x
        for w in self.Col_widths:
            this_width += w
            tablet.Lines.append( Line(
                    line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                    from_here=Position(this_width, bottom_extent), to_there=Position(this_width, top_extent)
                )
            )

        # Draw nodes
        [n.render() for n in self.Nodes]

    def add_row(self, height):
        """Adds an empty row upward with the given height"""
        # Add the row height
        if height + sum(self.Row_heights) > self.Diagram.Size.height:
            raise flatland_exceptions.SheetHeightExceededFE
        self.Row_heights.append(height)
        # Insert an empty node for each column
        empty_row = [None for _ in self.Col_widths]
        self.Cells.append(empty_row)

    def add_column(self, width):
        """Adds an empty column rightward with the given width"""
        if width + sum(self.Col_widths) > self.Diagram.Size.width:
            raise flatland_exceptions.SheetWidthExceededFE
        self.Col_widths.append(width)
        # For each row, add a column
        [row.append(None) for row in self.Cells]

    def place_node(self, row, column, node_type_name, content):
        """Places the node adding any required rows or columns"""

        assert row > 0, "Desired row out of bounds: Less than 1"
        assert column > 0, "Desired column out of bounds: Less than 1"
        new_node = Node(node_type_name, content, self, row, column)
        # If the number of rows or columns is less than the amount already there, don't add anything new
        rows_to_add = max(0, row - len(self.Row_heights))
        columns_to_add = max(0, column - len(self.Col_widths))

        # If there is already a node at that location, raise an exception
        if not rows_to_add and not columns_to_add and self.Cells[row-1][column-1]:
            raise flatland_exceptions.CellOccupiedFE

        # Add necessary rows and columns, if any
        node_height = new_node.Size.height + self.Cell_padding.top + self.Cell_padding.bottom
        node_width = new_node.Size.width + self.Cell_padding.left + self.Cell_padding.right
        [self.add_row(node_height) for _ in range(rows_to_add)]
        [self.add_column(node_width) for _ in range(columns_to_add)]

        # Place the node in the new location
        new_node.Row = row
        new_node.Column = column
        self.Cells[row-1][column-1] = new_node
        self.Nodes.append(new_node)


