"""
t051_rbranch_vertical.py - Draw a vertical rut branch
"""

from canvas import Canvas
from single_cell_node import SingleCellNode
from names import NodeTypeName, StemTypeName, ConnectorTypeName
from notation import StemSemantic
from tree_connector import TreeConnector
from connection_types import NodeFace, Path, AnchorPosition

from command_interface import New_Stem, New_Branch_Set, New_Trunk_Branch


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
                                grid=flatland_canvas.Diagram.Grid, row=2, column=1)
    l1_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_B1,
                             grid=flatland_canvas.Diagram.Grid, row=3, column=4)
    l2_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_B2,
                             grid=flatland_canvas.Diagram.Grid, row=1, column=4)

    trunk_stem = New_Stem(stem_type=StemTypeName.gen_superclass, semantic=StemSemantic.Super_class, node=trunk_node,
                          face=NodeFace.RIGHT, anchor=AnchorPosition(0))
    leaf1_stem = New_Stem(stem_type=StemTypeName.gen_subclass, semantic=StemSemantic.Sub_class, node=l1_node,
                          face=NodeFace.LEFT, anchor=AnchorPosition(0))
    leaf2_stem = New_Stem(stem_type=StemTypeName.gen_subclass, semantic=StemSemantic.Sub_class, node=l2_node,
                          face=NodeFace.LEFT, anchor=AnchorPosition(0))

    trunk_branch = New_Trunk_Branch(
        trunk_stem=trunk_stem,
        leaf_stems={leaf1_stem, leaf2_stem},
        graft=None, path=Path(lane=3, rut=1), floating_leaf_stem=None
    )
    branches = New_Branch_Set(trunk_branch=trunk_branch, offshoot_branches=[])

    TreeConnector(diagram=flatland_canvas.Diagram, connector_type=ConnectorTypeName.gen, branches=branches)

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
