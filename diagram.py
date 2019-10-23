"""
diagram.py
"""
from layout_specification import default_diagram_origin
from diagram_node_types import diagram_types
from flatland_types import Position
from grid import Grid

default_diagram_type = 'class'


class Diagram:
    def __init__(self, canvas, diagram_type):
        self.Canvas = canvas
        self.Diagram_type = diagram_types.get(diagram_type, default_diagram_type)
        self.Grid = Grid(diagram=self)  # Start with an empty grid
        self.Origin = Position(  # Origin is in the bottom corner of the Canvas margin
            x=default_diagram_origin.x + self.Canvas.Margin.left,
            y=default_diagram_origin.y + self.Canvas.Margin.bottom
        )

    def render(self):
        self.Grid.render()

    def __repr__(self):
        return f'Diagram: {self.Diagram_type}'
