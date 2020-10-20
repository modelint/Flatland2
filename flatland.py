"""
flatland.py – This is the Flatland main module
"""
import sys
from flatland_exceptions import FlatlandIOException
from collections import namedtuple
from model_parser import ModelParser
from layout_parser import LayoutParser
from flatlanddb import FlatlandDB
from canvas import Canvas
from single_cell_node import SingleCellNode
from straight_binary_connector import StraightBinaryConnector
from bending_binary_connector import BendingBinaryConnector
from connection_types import ConnectorName, OppositeFace, StemName
from command_interface import New_Stem
from text_block import TextBlock


def gen_diagram(args):
    """Generate a flatland diagram of the requested type"""
    # Parse the model
    try:
        model = ModelParser(model_file_path=args.model_file, debug=True)
    except FlatlandIOException as e:
        sys.exit(e)
    subsys = model.parse()

    # Parse the layout
    try:
        layout = LayoutParser(layout_file_path=args.layout_file, debug=True)
    except FlatlandIOException as e:
        sys.exit(e)
    layout = layout.parse()

    # Load the flatland database
    FlatlandDB()

    # Create a canvas
    lspec = layout.layout_spec
    flatland_canvas = Canvas(
        diagram_type=lspec.dtype,
        presentation=lspec.pres,
        notation=lspec.notation,
        standard_sheet_name=lspec.sheet,
        orientation=lspec.orientation,
        drawoutput=args.output_file,
        show_margin=True
    )

    # Draw all of the classes using subsys[1]
    classes = subsys[1]
    nodes = {}
    np = layout.node_placement
    for c in classes:
        nodes[c.name] = SingleCellNode(
            node_type_name='class',
            content=[ [ c.name ], c.attributes ],
            grid=flatland_canvas.Diagram.Grid,
            row=np[c.name][0], column=np[c.name][1]
        )
    # TODO:  Include method section in content
    # TODO:  Add support for axis offset on stem names

    rels = subsys[2]
    cp = layout.connector_placement
    for r in rels:  # r is the model data without any layout info
        rlayout = cp[r.rnum]  # How this r is to be laid out on the diagram
        # Straight or bent connector?
        tface = rlayout.t_data.face
        pface = rlayout.p_data.face
        t_phrase = StemName(
            text=TextBlock(r.rspec.t_side.phrase, wrap=rlayout.t_data.wrap),
            side=rlayout.t_data.name_side,
            axis_offset=None, end_offset=None
        )
        t_stem = New_Stem(stem_type='class mult', semantic=r.rspec.t_side.mult + ' mult',
                          node=nodes[r.rspec.t_side.cname], face=tface,
                          anchor=rlayout.t_data.anchor_at, stem_name=t_phrase)
        p_phrase = StemName(
            text=TextBlock(r.rspec.p_side.phrase, wrap=rlayout.p_data.wrap), side=rlayout.p_data.name_side,
            axis_offset=None, end_offset=None
        )
        p_stem = New_Stem(stem_type='class mult', semantic=r.rspec.p_side.mult + ' mult',
                          node=nodes[r.rspec.p_side.cname], face=pface,
                          anchor=rlayout.p_data.anchor_at, stem_name=p_phrase)
        rnum = ConnectorName(text=r.rnum, side=rlayout.name_side, bend=1)
        # TODO: Re-evaluate usage of bend parameter (is it needed?)
        if OppositeFace[tface] == pface:
            StraightBinaryConnector(
                diagram=flatland_canvas.Diagram,
                connector_type='binary association',
                projecting_stem=t_stem,
                floating_stem=p_stem,
                name=rnum
            )
            print("Straight connector")
        else:
            BendingBinaryConnector(
                diagram=flatland_canvas.Diagram,
                connector_type='binary association',
                anchored_stem_p=p_stem,
                anchored_stem_t=t_stem,
                paths=None,
                name=rnum)
            print("Bending connector")
        print()


    flatland_canvas.render()

    print("No problemo")

    # create the canvas
    # construct and execute each diagram element
    # render


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line

    layout_file_path = "Model Markup/test.mss"
    model_file_path = "Model Markup/test.xmm"
    output_file_path = ""

    DrawArgs = namedtuple("DrawArgs", "layout_file model_file output_file")

    test_input = DrawArgs(
        layout_file=layout_file_path,
        model_file=model_file_path,
        output_file="ftest.pdf"
    )
    gen_diagram(test_input)
