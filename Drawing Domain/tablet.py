"""
tablet.py – Flatland draws to this and then the tablet can be drawn using cairo or some other draw framework
"""
from draw_types import Line, Text_Line, Text_Style, FontWeight, FontSlant
from geometry_types import Rectangle, Rect_Size, Position
from typing import List
import cairo


class Tablet:
    """
    The Tablet class is not specified on the Flatland Class Diagram since it is at a different
    level of abstraction.  In Exexutable UML, we would say that Tablet is in another subject
    matter domain.

    Whereas the Flatland Class Diagram describes diagram layout, the Tablet
    class defines a mapping to a graphics framework. As such, it serves to isolate Flatland
    itself from the specifics of any particular graphics framework such as Cairo. For example,
    Flatland elements are specified in the upper right quadrant of an xy coordinate system.
    Cairo, uses display coordinates where y increments downward rather than upward. So Tablet
    converts from the Flatland coordinates to Cairo coordinates.  Also, text styles are defined
    in Flatland and then later mapped to whatever text display mechanisms are supported by a
    particular graphics framework.


    Consequently, a new framework can be supported by updating the Tablet class without affecting any
    of the Flatland classes.

    When flatland elements render themselves they create text, lines and rectangles on the Tablet
    in flatland coordinates. Once complete, the tablet renders these using coordinates and functions
    specific to a particular graphics framework such as Cairo.

    Attributes
    ---
    Size : The size of the whatever surface (PDF, RGB, SVG, etc) Tablet supports.
    Lines : A list of geometric lines each with start and end coordinates.
    Rectangles : A list of rectangles each with a lower left corner, height and width
    Text : A list of text lines (new lines are not supported)
    Output_file : A filename or output stream object to be output as a drawing
    PDF_sheet : For now we only support PDF output as defined in Cairo.  So this is a Cairo surface
    Context : A Cairo context object for drawing on the PDF sheet
    Font_weight_map : Translates Flatland font weight enums to Cairo enums
    Font_slant_map : Translates Flatland font slant enums to Cairo enums
    """
    def __init__(self, size, output_file):
        self.Size = size
        self.Lines: List[Line] = []
        self.Rectangles: List[Rectangle] = []
        self.Text: List[Text_Line] = []
        self.Output_file = output_file
        self.PDF_sheet = cairo.PDFSurface(self.Output_file, self.Size.width, self.Size.height)
        self.Context = cairo.Context(self.PDF_sheet)
        self.Font_weight_map = {FontWeight.NORMAL: cairo.FontWeight.NORMAL, FontWeight.BOLD: cairo.FontWeight.BOLD}
        self.Font_slant_map = {FontSlant.NORMAL: cairo.FontSlant.NORMAL, FontSlant.ITALIC: cairo.FontSlant.ITALIC}

    def render(self):
        """Renders the tablet using Cairo for now"""

        # For now, always assume output to cairo
        self.Context.set_source_rgb(0, 0, 0)
        self.Context.set_line_join(cairo.LINE_JOIN_ROUND)
        for l in self.Lines:
            self.Context.set_line_width(l.line_style.width.value)
            self.Context.move_to(*self.to_dc(l.from_here))
            self.Context.line_to(*self.to_dc(l.to_there))
            self.Context.stroke()
        for r in self.Rectangles:
            self.Context.set_line_width(r.line_style.width.value)
            # Invert y coordinate and use top left rather than bottom left origin
            self.Context.rectangle(r.lower_left.x, self.Size.height - r.lower_left.y - r.size.height,
                                   r.size.width, r.size.height)
            self.Context.stroke()
        for t in self.Text:
            self.Context.select_font_face(
                t.style.typeface.value,
                self.Font_slant_map[t.style.slant],
                self.Font_weight_map[t.style.weight]
            )
            self.Context.set_font_size(t.style.size)
            self.Context.move_to(t.lower_left.x, self.Size.height - t.lower_left.y)
            self.Context.show_text(t.content)

    def text_size(self, style: Text_Style, text_line):
        """Returns the size of a line of text if displayed"""
        # We map flatland values to cairo values to set the desired text style
        self.Context.select_font_face(
            style.typeface.value,
            self.Font_slant_map[style.slant],
            self.Font_weight_map[style.weight]
        )
        self.Context.set_font_size(style.size)
        te = self.Context.text_extents(text_line)
        return Rect_Size(height=te.height, width=te.width)

    def to_dc(self, tablet_coord):
        """
        To display coordinates – Convert tablet bottom_left origin coordinate to
        display coordinate where top-left origin is used.
        """
        #print(f'tc: {tablet_coord}')
        #print(f'to_dc x: {tablet_coord.x}, y: {tablet_coord.y}')
        assert (tablet_coord.y <= self.Size.height), "Tablet bounds exceeded"
        return Position(x=tablet_coord.x, y=self.Size.height - tablet_coord.y)

    def __repr__(self):
        return f'Tablet size: {self.Size}\nLines:\n{self.Lines}\nRectangles:\n{self.Rectangles}\nText:\n{self.Text}'
