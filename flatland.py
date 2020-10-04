"""
flatland.py – This is the Flatland main module
"""
import os
import sys
from flatland_exceptions import FlatlandIOException
from collections import namedtuple
from model_parser import ModelParser
from layout_parser import LayoutParser
from flatlanddb import FlatlandDB
from canvas import Canvas
from single_cell_node import SingleCellNode


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
    lspec = layout[0]
    flatland_canvas = Canvas(
        diagram_type=lspec['diagram'][0],
        presentation=lspec['presentation'][0],
        notation=lspec['notation'][0],
        standard_sheet_name=lspec['sheet'][0],
        orientation=lspec['orientation'][0],
        drawoutput=args.output_file,
        show_margin=True
    )

    # Draw all of the classes using subsys[1]
    # From layout, create dictionary of >> node_name : (row, col)
    cell_assignment = {n[0]: (int(n[1]), int(n[2])) for n in layout.node_placement}
    classes = subsys[1]
    nodes = {}
    for c in classes:
        nodes[c.name] = SingleCellNode(
            node_type_name='class',
            content=[ [ c.name ], c.attributes ],
            grid=flatland_canvas.Diagram.Grid,
            row=cell_assignment[c.name][0], column=cell_assignment[c.name][1]
        )
    # TODO:  Include method section in content

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
