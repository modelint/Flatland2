"""
canvas.py

This is the Flatland (and not the cairo) Canvas class
"""
import sys
from flatland_exceptions import InvalidOrientation
from diagram_layout_specification import DiagramLayoutSpecification as diagram_layout
from connector_layout_specification import ConnectorLayoutSpecification as connector_layout
from geometry_types import Rect_Size, Position
from diagram import Diagram
from tablet import Tablet
from sheet import Sheet, Group

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

        - Sheet -- A standard name such as letter and tabloid in the US or A2 in Europe to describe sheet size
        - Orientation -- portrait or landscape
        - Size -- The size in points as a Rect_Size named tuple
        - Margin -- The default amount of space surrounding a Node in a Cell
        - Diagram -- Instance of Diagram drawn on this Canvas
        - Tablet -- This is a proxy for the underlying graphics drawing context
        - Show_margin -- Draw the margin? For diagnostic purposes only

    """

    def __init__(self, diagram_type: str, presentation: str, notation: str, standard_sheet_name: str, orientation: str,
                 drawoutput=sys.stdout.buffer, show_margin=False):
        """
        Constructor

        :param diagram_type: A supported type of model diagram such as class, state machine, collaboration
        :param presentation: A predefined set of style specifications such as default, diagnostic, fullcolor
        :param notation: A supported notation such as xUML, Starr, Shlaer-Mellor
        :param standard_sheet_name: A US or international printer sheet size such as A1, tabloid, letter
        :param orientation: portrait or landscape
        :param drawoutput: A standard IO binary object obtained from sys
        :param show_margin: For diagnostics, show the canvas margin in the drawn output
        """
        # Load layout specifications
        diagram_layout()
        connector_layout()

        self.Sheet = Sheet(standard_sheet_name)  # Ensure that the user has specified a known sheet size
        if orientation not in ('portrait', 'landscape'):
            raise InvalidOrientation(orientation)
        self.Orientation = orientation
        factor = points_in_inch if self.Sheet.Group == Group.US else points_in_cm

        # Set point size height and width based on portrait vs. landscape orientation
        h, w = (self.Sheet.Size.height, self.Sheet.Size.width) if self.Orientation == 'landscape' else (
            self.Sheet.Size.width, self.Sheet.Size.height)
        self.Size = Rect_Size(
            height=int(round(h * factor)),
            width=int(round(w * factor))
        )
        self.Margin = diagram_layout.Default_margin
        self.Diagram = Diagram(self, diagram_type, presentation, notation)
        self.Tablet = Tablet(
            size=self.Size, output_file=drawoutput, drawing_type=diagram_type+' diagram', presentation='default'
        )
        self.Show_margin = show_margin

    def render(self):
        """
        Draw all content of this Canvas onto the Tablet
        """
        if self.Show_margin:
            # Add the margin boundary rectangle to the Tablet
            # The margin rectangle represents the drawable area defined for our Canvas
            # and may be equal to or smaller than the Tablet area
            drawable_origin = Position(x=self.Margin.left, y=self.Margin.bottom)
            draw_area_height = self.Size.height - self.Margin.top - self.Margin.bottom
            draw_area_width = self.Size.width - self.Margin.left - self.Margin.right
            draw_area_size = Rect_Size(height=draw_area_height, width=draw_area_width)
            self.Tablet.add_rectangle('margin', lower_left=drawable_origin, size=draw_area_size)

        # Now add all Diagram content to the Tablet
        self.Diagram.render()

        # Draw all added content and output a PDF using whatever graphics library is configured in the Tablet
        self.Tablet.render()

    def __repr__(self):
        return f'Sheet: {self.Sheet}, Orientation: {self.Orientation}, '\
               f'Canvas size: h{self.Size.height} pt x w{self.Size.width} pt Margin: {self.Margin}'
