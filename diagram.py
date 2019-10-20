"""
diagram.py
"""
from diagram_node_types import diagram_types
from grid import Grid

default_diagram_type = 'class'


class Diagram:
    def __init__(self, canvas, diagram_type):
        self.Canvas = canvas
        self.Diagram_type = diagram_types.get(diagram_type, default_diagram_type)
        self.Grid = Grid(diagram=self)  # Start with an empty grid

    def render(self):
        self.Grid.render()

    def __repr__(self):
        return f'Diagram: {self.Diagram_type}'
