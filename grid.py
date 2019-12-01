"""
grid.py
"""

import flatland_exceptions
from linear_geometry import expand_boundaries, span
from node import Node
from layout_specification import default_cell_alignment, default_cell_padding
from flatland_types import *
from spanning_node import SpanningNode
from single_cell_node import SingleCellNode
from itertools import product


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
    Cells : 2D array of Nodes, initially empty
    Nodes : All the nodes on the grid in placement order
    Row_boundaries : Floor y of each row ascending upward
    Col_boundaries : Left side x of each column, ascending rightward
    Cell_padding : Distances from cell to drawn node boundaries
    Cell_alignment : Default alignment for any placed node (can be overidden locally by node)
    Diagram : The Diagram that this Grid organizes content of
    """

    def __init__(self, diagram):
        self.Cells = []  # No rows or columns in grid yet
        self.Nodes = []  # No nodes in the grid yet
        self.Row_boundaries = [0]
        self.Col_boundaries = [0]
        self.Cell_padding = default_cell_padding
        self.Cell_alignment = default_cell_alignment
        self.Diagram = diagram

    def render(self):
        """Draw self on tablet for diagnostic purposes"""

        tablet = self.Diagram.Canvas.Tablet

        # Draw rows
        left_extent = self.Diagram.Origin.x
        right_extent = self.Diagram.Origin.x + self.Diagram.Size.width
        for h in self.Row_boundaries:
            tablet.Lines.append(Line(
                line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                from_here=Position(left_extent, h + self.Diagram.Origin.y),
                to_there=Position(right_extent, h + self.Diagram.Origin.y)
            )
            )

        # Draw columns
        bottom_extent = self.Diagram.Origin.y
        top_extent = bottom_extent + self.Diagram.Size.height
        for w in self.Col_boundaries:
            tablet.Lines.append(Line(
                line_style=Stroke(width=StrokeWidth.THIN, pattern=StrokeStyle.SOLID),
                from_here=Position(w + self.Diagram.Origin.x, bottom_extent),
                to_there=Position(w + self.Diagram.Origin.x, top_extent)
            )
            )

        # Draw nodes
        [n.render() for n in self.Nodes]

    def add_row(self, cell_height):
        """Adds an empty row upward with the given height"""
        # Compute the new y position relative to the Diagram y origin
        new_row_height = self.Row_boundaries[-1] + cell_height
        # Make sure that it's not above the Diagram area
        if new_row_height > self.Diagram.Size.height:
            raise flatland_exceptions.SheetHeightExceededFE
        # Add it to the list of row boundaries
        self.Row_boundaries.append(new_row_height)
        # Create new empty row with an empty node for each column boundary after the leftmost edge (0)
        empty_row = [None for _ in self.Col_boundaries[1:]]
        # Add it to our list of rows
        self.Cells.append(empty_row)

    def add_column(self, cell_width):
        """Adds an empty column rightward with the given width"""
        # Compute the new rightmost column boundary x value
        new_col_width = self.Col_boundaries[-1] + cell_width
        # Make sure that it's not right of the Diagram area
        if new_col_width > self.Diagram.Size.width:
            raise flatland_exceptions.SheetWidthExceededFE
        # Add it to the list of column boundaries
        self.Col_boundaries.append(new_col_width)
        # For each row, add a rightmost empty node space
        [row.append(None) for row in self.Cells]

    # def place_spanning_node(self, node: SpanningNode) -> Position:
    #     """Places a spanning node"""
    #
    #     # Get the top and right extents for the grid
    #     # The top row or rightmost col number = qty of boundaries exluding 0 on y or x
    #     highest_row_number = max(0, len(self.Row_boundaries[1:]))
    #     rightmost_col_number = max(0, len(self.Col_boundaries[1:]))
    #
    #     # Determine how many rows and columns to add to cover the requested span
    #     # We get zero if there are already enough rows or columns
    #     rows_to_add = max(0, node.High_row - highest_row_number)
    #     columns_to_add = max(0, node.Right_column - rightmost_col_number)
    #
    #     # Which rows or columns that already exist in the grid lie within the
    #     # specified node spanning range?
    #     spanned_existing_rows = list(range(node.Low_row, highest_row_number + 1))
    #     spanned_existing_cols = list(range(node.Left_column, rightmost_col_number + 1))
    #
    #     # Now take all existing cells in the occupied area and ensure that each is empty
    #     if spanned_existing_rows and spanned_existing_cols and \
    #             any([self.Cells[r][c] for r, c in product(spanned_existing_rows, spanned_existing_cols)]):
    #         raise flatland_exceptions.CellOccupiedFE
    #
    #     # Add cell padding to the node to determine grid space required
    #     padded_node_height = node.Size.height + self.Cell_padding.top + self.Cell_padding.bottom
    #     padded_node_width = node.Size.width + self.Cell_padding.left + self.Cell_padding.right
    #
    #     # How much of the padded node height is accommodated by existing rows?
    #     top_boundary = self.Row_boundaries[-1]  # topmost y of grid
    #     bottom_boundary = self.Row_boundaries[-len(spanned_existing_rows) - 1]  # floor boundary of lowest spanned node
    #     overlapped_height = top_boundary - bottom_boundary
    #
    #     # How much of the padded node width is accommodated by existing columns?
    #     right_boundary = self.Col_boundaries[-1]  # rightmost x of grid
    #     left_boundary = self.Col_boundaries[-len(spanned_existing_cols) - 1]  # left boundary of leftmost spanned node
    #     overlapped_width = right_boundary - left_boundary
    #
    #     # How much height would be added by default size extra rows?
    #     default_cell_height = node.Node_type.default_size.height + self.Cell_padding.top + self.Cell_padding.bottom
    #     default_added_height = rows_to_add * default_cell_height  # Height that would be added by default
    #     surplus_height = max(0, padded_node_height - overlapped_height - default_added_height)  # Surplus required
    #     insert_more_height_per_new_cell = 0  # Amount of height to add to each newly created row
    #     if surplus_height:
    #         insert_more_height_per_new_cell += surplus_height / rows_to_add
    #     cell_height = default_cell_height + insert_more_height_per_new_cell
    #
    #     # How much width would be added by default size extra columns?
    #     default_cell_width = node.Node_type.default_size.width + self.Cell_padding.left + self.Cell_padding.right
    #     default_added_width = columns_to_add * default_cell_width  # Width that would be added by default
    #     surplus_width = max(0, padded_node_width - overlapped_width - default_added_width)  # Surplus required
    #     insert_more_width_per_new_cell = 0  # Amount of width to add to each newly created column
    #     if surplus_width:
    #         insert_more_width_per_new_cell += surplus_width / columns_to_add
    #     cell_width = default_cell_width + insert_more_width_per_new_cell
    #
    #     # Now we can add the columns (but first do the same for rows)
    #     # Add extra rows and columns
    #     [self.add_row(cell_height) for _ in range(rows_to_add)]
    #     [self.add_column(cell_width) for _ in range(columns_to_add)]
    #
    #     # Determine Node y position
    #     if node.Local_alignment.vertical == VertAlign.CENTER:
    #         extra_space = span(self.Row_boundaries, node.Low_row, node.High_row) - padded_node_height
    #         assert extra_space >= 0, "Node too wide for span"
    #         lower_y = extra_space / 2 + self.Row_boundaries[node.Low_row - 1]
    #     elif node.Local_alignment.vertical == VertAlign.BOTTOM:
    #         lower_y = self.Row_boundaries[node.Low_row - 1] + self.Cell_padding.bottom
    #     elif node.Local_alignment.vertical == VertAlign.TOP:
    #         lower_y = self.Row_boundaries[node.High_row] - node.Size.height - self.Cell_padding.top
    #
    #     # Determine Node x position
    #     if node.Local_alignment.horizontal == HorizAlign.CENTER:
    #         extra_space = span(self.Col_boundaries, node.Left_column, node.Right_column) - padded_node_width
    #         assert extra_space >= 0, "Node too wide for span"
    #         left_x = extra_space / 2 + self.Col_boundaries[node.Left_column - 1]
    #     elif node.Local_alignment.horizontal == HorizAlign.LEFT:
    #         left_x = self.Col_boundaries[node.Left_column - 1] + self.Cell_padding.left
    #     elif node.Local_alignment.horizontal == HorizAlign.RIGHT:
    #         left_x = self.Col_boundaries[node.Right_column] - node.Size.width - self.Cell_padding.right
    #
    #     # Set node position in Diagram coordinates
    #     node.Position = Position(x=left_x, y=lower_y)
    #
    #     # Assign each cell to this node
    #     spanned_rows = list(range(node.Low_row, node.High_row))
    #     spanned_cols = list(range(node.Left_column, node.Right_column))
    #     # Figure out the correct syntax for statement below
    #     for r, c in product(spanned_rows, spanned_cols):
    #         self.Cells[r][c] = node
    #     self.Nodes.append(node)

    def place_single_cell_node(self, node: SingleCellNode):
        """Places the node adding any required rows or columns"""

        # Determine whether or not we'll need to extend upward or rightward
        rows_to_add = max(0, node.Row - len(self.Row_boundaries[1:]))
        columns_to_add = max(0, node.Column - len(self.Col_boundaries[1:]))

        # If there is already a node at that location, raise an exception
        if not rows_to_add and not columns_to_add and self.Cells[node.Row - 1][node.Column - 1]:
            raise flatland_exceptions.CellOccupiedFE

        # Add necessary rows and columns, if any
        horizontal_padding = self.Cell_padding.left + self.Cell_padding.right
        vertical_padding = self.Cell_padding.top + self.Cell_padding.bottom
        new_cell_height = node.Size.height + vertical_padding
        new_cell_width = node.Size.width + horizontal_padding
        default_cell_height = node.Node_type.default_size.height
        default_cell_width = node.Node_type.default_size.width

        # Check for horizontal overlap
        if not columns_to_add:
            overlap = max(0, node.Size.width + horizontal_padding - span(self.Col_boundaries, node.Column, node.Column))
            if overlap:
                # add the overlap to each col width from the right boundary rightward
                self.Col_boundaries = expand_boundaries(
                    boundaries=self.Col_boundaries, start_boundary=node.Column, expansion=overlap)
                # Check to see if the rightmost column position is now outside the diagram area
                if self.Col_boundaries[-1] > self.Diagram.Size.width:
                    raise flatland_exceptions.SheetWidthExceededFE

        # Check for vertical overlap
        if not rows_to_add:
            overlap = max(0, node.Size.height + vertical_padding - span(self.Row_boundaries, node.Row, node.Row))
            if overlap:
                # add the overlap to each row ceiling from the top of this cell upward
                self.Row_boundaries = expand_boundaries(
                    boundaries=self.Row_boundaries, start_boundary=node.Row, expansion=overlap)
                # Check to see if the rightmost column position is now outside the diagram area
                if self.Row_boundaries[-1] > self.Diagram.Size.height:
                    raise flatland_exceptions.SheetWidthExceededFE

        # Add extra rows and columns (must add the rows first)
        for r in range(rows_to_add):
            # Each new row, except the last will be of default height with the last matching the required height
            add_height = new_cell_height if r == rows_to_add-1 else default_cell_height
            self.add_row(add_height)
        for c in range(columns_to_add):
            add_width = new_cell_width if c == columns_to_add-1 else default_cell_width
            self.add_column(add_width)

        # Place the node in the new location
        self.Cells[node.Row - 1][node.Column - 1] = node
        self.Nodes.append(node)
