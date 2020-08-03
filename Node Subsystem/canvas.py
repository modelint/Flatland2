"""
canvas.py

This is the Flatland (and not the cairo) Canvas class
"""
import sys
from diagram_layout_specification import DiagramLayoutSpecification as diagram_layout
from connector_layout_specification import ConnectorLayoutSpecification as connector_layout
from geometry_types import , Rect_Size, Position, Rectangle
from draw_types import Stroke, StrokeStyle, StrokeWidth, Color
from diagram import Diagram
from tablet import Tablet
from sheet import Sheet

# All sheet and canvas related constants are kept together here for easy review and editing
points_in_cm = 28.3465
points_in_inch = 72


class Canvas:
    """
    You can think of a Canvas as a sheet of paper, typically, not necessarily of a standard size
    such as A1, Tabloid or 8.5 x 11. It represents the total space where any drawing may occur.
    Typically, though, a margin is specified to preserve empty space along the edges of the Canvas.
    The margin can be set to zero all the way around if desired.

    Attributes
    ---
    Sheet_name : A standard name such as letter and tabloid in the US or A2 in Europe to describe sheet size
    Orientation: portrait or landscape
    Size : The size in US or Metric units as a simple tuple (height, width)
    Point_size : The size in points (required by Cairo) as a Rect_Size named tuple
    Margin : The default amount of space surrounding a Node in a Cell
    Diagram : Instance of Diagram drawn on this Canvas
    Tablet : This is a proxy for the graphics framework.  It is the only place in the code
        where the framework (such as Cairo) is referenced.  Consequently, we can easily swap
        to alternate graphic or web based display frameworks as necessary
    Show_margin : Draw the margin? For diagnostic purposes only

    """

    def __init__(self, diagram_type, notation, standard_sheet_name, orientation,
                 drawoutput=sys.stdout.buffer, show_margin=False):
        # Load layout specifications
        diagram_layout()
        connector_layout()

        self.Sheet = Sheet(standard_sheet_name)
        self.Orientation = orientation
        factor = points_in_inch if self.Sheet.Group == 'US' else points_in_cm

        # Set point size height and width based on portrait vs. landscape orientation
        h, w = (self.Sheet.Size.height, self.Sheet.Size.width) if self.Orientation == 'landscape' else (
            self.Sheet.Size.width, self.Sheet.Size.height)
        self.Size = Rect_Size(
            height=int(round(h * factor)),
            width=int(round(w * factor))
        )
        self.Margin = diagram_layout.Default_margin
        self.Diagram = Diagram(self, diagram_type, notation)
        self.Tablet = Tablet(size=self.Size, output_file=drawoutput)
        self.Show_margin = show_margin

    def render(self):
        """Draw all content of this Canvas onto the framework independent Tablet"""
        if self.Show_margin:
            # Draw a thin rectangle to represent the margin boundary
            drawable_origin = Position(x=self.Margin.left, y=self.Margin.bottom)
            draw_area_height = self.Size.height - self.Margin.top - self.Margin.bottom
            draw_area_width = self.Size.width - self.Margin.left - self.Margin.right
            draw_area_size = Rect_Size(height=draw_area_height, width=draw_area_width)
            self.Tablet.Rectangles.append(
                Rectangle(line_style=Stroke(width=StrokeWidth.THIN, color=Color.MARGIN_GOLD, pattern=StrokeStyle.SOLID),
                          lower_left=drawable_origin, size=draw_area_size)
            )
        # Now draw the diagram content
        self.Diagram.render()
        # Finally output the tablet to the target graphics framework
        self.Tablet.render()

    def __repr__(self):
        return f'Sheet: {self.Sheet}, Orientation: {self.Orientation}, '\
               f'Canvas size: h{self.Size.height} pt x w{self.Size.width} pt Margin: {self.Margin}'
