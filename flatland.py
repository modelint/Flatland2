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

    # FlatlandDB()  # Load the flatland database
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

    DrawArgs = namedtuple("DrawArgs", "layout_file model_file")

    test_input = DrawArgs(layout_file=layout_file_path, model_file=model_file_path)
    gen_diagram(test_input)
