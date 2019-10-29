""" flatland.py – 2D Model diagram generator """

from canvas import Canvas


def create_canvas(args):
    flatland_canvas = Canvas(
        diagram_type=args.diagram,
        standard_sheet_name=args.sheet,
        orientation=args.orientation,
        drawoutput=args.file,
        show_margin=True
    )
    flatland_canvas.Diagram.Grid.place_node(
        row=1, column=2, node_type_name='class', content='Aircraft')
    flatland_canvas.render()


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line
    from collections import namedtuple
    Canvas_Args = namedtuple("Canvas_Args", "diagram sheet orientation file")

    test_input = Canvas_Args(
        diagram="class", sheet="tabloid", orientation="landscape", file="ftest.pdf")
    create_canvas(args=test_input)