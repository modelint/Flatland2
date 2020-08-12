""" compartment.py """

from geometry_types import Rect_Size, Position
from typing import TYPE_CHECKING, List
from compartment_type import CompartmentType

if TYPE_CHECKING:
    from node import Node


class Compartment:
    """
    A rectangle filled with text inside of a Node

        Attributes

        - Name -- Compartment type name indicating overall purpose of compartment (Title, Attributes, Methods, etc)
        - Alignment -- Alignment of text block within the compartment
        - Padding -- Extra space between text block and Node boundary
        - Text style -- Font, size, etc of text
    """
    def __init__(self, node: 'Node', ctype: CompartmentType, content: List[str]):
        """
        Constructor

        :param node: Node reference - Compartment is inside this Node
        :param ctype: Compartment Type referende - Specifies layout and stack order of this Compartment
        :param content: Text block a list of text lines to be rendered inside this Compartment
        """
        self.Type = ctype
        self.Node = node
        self.Content = content  # list of text lines
        self.Line_height = None  # Unknown until Text block size computed
        self.Leading = None  # Unknown until Text block size computed

    @property
    def Text_block_size(self):
        """Compute the size of the text block with required internal compartment padding"""
        tablet = self.Node.Grid.Diagram.Canvas.Tablet
        longest_line = max(self.Content, key=len)
        # Have the tablet compute the total ink area given the text style
        line_ink_area, leading = tablet.text_size(asset=self.Type.Name, text_line=longest_line)

        self.Line_height = line_ink_area.height
        self.Leading = leading

        block_width = line_ink_area.width + self.Type.Padding.left + self.Type.Padding.right
        block_height = ((line_ink_area.height + leading) * len(self.Content)
                        + self.Type.Padding.top + self.Type.Padding.bottom)
        # Now add the padding specified for this compartment type
        return Rect_Size(width=block_width, height=block_height)

    @property
    def Size(self):
        """Compute the size of the visible border"""
        # Width matches the node width and the height is the full text block size
        return Rect_Size(width=self.Node.Size.width, height=self.Text_block_size.height)

    def render(self, lower_left_corner: Position):
        """Create rectangle on the tablet and add each line of text"""
        tablet = self.Node.Grid.Diagram.Canvas.Tablet
        tablet.add_rectangle(asset=self.Node.Node_type.Name+' compartment', lower_left=lower_left_corner, size=self.Size)

        # Append each line of text into the tablet text list
        # TODO: Add text block capability to the tablet
        assert self.Line_height  # It should have been set by now
        ypos = lower_left_corner.y + self.Type.Padding.bottom
        xpos = lower_left_corner.x + self.Type.Padding.left
        for line in self.Content[::-1]:  # Reverse order since we are positioning lines from the bottom up
            tablet.add_text(asset=self.Type.Name, lower_left=Position(xpos, ypos), text=line)
            ypos += self.Leading + self.Line_height
