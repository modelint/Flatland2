from collections import namedtuple

from canvas import Canvas
from single_cell_node import SingleCellNode
from names import NodeTypeName, StemTypeName
from notation import StemSemantic
from straight_binary_connector import StraightBinaryConnector
from bending_binary_connector import BendingBinaryConnector
from connection_types import NodeFace

# from spanning_node import SpanningNode
# from bend_route import Bend_Route, Bend
# from geometry_types import VertAlign, HorizAlign, Alignment

""" flatland_REF.py – 2D Model diagram generator

DESCRIPTION

Flatland is a 2D model diagram generator that takes flatland markup as input
and outputs a PDF sheet with a model diagram on it.

A variety of model diagrams are supported such as class, state, collaboration
and domain diagrams. There is no intention to support every type of model diagram.
Only certain kinds of diagrams lend themselves to a flexible grid style of layout.
But a wide variety of diagrams can be laid out this way.  You only need to specify
certainly properties of the Node Types and connections between them.

This program is created based on the Flatland Class Model. This model specifies the key
data, logic and constraints that apply to flatland diagrams. For example, the class model
specifies that a Cell may contain at most one Node. Comments in this program refer back to
the originating class model.

We will, in fact, use this program to draw the Flatland Class Model diagram! Since we did
not have the tool when the original diagram was created, it was drawn using OmniGraffle. But
subsequent versions will be autogenerated by this program. Consequently, the diagram provides
a nice, but not comprehensive, test case to run against this program.
"""

"""
OPEN SOURCE LICENSE

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Leon Starr"
__contact__ = "leon_starr@modelint.com"
__copyright__ = "Copyright 2019,2020, Leon Starr"
__date__ = "2020/6/16"
__deprecated__ = False
__email__ = "leon_starr@modelint.com"
__license__ = "GPLv3"
__maintainer__ = "Leon Starr"
__status__ = "Development"
__version__ = "0.4.0"

New_Stem = namedtuple('New_Stem', 'stem_type semantic node face anchor')
New_Path = namedtuple('New_Path', 'lane rut')


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

    class_Runway = [
        ['Runway'], [
            'ID : Runway Code {I}',
            'Length : Distance',
            'Width : Distance',
            'Something to make it really really long'
        ]
    ]

    class_Tower = [
        ['Tower'], [
            'ID : Nominal {I}',
            'A : Distance',
            'B : Distance',
            'C : Distance',
            'D : Distance',
            'E : Distance',
            'F : Distance',
            'G : Distance'
        ]
    ]
    t_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_Aircraft, grid=flatland_canvas.Diagram.Grid,
                        row=1, column=1)
    p_node = SingleCellNode(node_type_name=NodeTypeName.M_class, content=class_Pilot, grid=flatland_canvas.Diagram.Grid,
                        row=1, column=3)

    # t_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc, node=t_node,
    #                   face=NodeFace.RIGHT, anchor=-2)
    # p_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1, node=p_node,
    #                   face=NodeFace.LEFT, anchor=None)
    #
    t_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_Mc, node=t_node,
                      face=NodeFace.TOP, anchor=0)
    p_stem = New_Stem(stem_type=StemTypeName.class_mult, semantic=StemSemantic.Mult_1, node=p_node,
                      face=NodeFace.TOP, anchor=0)
    p = [ New_Path(lane=2, rut=0) ]

    BendingBinaryConnector(diagram=flatland_canvas.Diagram, anchored_stem_p=p_stem, anchored_stem_t=t_stem, paths=p)
    #
    # StraightBinaryConnector(diagram=flatland_canvas.Diagram, projecting_stem=t_stem, floating_stem=p_stem)

    # SpanningNode(node_type_name='class', content=class_Tower, grid=flatland_canvas.Diagram.Grid,
    #              high_row=2, low_row=1, left_column=1, right_column=2,
    #              local_alignment=Alignment(vertical=VertAlign.TOP, horizontal=HorizAlign.LEFT))
    # SingleCellNode(node_type_name='class', content=class_Runway, grid=flatland_canvas.Diagram.Grid,
    #                row=1, column=3)
    # SingleCellNode(node_type_name='class', content=class_Tower, grid=flatland_canvas.Diagram.Grid,
    #                row=2, column=2, local_alignment=Alignment(vertical=VertAlign.CENTER, horizontal=HorizAlign.CENTER))
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
