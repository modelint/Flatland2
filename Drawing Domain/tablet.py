"""
tablet.py – Flatland draws to this and then the tablet can be drawn using cairo or some other draw framework
"""
from draw_types import Text_Line, Text_Style, FontWeight, FontSlant, Color, StrokeStyle
from geometry_types import Rect_Size, Position
from typing import List
import cairo
from styledb import StyleDB
from collections import namedtuple

# These structures are intended for internal use only
# They each incoroporate style information with a more general geometric structure
# So that the Tablet can draw them in the correct presentation style
_Line_Segment = namedtuple('_Line_Segment', 'from_here to_there style')
_Rectangle = namedtuple('_Rectangle', 'upper_left size border_style')
_Text_line = namedtuple('_Text_line', 'lower_left text style')

# TODO: Make the Tablet a singleton with class based attributes and remove link from Canvas


class Tablet:
    """
    The Tablet class is part of the Drawing Domain which provides a service to the Flatland model
    diagram application. We can imagine a virtual Tablet that the application uses to draw
    all of its nodes and connectors and other model elements. The Tablet abstracts away the details
    of drawing and graphics library interaction from the fundamental Flatland application.

    For example, when a Flatland node compartment wants to draw itself, it doesn't worry about line
    widths, dash patterns and colors. It also doesn't worry about flipping to whatever coordinate
    system the graphics library uses. A compartment would just say "add_shape( asset, size, location )" and
    the Tablet will take care of the rest. Here the asset is the name of the model entity 'compartment',
    the size in points (or whatever units the Flatland app wants to use) and location expressed in Flatland
    Canvas coordinates.

    When a blank Flatland Canvas is created, it will initialize its underlying Tablet and select a predefined
    Drawing Type ('class diagram', 'state machine diagram' etc.) and Presentation Style ('default', 'formal',
    'diagnostic', etc).  The Diagram Type determines what kinds of things might be drawn, Assets such as 'connector',
    'compartment', 'class name', etc., while the Presentation Style establishes the Text and Line Styles to
    be used when drawing those Assets. All of this information is stored in a database which the Tablet
    loads upon creation.

    Each time the application wants something drawn, it will ask Tablet to add the appropriate Asset
    to one of its draw lists. A separate list is maintained for all the rectangles, line segments and
    text lines to be rendered. When the application is finished populating these lists, the Tablet can
    render everything using its graphic library, such as Cairo, using whatever coordinate system the
    library supplies, making any necessary conversions from the application coordinate system.

    Consequently, a new graphics library, such as NumPy for example, can be supported by updating the Drawing Domain
    and primarily the Tablet class without having to make any changes in the Flatland application. Futhermore, any
    changes to text styles, colors, line patterns etc can be perfomred by updating the Drawing Domain's style
    database.

    Attributes:
        Size : The size of the whatever surface (PDF, RGB, SVG, etc) Tablet supports.
        Line_segments : A list of geometric lines each with start and end coordinates.
        Rectangles : A list of rectangles each with a lower left corner, height and width
        Text : A list of text lines (new lines are not supported)
        Output_file : A filename or output stream object to be output as a drawing
        PDF_sheet : For now we only support PDF output as defined in Cairo.  So this is a Cairo surface
        Context : A Cairo context object for drawing on the PDF sheet
    """

    def __init__(self, size, output_file, drawing_type, presentation):
        """
        Constructs a new singleton Tablet instance
        :param size: Vertical and horizontal span of the entire draw surface in points
        :param output_file: Name of the drawing file to be generated, PDF only for now
        :param drawing_type: Type of drawing so we can determine what kinds of shapes and text will be drawn
        :param presentation: User selected Presentation Style so we know which styles to load from the database
        """

        # Load all of the draw styles from the flatland database
        # We only need to load the styles for the user selected Presentation Style and only for the Assets
        # that can be drawn in the given Drawing Type
        StyleDB(drawing_type=drawing_type, presentation=presentation)

        self.Drawing_type = drawing_type  # class diagram, state diagram, etc
        self.Presentation = presentation  # informal, sexy, etc
        self.Size = size
        self.Line_segments: List[_Line_Segment] = []
        self.Rectangles: List[_Rectangle] = []
        self.Text: List[_Text_line] = []
        self.Output_file = output_file
        self.PDF_sheet = cairo.PDFSurface(self.Output_file, self.Size.width, self.Size.height)
        self.Context = cairo.Context(self.PDF_sheet)

    def add_line_segment(self, asset: str, from_here:Position, to_there: Position):
        """
        Convert line segment coordinates to device coordinates and combine with the Line Style defined
        for the Asset in the selected Preentation Style
        :param asset:
        :param from_here:
        :param to_there:
        """
        self.Line_segments.append(_Line_Segment(
            from_here=self.to_dc(from_here), to_there=self.to_dc(to_there), style=StyleDB.shape_presentation[asset])
        )

    def add_rectangle(self, asset: str, lower_left: Position, size: Rect_Size):
        """
        Adds a rectangle to the tablet and converts the lower left corner to device coordinates
        """
        # Flip lower left corner to device coordinates
        ll_dc = Position(x=self.to_dc(lower_left.x), y=self.to_dc(lower_left.y))

        # Use upper left corner instead
        ul = Position(x=ll_dc.x, y=self.Size.height - ll_dc.lower_left.y - size.height)

        self.Rectangles.append(_Rectangle( upper_left=ul, size=size, border_style=StyleDB.shape_presentation[asset]))

    def add_text(self, asset: str, lower_left: Position, text: str):
        """
        Adds a line of text to the tablet at the specified lower left corner location which will be converted
        to device coordinates
        """
        self.Text.append(_Text_line(lower_left=Position(x=self.to_dc(lower_left.x), y=self.to_dc(lower_left.y)),
                                    text=text, style=StyleDB.text_presentation[asset]) )


    def render(self):
        """Renders the tablet using Cairo for now"""

        # For now, always assume output to cairo
        self.Context.set_line_join(cairo.LINE_JOIN_ROUND)
        for l in self.Line_segments:
            self.Context.set_dash(l.style.pattern)
            self.Context.set_source_rgb(*l.style.color)
            self.Context.set_line_width(l.style.width)
            self.Context.move_to(*l.from_here)
            self.Context.line_to(*l.to_there)
            self.Context.stroke()
        for r in self.Rectangles:
            self.Context.set_dash(r.border_style.pattern)
            self.Context.set_source_rgb(*r.border_style.color)
            self.Context.set_line_width(r.border_style.width)
            self.Context.rectangle(x=r.upper_left.x, y=r.upper_left.y, width=r.size.width, height=r.size.height)
            self.Context.stroke()
        for t in self.Text:
            self.Context.select_font_face(family=t.style.typeface, slant=t.style.slant, weight=t.style.weight)
            self.Context.set_font_size(t.style.size)
            self.Context.move_to(x=t.lower_left.x, y=self.Size.height - t.lower_left.y)
            self.Context.show_text(t.text)

    def text_size(self, asset: str, text_line: str) -> (Rect_Size, int):
        """
        Returns the size of a line of text when rendered with the asset's text style
        :param asset: Application entity to determine text style
        :param text_line: Text that would be rendered
        :return: Size of the text line ink area and the text style's leading value
        """
        style = StyleDB.text_presentation[asset] # Look up the text style for this asset
        # Configure the Cairo context with style properties and the text line
        self.Context.select_font_face( style.typeface, style.slant, style.weight )
        self.Context.set_font_size(style.size)
        te = self.Context.text_extents(text_line)
        return Rect_Size(height=te.height, width=te.width), style.leading

    def to_dc(self, tablet_coord: Position) -> Position:
        """
        To display coordinates – Convert tablet bottom_left origin coordinate to
        display coordinate where top-left origin is used.
        """
        assert (tablet_coord.y <= self.Size.height), "Tablet bounds exceeded"
        return Position(x=tablet_coord.x, y=self.Size.height - tablet_coord.y)

    def __repr__(self):
        return f'Tablet size: {self.Size}\nLine_segments:\n{self.Line_segments}\nRectangles:\n{self.Rectangles}\nText:\n{self.Text}'
