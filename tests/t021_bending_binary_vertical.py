"""
t021_bending_binary_vertical.py
"""
from collections import namedtuple
from canvas import Canvas
from single_cell_node import SingleCellNode
from names import NodeTypeName, StemTypeName
from notation import StemSemantic
from bending_binary_connector import BendingBinaryConnector
from connection_types import NodeFace, AnchorPosition
from command_interface import New_Stem, New_Path


# For diagnostics during development
def create_canvas(args):
    """Create a canvas using the arguments supplied in the call to Flatland"""
    # These args could come from the command line or be supplied directly in
    # this file for diagnostic purposes
    flatland_canvas = Canvas(
        diagram_type=args.diagram,
        notation=args.notation,
        standard_sheet_name=args.sheet,
        orientation=args.orientation,
        drawoutput=args.file,
        show_margin=True
    )

    # Until markup parsing is supported, we will provide test data by hand crafting
    # the parsed output
    class_Aircraft = [
        ['Aircraft'], [
            'Altitude',
            'Tail number: ACAO {I}',
            'Airspeed : Knots',
            'Heading'
        ]
    ]
    class_Pilot = [
        ['Pilot'], [
            'ID : Pilot ID {I}',
            'Name : Call Sign',
            'Experience : Hours',
            'Aircraft {R13}'
        ]
    ]

    t_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_Aircraft,
                            grid=flatland_canvas.Diagram.Grid,
                            row=1, column=1)
    p_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_Pilot, grid=flatland_canvas.Diagram.Grid,
                            row=3, column=1)

    t_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc, node=t_node,
                      face=NodeFace.RIGHT, anchor=AnchorPosition(0))
    p_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1, node=p_node,
                      face=NodeFace.RIGHT, anchor=AnchorPosition(0))
    p = [New_Path(lane=2, rut=0)]

    BendingBinaryConnector(diagram=flatland_canvas.Diagram, anchored_stem_p=p_stem, anchored_stem_t=t_stem, paths=p)
    flatland_canvas.render()


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line
    from collections import namedtuple

    Canvas_Args = namedtuple("Canvas_Args", "diagram notation sheet orientation file")

    test_input = Canvas_Args(
        diagram="class", notation="xUML", sheet="letter", orientation="landscape", file="ftest.pdf")
    create_canvas(args=test_input)
