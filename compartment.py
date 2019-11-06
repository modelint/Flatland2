""" compartment.py """

from flatland_types import Rect_Size, Compartment_Type_Attrs


class Compartment:
    """
    A rectangle filled with text inside of a Node

    Attributes
    ---

    """
    def __init__(self, node, name, content):
        self.Name = name
        self.Node = node
        self.Type : Compartment_Type_Attrs = self.Node.Node_type.compartments[self.Name]
        self.Content = content

    @property
    def Text_block_size(self):
        """ Compute the size of the text block with required internal compartment padding """
        # Have the tablet compute the total ink area given the text style
        text_ink_area : Rect_Size = self.Node.Grid.Diagram.Canvas.Tablet.text_size(
            style=self.Node.Node_type.text_style, text_block=self.Content)
        # Now add the padding specified for this compartment type
        return Rect_Size(width=text_ink_area.width + self.Type.padding.left + self.Type.padding.right,
                         height=text_ink_area.height + self.Type.padding.top + self.Type.padding.bottom)

