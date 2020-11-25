"""
t005_straight_binary_horiz_names.py
"""
from single_cell_node import SingleCellNode
from straight_binary_connector import StraightBinaryConnector
from connection_types import NodeFace, AnchorPosition, StemName, ConnectorName
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

    t_node = SingleCellNode(node_type_name='class', content=class_Aircraft, grid=flatland_canvas.Diagram.Grid,
                            row=1, column=1)
    p_node = SingleCellNode(node_type_name='class', content=class_Pilot, grid=flatland_canvas.Diagram.Grid,
                            row=1, column=3)

    t_phrase = StemName(text='is flying', axis_offset=None, end_offset=None)
    t_stem = New_Stem(stem_type='class mult', semantic='1 mult', node=t_node,
                      face=NodeFace.RIGHT, anchor=AnchorPosition(0), stem_name=t_phrase)

    p_phrase = StemName(text='is flown by', axis_offset=None, end_offset=None)
    p_stem = New_Stem(stem_type='class mult', semantic='1 mult', node=p_node,
                      face=NodeFace.LEFT, anchor=None, stem_name=p_phrase)

    rnum = ConnectorName(text='R1', side=1, bend=1)
    StraightBinaryConnector(diagram=flatland_canvas.Diagram, connector_type='binary association',
                            projecting_stem=t_stem, floating_stem=p_stem, name=rnum)

    flatland_canvas.render()


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line
    from collections import namedtuple

    Canvas_Args = namedtuple("Canvas_Args", "diagram notation presentation sheet orientation file")

    test_input = Canvas_Args(
        diagram="class", notation="Starr", presentation="diagnostic", sheet="letter",
        orientation="landscape", file="../ftest.pdf"
    )
    create_canvas(args=test_input)
