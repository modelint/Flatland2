"""
node.py
"""
from geometry_types import Rect_Size, Position, Alignment
from compartment import Compartment
from flatland_exceptions import UnknownNodeType, IncompatibleNodeType, EmptyTitleCompartment
from layout_specification import default_cell_alignment
from connection_types import NodeFace
from flatlanddb import FlatlandDB as fdb
from typing import TYPE_CHECKING, List, Optional
from collections import namedtuple
from node_type import NodeType
from sqlalchemy import select, and_

if TYPE_CHECKING:
    from grid import Grid

NodeType = namedtuple('NodeType', 'Name, About, Corner_rounding, Border, Default_size, Max_size')


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

    def __init__(self, node_type_name: str, content: List[str], grid: 'Grid', local_alignment: Optional[Alignment]):
        self.Grid = grid

        # Validate node type name
        # Check that the node type and its diagram type name are in the database
        ntypes = fdb.MetaData.tables['Node Type']
        q = select([ntypes.c['Name'], ntypes.c['Diagram type']]).where(ntypes.c['Name'] == node_type_name)
        i = fdb.Connection.execute(q).fetchone()
        if not i:
            raise UnknownNodeType(node_type_name)
        if i['Diagram type'] != self.Grid.Diagram.Diagram_type:
            raise IncompatibleNodeType(node_type_name, self.Grid.Diagram.Diagram_type)
        # All good, so save the name of the Node Type
        self.Node_type = NodeType(dict(i))

        # Create a compartment for each element of content
        # If content is missing, make less compartments
        # First, get a list of the compartment type rows from the database
        ctypes = fdb.MetaData.tables['Compartment Type']
        q = select([ctypes]).where(
            and_(ctypes.c['Node type'] == self.Node_type, ctypes.c['Diagram type'] == self.Grid.Diagram.Diagram_type)
        ).order_by('Stack order')
        found = fdb.Connection.execute(q).fetchall()
        # We take the found ctypes and the text content, which is a list of text blocks, both ordered top to bottom
        # as they will appear in the Node, and zip these lists together to get tuples (text, instance)
        # For each tuple, we can create an instance of Compartment
        # The list of newly created compartments is then assigned to the Node's Compartments attribute
        self.Compartments = [Compartment(node=self, ctype_data=dict(i), content=text)
                             for text, i in zip(content, found)]
        # The Node will be aligned in the Cell according to either the specified local alignment or, if none,
        # the default cell alignment that we got from the global Layout Specification
        self.Local_alignment = local_alignment if local_alignment else default_cell_alignment

    @property
    def Canvas_position(self):
        """
        Must be overidden by each subclass.
        :return: None, None
        """
        return Position(x=None, y=None)

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

    def Face_position(self, face: NodeFace):
        """
        Returns the position of the specified face on the x or y axis
        :param face : A node face
        :return: position in x or y
        """
        if face == NodeFace.TOP:
            return self.Canvas_position.y + self.Size.height
        elif face == NodeFace.BOTTOM:
            return self.Canvas_position.y
        elif face == NodeFace.RIGHT:
            return self.Canvas_position.x + self.Size.width
        else:
            return self.Canvas_position.x

    def render(self):
        """Calculate final position on the Canvas and register my rectangle in the Tablet"""

        print("Drawing node")
        # Start at the bottom of the node and render each compartment upward
        comp_y = self.Canvas_position.y
        for c in self.Compartments[::-1]:  # Reverse the compartment order to bottom up
            c.render(Position(x=self.Canvas_position.x, y=comp_y))
            comp_y += c.Size.height  # bottom of next compartment is top of this one
