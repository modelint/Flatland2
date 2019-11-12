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
        for h in self.Row_heights:
            tablet.Lines.append( Line(
                    line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                    from_here=Position(left_extent, h + self.Diagram.Origin.y),
                    to_there=Position(right_extent, h + self.Diagram.Origin.y)
                )
            )

        # Draw columns
        bottom_extent = self.Diagram.Origin.y
        top_extent = bottom_extent + self.Diagram.Size.height
        for w in self.Col_widths:
            tablet.Lines.append( Line(
                    line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                    from_here=Position(w + self.Diagram.Origin.x, bottom_extent),
                    to_there=Position(w + self.Diagram.Origin.x, top_extent)
                )
            )

        # Draw nodes
        [n.render() for n in self.Nodes]

    def add_row(self, cell_height):
        """Adds an empty row upward with the given height"""
        # Add the row height
        new_row_height = cell_height if not self.Row_heights else self.Row_heights[-1] + cell_height
        if new_row_height > self.Diagram.Size.height:
            raise flatland_exceptions.SheetHeightExceededFE
        self.Row_heights.append(new_row_height)
        # Insert an empty node for each column
        empty_row = [None for _ in self.Col_widths]
        self.Cells.append(empty_row)

    def add_column(self, cell_width):
        """Adds an empty column rightward with the given width"""
        new_col_width = cell_width if not self.Col_widths else self.Col_widths[-1] + cell_width
        if new_col_width > self.Diagram.Size.width:
            raise flatland_exceptions.SheetWidthExceededFE
        self.Col_widths.append(new_col_width)
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
        cell_height = new_node.Size.height + self.Cell_padding.top + self.Cell_padding.bottom
        cell_width = new_node.Size.width + self.Cell_padding.left + self.Cell_padding.right

        # Check for horizontal overlap
        if not columns_to_add:
            left, right = column-2, column-1
            right_col_pos = self.Col_widths[right]
            left_col_pos = 0 if left < 0 else self.Col_widths[left]
            current_col_width = right_col_pos - left_col_pos
            overlap = max(0, cell_width - current_col_width)
            if overlap:
                # add the overlap to each col width from the right side of this cell outward
                self.Col_widths = self.Col_widths[:right] + [c + overlap for c in self.Col_widths[right:]]
                # Check to see if the rightmost column position is now outside the diagram area
                if self.Col_widths[-1] > self.Diagram.Size.width:
                    raise flatland_exceptions.SheetWidthExceededFE

        # Check for vertical overlap
        if not rows_to_add:
            bottom, top = row-2, row-1
            row_ceiling = self.Row_heights[top]
            row_floor = 0 if bottom < 0 else self.Row_heights[bottom]
            current_row_height = row_ceiling - row_floor
            overlap = max(0, cell_height - current_row_height)
            if overlap:
                # add the overlap to each row ceiling from the top of this cell upward
                self.Row_heights = self.Row_heights[:top] + [r + overlap for r in self.Row_heights[top:]]
                # Check to see if the rightmost column position is now outside the diagram area
                if self.Row_heights[-1] > self.Diagram.Size.height:
                    raise flatland_exceptions.SheetWidthExceededFE


        [self.add_row(cell_height) for _ in range(rows_to_add)]
        [self.add_column(cell_width) for _ in range(columns_to_add)]

        # Place the node in the new location
        new_node.Row = row
        new_node.Column = column
        self.Cells[row-1][column-1] = new_node
        self.Nodes.append(new_node)


