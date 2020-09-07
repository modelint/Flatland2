""" compartment.py """

from geometry_types import Rect_Size, Position
from typing import TYPE_CHECKING, List
from node_type import CompartmentType

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
    def Text_block_size(self) -> Rect_Size:
        """Compute the size of the text block with required internal compartment padding"""
        tablet = self.Node.Grid.Diagram.Canvas.Tablet
        unpadded_text_size = tablet.text_block_size(asset=self.Type.name, text_block=self.Content)

        padded_text_width = unpadded_text_size.width + self.Type.padding.left + self.Type.padding.right
        padded_text_height = unpadded_text_size.height + self.Type.padding.top + self.Type.padding.bottom
        # Now add the padding specified for this compartment type
        return Rect_Size(width=padded_text_width, height=padded_text_height)

    @property
    def Size(self) -> Rect_Size:
        """Compute the size of the visible border"""
        # Width matches the node width and the height is the full text block size
        return Rect_Size(width=self.Node.Size.width, height=self.Text_block_size.height)

    def render(self, lower_left_corner: Position):
        """Create rectangle on the tablet and add each line of text"""
        tablet = self.Node.Grid.Diagram.Canvas.Tablet
        tablet.add_rectangle(asset=self.Node.Node_type.Name+' compartment', lower_left=lower_left_corner, size=self.Size)
        text_position = Position(lower_left_corner.x + self.Type.padding.left,
                                 lower_left_corner.y + self.Type.padding.bottom)
        tablet.add_text_block(asset=self.Type.name, lower_left=text_position, text=self.Content)
