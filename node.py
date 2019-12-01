"""
node.py
"""
from flatland_types import Rect_Size, Position
from diagram_node_types import node_types
from compartment import Compartment
import flatland_exceptions
from layout_specification import default_cell_alignment


class Node:
    """
    This is a rectangular diagram symbol consisting of one or more UML style Compartments
    stacked in a vertical order.

    Attributes
    ---
    Content : The unformatted text that will be drawn into the Node's Compartments
              organized as a dictionary with the keys as compartment names such as 'class name', 'attributes', etc.
    Grid : The Node is positioned into this Grid
    Compartments : Each compartment to be filled in
    Local_alignment : Position of the node in the spanned area, vertical and horizontal
    """

    def __init__(self, node_type_name, content, grid, local_alignment):
        if not content:
            raise flatland_exceptions.NoContentForCompartment
        self.Content = content
        try:
            self.Node_type = node_types[node_type_name]
        except IndexError:
            raise flatland_exceptions.UnknownNodeType
        self.Grid = grid
        # Create a compartment for each element of content
        # If content is missing, make less compartments
        self.Compartments = [
            Compartment(node=self, name=comp_name, content=text)
            for text, comp_name in zip(self.Content, self.Node_type.compartments.keys())
        ]
        self.Local_alignment = local_alignment if local_alignment else default_cell_alignment

    @property
    def Canvas_position(self):
        """Overridden: Position of lower left corner on canvas is computed differently by each subclass"""
        return None

    @property
    def Size(self):
        """Adjust node size to accommodate text content in each compartment"""
        # For all compartments in this node, get the max height and width
        crects = [c.Text_block_size for c in self.Compartments]
        # Get the max of each compartment width and the default node type width
        max_width = max([r.width for r in crects] + [self.Node_type.default_size.width])
        # Height is the sum of all compartment heights
        # Ignore the default node type height for now
        node_height = sum([r.height for r in crects])
        # Return a rectangle with the
        return Rect_Size(height=node_height, width=max_width)

    def render(self):
        """Calculate final position on the Canvas and register my rectangle in the Tablet"""

        # Start at the bottom of the node and render each compartment upward
        comp_y = self.Canvas_position.y
        for c in self.Compartments[::-1]: # Reverse the compartment order to bottom up
            c.render(Position(x=self.Canvas_position.x, y=comp_y))
            comp_y += c.Size.height # bottom of next compartment is top of this one
