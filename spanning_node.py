""" spanning_node.py """

from node import Node
from flatland_types import *


class SpanningNode(Node):
    """
    A node that spans multiple rows and/or columns. On a class diagram this is useful for positioning
    a superclass above two subclasses. The superclass spans two columns each containing a subclass.

    The simplest case of a span involves just one column and one row. But it is best to specify that as
    a single cell node.  But it would be common to specify a spanning node only across rows or columns.
    Only a particularly large node would need both rows and columns.

    Note that a cell may contain at most one Node. So if a node spans into some cell, no other Node may be placed
    in that Cell even if the Node isn't large enough to intrude into the Cell area.  Therefore, the modeler
    must take care to not specify too large an area to span relative to the actual Node size.

    Attributes
    ---
    High_row : The topmost row
    Low_row : The lowest row
    Left_column : The leftmost column
    Right_column : The rightmost column
    Position : Lower left corner position of Node in Diagram coordinates
    """
    def __init__(self, node_type_name, content, grid, high_row, low_row, left_column, right_column, local_alignment):
        super().__init__(node_type_name, content, grid, local_alignment)
        assert high_row >= low_row >= 0, "Row span is negative"
        assert right_column >= left_column >= 0, "Column span is negative"
        self.High_row = high_row
        self.Low_row = low_row
        self.Left_column = left_column
        self.Right_column = right_column
        self.Position = self.Grid.place_spanning_node(self)


