"""
t030_straight_binary_ternary.py
"""
from collections import namedtuple

from canvas import Canvas
from single_cell_node import SingleCellNode
from names import NodeTypeName, StemTypeName, ConnectorTypeName
from notation import StemSemantic
from hierachy_connector import HierarchyConnector
from connection_types import NodeFace

from command_interface import *


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
    class_Trunk = [
        ['Aircraft'], [
            'Altitude',
            'Tail number: ACAO {I}',
            'Airspeed : Knots',
            'Heading'
        ]
    ]
    class_B1 = [
        ['Helicopter'], [
            'ID : Pilot ID {I}',
            'Name : Call Sign',
            'Experience : Hours',
            'Aircraft {R13}'
        ]
    ]

    class_B2 = [
        ['Fixed Wing'], [
            'Aircraft {I, R1}',
            'Pilot  {I2, R1}',
            'Flight time : Duration'
        ]
    ]

    trunk_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_Trunk,
                                grid=flatland_canvas.Diagram.Grid, row=3, column=2)
    b1_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_B1,
                             grid=flatland_canvas.Diagram.Grid, row=1, column=1)
    b2_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_B2,
                             grid=flatland_canvas.Diagram.Grid, row=1, column=3)

    trunk_stem = New_Stem(stem_type=StemTypeName.gen_superclass, semantic=StemSemantic.Super_class, node=trunk_node,
                          face=NodeFace.BOTTOM, anchor=0)
    b1_stem = New_Stem(stem_type=StemTypeName.gen_subclass, semantic=StemSemantic.Sub_class, node=b1_node,
                       face=NodeFace.TOP, anchor=0)
    b2_stem = New_Stem(stem_type=StemTypeName.gen_subclass, semantic=StemSemantic.Sub_class, node=b2_node,
                       face=NodeFace.TOP, anchor=0)

    trunk_branch = New_Trunk_Branch(trunk_stem=trunk_stem, branch_stems={b1_stem, b2_stem}, graft=None, path=None)
    branches = New_Branch_Set(trunk_branch=trunk_branch, offshoot_branches=None)

    HierarchyConnector(diagram=flatland_canvas.Diagram, connector_type=ConnectorTypeName.gen, branches=branches)

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
