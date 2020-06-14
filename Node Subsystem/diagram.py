"""
diagram.py
"""
import flatland_exceptions
from diagram_type import diagram_types
from geometry_types import Position, Padding, Rect_Size
from grid import Grid

default_diagram_type = 'class'


class Diagram:
    """
    The Diagram covers a rectangle within the area inside the Canvas margin.  Use padding to specify
    the extent and location of the diagram.  An origin and rectangle size will be derived from that
    for internal usage.

    Attributes
    ---

    Canvas : Drawn on this Canvas
    Diagram_type : Type of model diagram to be drawn, class, for example
    Notation: The supported notation used on this diagram
    Grid : All content in the diagram is organized within the cells of this Grid
    Padding : Space between Canvas margin and Diagram on all sides (useful for specification)
    Origin : Lower left corner of Diagram in Canvas coordinates
    Size : Size of the Diagram, derived from Padding also

    """
    def __init__(self, canvas, diagram_type, notation):
        self.Canvas = canvas
        self.Diagram_type = diagram_types.get(diagram_type, default_diagram_type)
        if notation in self.Diagram_type.notations:
            self.Notation = notation
        else:
            raise flatland_exceptions.UnsupportedNotation
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
