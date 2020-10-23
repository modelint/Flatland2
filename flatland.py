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
from geometry_types import Alignment, VertAlign, HorizAlign


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
        nlayout = np[c.name]
        nlayout['wrap'] = nlayout.get('wrap', 1)
        name_block = TextBlock(c.name, nlayout['wrap'])
        h = HorizAlign[nlayout.get('halign', 'CENTER')]
        v = VertAlign[nlayout.get('valign', 'CENTER')]
        nodes[c.name] = SingleCellNode(
            node_type_name='class',
            content=[ name_block.text, c.attributes ],
            grid=flatland_canvas.Diagram.Grid,
            row=nlayout['node_loc'][0], column=nlayout['node_loc'][1],
            local_alignment=Alignment(vertical=v, horizontal=h)
        )
    # TODO:  Include method section in content
    # TODO:  Add support for axis offset on stem names

    rels = subsys[2]
    if rels:
        cp = layout.connector_placement
        for r in rels:  # r is the model data without any layout info
            rlayout = cp[r.rnum]  # How this r is to be laid out on the diagram
            # Straight or bent connector?
            tstem = rlayout['tstem']
            pstem = rlayout['pstem']
            t_phrase = StemName(
                text=TextBlock(r.rspec.t_side.phrase, wrap=tstem['wrap']),
                side=tstem['stem_dir'], axis_offset=None, end_offset=None
            )
            t_stem = New_Stem(stem_type='class mult', semantic=r.rspec.t_side.mult + ' mult',
                              node=nodes[r.rspec.t_side.cname], face=tstem['face'],
                              anchor=tstem.get('anchor', 0), stem_name=t_phrase)
            p_phrase = StemName(
                text=TextBlock(r.rspec.p_side.phrase, wrap=pstem['wrap']),
                side=pstem['stem_dir'], axis_offset=None, end_offset=None
            )
            p_stem = New_Stem(stem_type='class mult', semantic=r.rspec.p_side.mult + ' mult',
                              node=nodes[r.rspec.p_side.cname], face=pstem['face'],
                              anchor=pstem.get('anchor', 0), stem_name=p_phrase)
            rnum = ConnectorName(text=r.rnum, side=rlayout['dir'], bend=rlayout.get('bend', 1))

            if OppositeFace[tstem['face']] == pstem['face']:
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
