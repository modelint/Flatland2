"""
node.py
"""
from diagram_specification import node_types
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
        cell_height = self.Grid.Heights[self.Row]
        cell_width = self.Grid.Widths[self.Column]
        self.Grid.Diagram.Canvas.Tablet.Rectangles.append()
