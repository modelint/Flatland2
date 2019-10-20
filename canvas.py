"""
canvas.py

This is not the flatland (and not the cairo) Canvas class
"""
import sys
from flatland_types import Padding, Alignment, Rect_Size
from diagram import Diagram
from tablet import Tablet

# All sheet and canvas related constants are kept together here for easy review and editing
us_sheet_sizes = {'letter': (8.5, 11), 'tabloid': (11, 17), 'C': (17, 22), 'D': (22, 34), 'E': (34, 44)}
euro_sheet_A_sizes = {'A4': (210, 297), 'A3': (297, 420), 'A2': (420, 594), 'A1': (594, 841)}
default_sheet = 'tabloid'
points_in_cm = 28.3465
points_in_inch = 72
global_padding = Padding(top=10, bottom=10, left=10, right=10)
global_alignment = Alignment(vertical='center', horizontal='center')


class Canvas:
    """
    A PDF sheet is represented as a Canvas. It represents the full writing surface.

    Attributes
    ---
    Sheet_name : A standard name such as letter and tabloid in the US or A2 in Europe to describe sheet size
    Orientation: portrait or landscape
    Size : The size in US or Metric units as a simple tuple (height, width)
    Point_size : The size in points (required by Cairo) as a Rect_Size named tuple
    Padding : The default amount of space surrounding a Node in a Cell
    Alignment : The default node alignment within a cell
    Diagram : Instance of Diagram drawn on this Canvas

    """

    def __init__(self,
                 diagram_type, standard_sheet_name=default_sheet, orientation='landscape',
                 drawoutput=sys.stdout.buffer):
        self.Sheet_name = standard_sheet_name
        self.Orientation = orientation
        self.Size = us_sheet_sizes.get(standard_sheet_name)
        if self.Size:
            factor = points_in_inch
        else:
            self.Size = euro_sheet_A_sizes.get(standard_sheet_name, us_sheet_sizes[default_sheet])
            factor = points_in_cm
        self.Point_size = Rect_Size(height=int(self.Size[1] * factor), width=int(self.Size[0] * factor))
        self.Padding = global_padding
        self.Alignment = global_alignment
        self.Diagram = Diagram(self, diagram_type)
        self.Tablet = Tablet(size=self.Point_size, output_file=drawoutput)

    def render(self):
        self.Tablet.render()


    def __repr__(self):
        return (
            f"""Canvas size {self.Sheet_name} (W{self.Size[0]} x H{self.Size[1]}) with orientation {self.Orientation}
        and point size {self.Point_size}
        using global padding: {self.Padding}
        using global alignment: {self.Alignment}""")
