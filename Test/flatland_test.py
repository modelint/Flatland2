"""
flatland_test.py – This is the Flatland test driver
"""
import sys
from flatland_exceptions import FlatlandIOException, ConflictingTreeLayoutGraft
from collections import namedtuple
from model_parser import ModelParser
from layout_parser import LayoutParser
from flatlanddb import FlatlandDB
from canvas import Canvas
from single_cell_node import SingleCellNode
from straight_binary_connector import StraightBinaryConnector
from bending_binary_connector import BendingBinaryConnector
from tree_connector import TreeConnector
from connection_types import ConnectorName, OppositeFace, StemName
from command_interface import New_Stem, New_Path, New_Trunk_Branch, New_Offshoot_Branch, New_Branch_Set
from text_block import TextBlock
from geometry_types import Alignment, VertAlign, HorizAlign
from pathlib import Path


def layout_generalization(diagram, nodes, rnum, generalization, tree_layout):
    super_name = generalization['superclass']
    trunk_node = nodes[super_name]
    trunk_layout = tree_layout['trunk_face']

    # Process trunk branch
    trunk_stem = New_Stem(stem_type='superclass', semantic='superclass', node=trunk_node,
                          face=trunk_layout['face'], anchor=trunk_layout['anchor'], stem_name=None)
    tbranch = tree_layout['branches'][0]  # First branch is required and it is the trunk branch
    lfaces = tbranch['leaf_faces']
    path_fields = tbranch.get('path', None)
    tbranch_path = None if not path_fields else New_Path(**path_fields)
    leaf_stems = set()
    graft = trunk_stem if trunk_layout['graft'] else None
    local_leaf_graft = None
    next_branch_graft = None
    floating_leaf_stem = None
    for name in lfaces.keys():
        leaf_stems.add(New_Stem(stem_type='subclass', semantic='subclass', node=nodes[name],
                                      face=lfaces[name]['face'], anchor=lfaces[name]['anchor'],
                                      stem_name=None))
        if lfaces[name]['graft'] == 'local':
            if tbranch['graft']:
                raise ConflictingTreeLayoutGraft(stem=lfaces[name])
            else:
                local_leaf_graft = leaf_stems[name]
        elif lfaces[name]['graft'] == 'next':
            next_branch_graft = leaf_stems[name]
    graft = graft if graft else local_leaf_graft if local_leaf_graft else None
    trunk_branch = New_Trunk_Branch(
        trunk_stem=trunk_stem, leaf_stems=leaf_stems,
        graft=graft, path=tbranch_path, floating_leaf_stem=floating_leaf_stem
    )
    pass
    # for branch in trunk_layout['branches'][1:]:
    #     lfaces = branch['leaf faces']
    #     path_fields = branch.get('path', None)
    #     leaf_stems = {}
    #     leaf_graft = {}
    #     for name in lfaces.keys():
    #         leaf_stems['name'] = New_Stem(stem_type='subclass', semantic='subclass', node=nodes[name],
    #                            face=lfaces[name]['face'], anchor=lfaces[name]['anchor'],
    #                            stem_name=None)
    #     path = None if not path_fields else New_Path(**path_fields)
    #     graft = None



    branches = New_Branch_Set(trunk_branch=trunk_branch, offshoot_branches=[])
    rnum_data = ConnectorName(text=rnum, side=tree_layout['dir'], bend=None)
    TreeConnector(diagram=diagram, connector_type='generalization', branches=branches, name=rnum_data)


def layout_association(diagram, nodes, rnum, association, binary_layout):
    # Straight or bent connector?
    tstem = binary_layout['tstem']
    pstem = binary_layout['pstem']
    astem = binary_layout.get('tertiary_node', None)
    t_side = association['t_side']
    t_phrase = StemName(
        text=TextBlock(t_side['phrase'], wrap=tstem['wrap']),
        side=tstem['stem_dir'], axis_offset=None, end_offset=None
    )
    t_stem = New_Stem(stem_type='class mult', semantic=t_side['mult'] + ' mult',
                      node=nodes[t_side['cname']], face=tstem['face'],
                      anchor=tstem.get('anchor', None), stem_name=t_phrase)
    p_side = association['p_side']
    p_phrase = StemName(
        text=TextBlock(p_side['phrase'], wrap=pstem['wrap']),
        side=pstem['stem_dir'], axis_offset=None, end_offset=None
    )
    p_stem = New_Stem(stem_type='class mult', semantic=p_side['mult'] + ' mult',
                      node=nodes[p_side['cname']], face=pstem['face'],
                      anchor=pstem.get('anchor', None), stem_name=p_phrase)
    if astem:
        a_stem = New_Stem(stem_type='associative mult', semantic=association['assoc_mult'] + ' mult',
                          node=nodes[association['assoc_cname']], face=astem['face'], anchor=astem.get('anchor', None),
                          stem_name=None)
    else:
        a_stem = None
    rnum_data = ConnectorName(text=rnum, side=binary_layout['dir'], bend=binary_layout.get('bend', 1))

    paths = None if not binary_layout.get('paths', None) else \
        [New_Path(lane=p['lane'], rut=p['rut']) for p in binary_layout['paths']]

    if not paths and OppositeFace[tstem['face']] == pstem['face']:
        StraightBinaryConnector(
            diagram=diagram,
            connector_type='binary association',
            t_stem=t_stem,
            p_stem=p_stem,
            tertiary_stem=a_stem,
            name=rnum_data
        )
        print("Straight connector")
    else:
        BendingBinaryConnector(
            diagram=diagram,
            connector_type='binary association',
            anchored_stem_p=p_stem,
            anchored_stem_t=t_stem,
            tertiary_stem=a_stem,
            paths=paths,
            name=rnum_data)
        print("Bending connector")
    print()


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
    nodes = {}
    np = layout.node_placement
    for c in subsys.classes:
        cname = c['name']
        nlayout = np[cname]
        nlayout['wrap'] = nlayout.get('wrap', 1)
        name_block = TextBlock(cname, nlayout['wrap'])
        h = HorizAlign[nlayout.get('halign', 'CENTER')]
        v = VertAlign[nlayout.get('valign', 'CENTER')]
        nodes[cname] = SingleCellNode(
            node_type_name='class',
            content=[name_block.text, c['attributes']],
            grid=flatland_canvas.Diagram.Grid,
            row=nlayout['node_loc'][0], column=nlayout['node_loc'][1],
            local_alignment=Alignment(vertical=v, horizontal=h)
        )
    # TODO:  Include method section in content
    # TODO:  Add support for axis offset on stem names

    if subsys.rels:
        cp = layout.connector_placement
        for r in subsys.rels:  # r is the model data without any layout info
            rnum = r['rnum']
            rlayout = cp[rnum]  # How this r is to be laid out on the diagram
            if 'superclass' in r.keys():
                layout_generalization(diagram=flatland_canvas.Diagram,
                                      nodes=nodes, rnum=rnum, generalization=r, tree_layout=rlayout)
            else:
                layout_association(diagram=flatland_canvas.Diagram,
                                   nodes=nodes, rnum=rnum, association=r, binary_layout=rlayout)

    flatland_canvas.render()
    print("No problemo")

    # create the canvas
    # construct and execute each diagram element
    # render


if __name__ == "__main__":
    # Was not called from the command line, so we are in diagnostic mode
    # so we supply some test input arg values and call the same top level
    # function that is called from the command line

    tests = {
        't001': ('aircraft2', 't001_straight_binary_horiz'),
        't020': ('aircraft2', 't020_bending_binary_horiz'),
        't023': ('aircraft2', 't023_bending_binary_twice'),
        't030': ('aircraft3', 't030_straight_binary_tertiary'),
        't031': ('aircraft3', 't031_straight_binary_tertiary_horizontal'),
        't032': ('aircraft3', 't032_1bend_tertiary_left'),
        't033': ('aircraft3', 't033_2bend_tertiary_below'),
        't034': ('aircraft3', 't034_2bend_tertiary_above'),
        't035': ('aircraft3', 't035_2bend_tertiary_right'),
        't036': ('aircraft3', 't036_2bend_tertiary_left'),
        't040': ('aircraft_tree1', 't040_ibranch_horiz'),
        't041': ('aircraft_tree1', 't041_ibranch_vert'),
        't050': ('aircraft_tree1', 't050_rbranch_horiz'),
        't051': ('aircraft_tree1', 't051_rbranch_vert'),
        't052': ('aircraft_tree1', 't052_rbranch_vert_corner'),
    }
    selected_test = 't052'

    model_file_path = (Path(__file__).parent / tests[selected_test][0]).with_suffix(".xmm")
    layout_file_path = (Path(__file__).parent / tests[selected_test][1]).with_suffix(".mss")

    diagram_file_path = (Path(__file__).parent.parent / "Diagnostics" / "ftest").with_suffix(".pdf")

    DrawArgs = namedtuple("DrawArgs", "layout_file model_file output_file")

    test_input = DrawArgs(
        layout_file=layout_file_path,
        model_file=model_file_path,
        output_file=diagram_file_path
    )
    gen_diagram(test_input)
