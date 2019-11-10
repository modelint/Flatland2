"""
tablet.py – Flatland draws to this and then the tablet can be drawn using cairo or some other draw framework
"""
from flatland_types import *
from typing import List
import cairo


class Tablet:
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
        assert (tablet_coord.y <= self.Size.height), "Tablet bounds exceeded"
        return Position(x=tablet_coord.x, y=self.Size.height - tablet_coord.y)

    def __repr__(self):
        return f'Tablet size: {self.Size}\nLines:\n{self.Lines}\nRectangles:\n{self.Rectangles}\nText:\n{self.Text}'
