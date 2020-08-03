""" compartment.py """

from geometry_types import Rect_Size, Position, Rectangle, Alignment, Padding
from draw_types import Text_Line
from typing import TYPE_CHECKING, List, Dict
from compartment_type import CompartmentType

if TYPE_CHECKING:
    from node import Node


class Compartment:
    """
    A rectangle filled with text inside of a Node

    Attributes
    ---
    Name - Compartment type name indicating overall purpose of compartment (Title, Attributes, Methods, etc)
    Alignment - Alignment of text block within the compartment
    Padding - Extra space between text block and Node boundary
    Text style - Font, size, etc of text
    """

    def __init__(self, node: 'Node', ctype_data: Dict, content: List[str]):
        #
        self.Name = ctype_data['Name']
        self.Alignment = Alignment(
            vertical=ctype_data['Vertical alignment'], horizontal=ctype_data['Horizontal_alignment'])
        self.Padding = Padding(
            top=ctype_data['Pad top'], bottom=ctype_data['Pad bottom'],
            right=ctype_data['Pad right'], left=ctype_data['Pad left']
        )
        self.Text_style = ctype_data['Text style']
        self.Node = node
        self.Type = CompartmentType(ctype_data)
        # self.Type: Compartment_Type_Attrs = self.Node.Node_type.compartments[self.Name]
        self.Content = content  # list of text lines
        self.leading = 4  # Temporary default leading in points ( change later to be font specific
        self.Line_height = None  # Unknown until Text block size computed

    @property
    def Text_block_size(self):
        """ Compute the size of the text block with required internal compartment padding """
        longest_line = max(self.Content, key=len)
        # Have the tablet compute the total ink area given the text style
        line_ink_area: Rect_Size = self.Node.Grid.Diagram.Canvas.Tablet.text_size(
            style=self.Type.text_style, text_line=longest_line)

        self.Line_height = line_ink_area.height

        block_width = line_ink_area.width + self.Type.padding.left + self.Type.padding.right
        block_height = ((line_ink_area.height + self.leading) * len(self.Content)
                        + self.Type.padding.top + self.Type.padding.bottom)
        # Now add the padding specified for this compartment type
        return Rect_Size(width=block_width, height=block_height)

    @property
    def Size(self):
        """Compute the size of the visible border"""
        # Width matches the node width and the height is the full text block size
        return Rect_Size(width=self.Node.Size.width, height=self.Text_block_size.height)

    def render(self, lower_left_corner: Position):
        """ Create rectangle on the tablet and add each line of text"""

        self.Node.Grid.Diagram.Canvas.Tablet.Rectangles.append(
            Rectangle(line_style=self.Node.Node_type.line_style, lower_left=lower_left_corner,
                      size=self.Size)
        )
        # Append each line of text into the tablet text list
        assert self.Line_height # It should have been set by now
        ypos = lower_left_corner.y + self.Type.padding.bottom
        xpos = lower_left_corner.x + self.Type.padding.left
        for line in self.Content[::-1]:  # Reverse order since we are positioning lines from the bottom up
            self.Node.Grid.Diagram.Canvas.Tablet.Text.append(Text_Line(
                lower_left=Position(xpos, ypos), content=line, style=self.Type.text_style))
            ypos += self.leading + self.Line_height
