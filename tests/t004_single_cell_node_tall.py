"""
t004_single_cell_node_tall.py
"""
from single_cell_node import SingleCellNode
from command_interface import New_Stem
from canvas import Canvas

from flatlanddb import FlatlandDB

FlatlandDB()


# For diagnostics during development
def create_canvas(args):
    """Create a canvas using the arguments supplied in the call to Flatland"""
    # These args could come from the command line or be supplied directly in
    # this file for diagnostic purposes
    flatland_canvas = Canvas(
        diagram_type=args.diagram,
        presentation=args.presentation,
        notation=args.notation,
        standard_sheet_name=args.sheet,
        orientation=args.orientation,
        drawoutput=args.file,
        show_margin=True
    )

    # Let's just draw a tall class (with many attributes) to check sizing and padding
    # as a single cell node
    class_Diagram = [
        ['Diagram'], ['ID : Nominal {I}', 'Grid {R10}', 'Type {R11, R30}', 'Notation {R30}',
                       'Canvas {R14}', 'Size : Rect Size', 'Origin : Position', 'Presentation style {R26}']
    ]

    t_node = SingleCellNode(node_type_name='class', content=class_Diagram, grid=flatland_canvas.Diagram.Grid,
                            row=1, column=1)

    flatland_canvas.render()


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line
    from collections import namedtuple

    Canvas_Args = namedtuple("Canvas_Args", "diagram notation presentation sheet orientation file")

    test_input = Canvas_Args(
        diagram="class", notation="Starr", presentation="diagnostic", sheet="letter",
        orientation="landscape", file="ftest.pdf"
    )
    create_canvas(args=test_input)
