"""
t055_p2_three_branch_one_graft.py
"""
from single_cell_node import SingleCellNode
from tree_connector import TreeConnector
from connection_types import NodeFace, AnchorPosition, Path, ConnectorName
from command_interface import New_Stem, New_Branch_Set, New_Trunk_Branch, New_Offshoot_Branch
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

    class_B3 = [
        ['Hybrid Wing'], [
            'Aircraft {I, R1}',
            'Pilot  {I2, R1}',
            'Flight time : Duration'
        ]
    ]

    trunk_node = SingleCellNode(node_type_name='class', content=class_Trunk,
                                grid=flatland_canvas.Diagram.Grid, row=3, column=2)
    l1_node = SingleCellNode(node_type_name='class', content=class_B1,
                             grid=flatland_canvas.Diagram.Grid, row=1, column=1)
    l2_node = SingleCellNode(node_type_name='class', content=class_B2,
                             grid=flatland_canvas.Diagram.Grid, row=3, column=4)
    l3_node = SingleCellNode(node_type_name='class', content=class_B3,
                             grid=flatland_canvas.Diagram.Grid, row=4, column=4)
    l4_node = SingleCellNode(node_type_name='class', content=class_B3,
                             grid=flatland_canvas.Diagram.Grid, row=6, column=2)
    l5_node = SingleCellNode(node_type_name='class', content=class_B2,
                             grid=flatland_canvas.Diagram.Grid, row=5, column=1)

    trunk_stem = New_Stem(stem_type='superclass', semantic='superclass', node=trunk_node,
                          face=NodeFace.BOTTOM, anchor=AnchorPosition(0), stem_name=None)
    leaf1_stem = New_Stem(stem_type='subclass', semantic='subclass', node=l1_node,
                          face=NodeFace.TOP, anchor=AnchorPosition(0), stem_name=None)
    leaf2_stem = New_Stem(stem_type='subclass', semantic='subclass', node=l2_node,
                          face=NodeFace.LEFT, anchor=AnchorPosition(0), stem_name=None)
    leaf3_stem = New_Stem(stem_type='subclass', semantic='subclass', node=l3_node,
                          face=NodeFace.LEFT, anchor=AnchorPosition(0), stem_name=None)
    leaf4_stem = New_Stem(stem_type='subclass', semantic='subclass', node=l4_node,
                          face=NodeFace.BOTTOM, anchor=AnchorPosition(0), stem_name=None)
    leaf5_stem = New_Stem(stem_type='subclass', semantic='subclass', node=l5_node,
                          face=NodeFace.BOTTOM, anchor=AnchorPosition(0), stem_name=None)

    br1 = New_Trunk_Branch(
        trunk_stem=trunk_stem,
        leaf_stems={leaf1_stem},
        graft=None, path=None, floating_leaf_stem=None
    )
    br2 = New_Offshoot_Branch(
        leaf_stems={leaf2_stem},
        graft=None, path=Path(lane=3, rut=-1), floating_leaf_stem=None
    )
    br3 = New_Offshoot_Branch(
        leaf_stems={leaf3_stem, leaf4_stem, leaf5_stem},
        graft=leaf3_stem, path=None, floating_leaf_stem=None
    )

    branches = New_Branch_Set(trunk_branch=br1, offshoot_branches=[br2, br3])

    rnum = ConnectorName(text='R1', side=-1, bend=None)
    TreeConnector(diagram=flatland_canvas.Diagram, connector_type='generalization', branches=branches, name=rnum)

    flatland_canvas.render()


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line
    from collections import namedtuple

    Canvas_Args = namedtuple("Canvas_Args", "diagram notation presentation sheet orientation file")

    test_input = Canvas_Args(
        diagram="class", notation="Starr", presentation="default", sheet="letter",
        orientation="landscape", file="../ftest.pdf"
    )
    create_canvas(args=test_input)
