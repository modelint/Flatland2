"""
tablet.py – Flatland draws to this and then the tablet can be drawn using cairo or some other draw framework
"""
from flatland_types import Position, Line, Rectangle
from typing import List

class Tablet:
    def __init__(self, size, output_file):
        self.Size = size
        self.Lines:  List[Line] = []
        self.Rectangles: List[Rectangle] = []
        self.Text = []
        self.Output_file = output_file

    def render(self):
        """Renders the tablet using Cairo for now"""

        # For now, always assume output to cairo
        import cairo
        pdf_sheet = cairo.PDFSurface(self.Output_file, self.Size.width, self.Size.height)
        context = cairo.Context(pdf_sheet)
        context.set_source_rgb(0, 0, 0)
        context.set_line_join(cairo.LINE_JOIN_ROUND)
        for l in self.Lines:
            context.set_line_width(l.line_style.width.value)
            context.move_to(*self.to_dc(l.from_here))
            context.line_to(*self.to_dc(l.to_there))
            context.stroke()
        for r in self.Rectangles:
            context.set_line_width(r.line_style.width.value)
            # Invert y coordinate and use top left rather than bottom left origin
            context.rectangle(r.lower_left.x, self.Size.height - r.lower_left.y - r.size.height, r.size.width, r.size.height)
            context.stroke()

    def to_dc(self, tablet_coord):
        """
        To display coordinates – Convert tablet bottom_left origin coordinate to
        display coordinate where top-left origin is used.
        """
        assert (tablet_coord.y <= self.Size.height), "Tablet bounds exceeded"
        return Position(x=tablet_coord.x, y=self.Size.height - tablet_coord.y)

    def __repr__(self):
        return f'Tablet size: {self.Size}\nLines:\n{self.Lines}\nRectangles:\n{self.Rectangles}\nText:\n{self.Text}'