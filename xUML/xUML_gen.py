"""
xUML_gen.py – DEPRECATED (keeping it around for referece only)
"""
from straight_binary_connector import StraightBinaryConnector
from bending_binary_connector import BendingBinaryConnector
from connection_types import ConnectorName, OppositeFace, StemName
from command_interface import New_Stem, New_Path, New_Trunk_Branch, New_Offshoot_Branch, New_Branch_Set
from text_block import TextBlock


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


