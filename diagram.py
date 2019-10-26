"""
diagram.py
"""
from layout_specification import default_diagram_origin
from diagram_node_types import diagram_types
from flatland_types import Position, Padding, Rect_Size
from grid import Grid

default_diagram_type = 'class'


class Diagram:
    """
    The Diagram covers the entire area of the Canvas inside the Canvas margin.

    """
    def __init__(self, canvas, diagram_type):
        self.Canvas = canvas
        self.Diagram_type = diagram_types.get(diagram_type, default_diagram_type)
        self.Grid = Grid(diagram=self)  # Start with an empty grid
        self.Padding = Padding(top=0, bottom=0, left=0, right=0)
        self.Origin = Position(
            x=self.Canvas.Margin.left + self.Padding.left,
            y=self.Canvas.Margin.bottom + self.Padding.bottom
        )
        self.Size = Rect_Size(
            width=self.Canvas.Point_size.width - self.Origin.x - self.Canvas.Margin.right,
            height=self.Canvas.Point_size.height - self.Origin.y - self.Canvas.Margin.top
        )

    def render(self):
        self.Grid.render()

    def __repr__(self):
        return f'Diagram: {self.Diagram_type}'
