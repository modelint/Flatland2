"""
canvas.py

This is the Flatland (and not the cairo) Canvas class
"""
import sys
import sheet
from geometry_types import Padding, Alignment, Rect_Size, Position, Rectangle
from draw_types import Stroke, StrokeStyle, StrokeWidth, Color
from sheet import us_sheet_sizes, int_sheet_sizes, default_us_sheet
from diagram import Diagram
from tablet import Tablet

# All sheet and canvas related constants are kept together here for easy review and editing
points_in_cm = 28.3465
points_in_inch = 72
default_canvas_margin = Padding(top=10, bottom=10, left=10, right=10)
global_alignment = Alignment(vertical='center', horizontal='center')


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

    def __init__(self, db, diagram_type, notation, standard_sheet_name, orientation,
                 drawoutput=sys.stdout.buffer, show_margin=False):
        self.Database = db
        self.Sheet_name = standard_sheet_name
        self.Orientation = orientation
        sheet.load_sizes()
        self.Size = us_sheet_sizes.get(standard_sheet_name)
        if self.Size:
            factor = points_in_inch
        else:
            self.Size = int_sheet_sizes.get(standard_sheet_name, us_sheet_sizes[default_us_sheet])
            factor = points_in_cm
        # Set point size height and width based on portrait vs. landscape orientation
        h, w = (self.Size[0], self.Size[1]) if self.Orientation == 'portrait' else (self.Size[1], self.Size[0])
        self.Point_size = Rect_Size(height=int(h * factor), width=int(w * factor))
        self.Margin = default_canvas_margin
        self.Diagram = Diagram(self, diagram_type, notation)
        self.Notation = notation
        self.Tablet = Tablet(size=self.Point_size, output_file=drawoutput)
        self.Show_margin = show_margin

    def render(self):
        """Draw all content of this Canvas onto the framework independent Tablet"""
        if self.Show_margin:
            # Draw a thin rectangle to represent the margin boundary
            drawable_origin = Position(x=self.Margin.left, y=self.Margin.bottom)
            draw_area_height = self.Point_size.height - self.Margin.top - self.Margin.bottom
            draw_area_width = self.Point_size.width - self.Margin.left - self.Margin.right
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
        return f'Sheet: {self.Sheet_name} W{self.Size.width} x H{self.Size.height} Orientation: {self.Orientation} ' \
            f'Points: H{self.Point_size.height} x W{self.Point_size.width} {self.Margin}'
