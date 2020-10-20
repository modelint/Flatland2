""" layout_parser.py """

from flatland_exceptions import LayoutGrammarFileOpen, LayoutFileOpen, LayoutFileEmpty
from layout_visitor import LayoutVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
from pathlib import Path
import os
from collections import namedtuple
from nocomment import nocomment

DiagramLayout = namedtuple('DiagramLayout', 'layout_spec node_placement connector_placement')
LayoutSpec = namedtuple('LayoutSpec', 'dtype pres notation sheet orientation')
NodePlacement = namedtuple('NodePlacement', 'wrap row column')
ConnPlacement = namedtuple('ConnPlacement', 'name_side bend t_data, p_data')
StemSpec = namedtuple('StemSpec', 'name_side wrap face node anchor_at')


class LayoutParser:
    """
    Parses a flatland diagram layout specification for a corresponding model file.

        Attributes

        - grammar_file -- (class based) Name of the system file defining the layout grammar
        - layout_file -- Name of user specified diagram layout specification file
    """
    grammar_file_name = "Model Markup/layout.peg"
    grammar_file = Path(__file__).parent.parent / grammar_file_name
    root_rule_name = "diagram_layout"

    def __init__(self, layout_file_path, debug=True):
        """
        Constructor

        :param layout_file_path: Where to find the user supplied layout file
        :param debug: Debug flag
        """
        self.debug = debug
        self.layout_file_path = layout_file_path

        # Read the grammar file
        try:
            self.layout_grammar = nocomment(open(LayoutParser.grammar_file, 'r').read())
        except OSError as e:
            raise LayoutGrammarFileOpen(LayoutParser.grammar_file)

        # Read the layout file
        try:
            self.layout_text = nocomment(open(self.layout_file_path, 'r').read())
        except OSError as e:
            raise LayoutFileOpen(self.layout_file_path)

        if not self.layout_text:
            raise LayoutFileEmpty(self.layout_file_path)

    def parse(self) -> DiagramLayout:
        """
        Parse the layout file and return the content
        :return: THe abstract syntax tree content of interest
        """
        # Create an arpeggio parser for our model grammar that does not eliminate whitespace
        # We interpret newlines and indents in our grammar, so whitespace must be preserved
        parser = ParserPEG(self.layout_grammar, LayoutParser.root_rule_name, skipws=False, debug=self.debug)
        # Now create an abstract syntax tree from our layout text
        parse_tree = parser.parse(self.layout_text)
        # Transform that into a result that is better organized with grammar artifacts filtered out
        result = visit_parse_tree(parse_tree, LayoutVisitor(debug=self.debug))
        if self.debug:
            # Transform dot files into pdfs
            os.system('dot -Tpdf diagram_layout_parse_tree.dot -o layout_tree.pdf')
            os.system('dot -Tpdf diagram_layout_peg_parser_model.dot -o layout_model.pdf')
        # Refine parsed result into something more useful for the client
        ld = result.results['layout_spec'][0] # layout data
        lspec = LayoutSpec(dtype=ld['diagram'][0], notation=ld['notation'][0], pres=ld['presentation'][0],
                           orientation=ld['orientation'][0], sheet=ld['sheet'][0])
        node_pdict = {
            n[0]: NodePlacement(
                wrap=1 if len(n) == 3 else n[3], row=n[1], column=n[2]
            ) for n in result.results['node_block'][0] }
        conn_pdict = {}
        for c in result.results['connector_block'][0]:
            cname_side, c_name = c[0][:2]  # Connector name
            c_bend = 1 if len(c[0]) == 2 else c[0][2]
            t_name_side, t_num_lines = c[1]  # T stem (left or top)
            p_name_side, p_num_lines = c[3]  # P stem (right or bottom)
            t_face, t_node = c[2][:2]  # Face and node ref
            p_face, p_node = c[4][:2]
            t_anchor = 0 if len(c[2]) == 2 else c[2][2]  # Optional anchor position on node face if not centered at 0
            p_anchor = 0 if len(c[4]) == 2 else c[4][2]
            conn_pdict[c_name] = ConnPlacement(
                name_side=cname_side,
                bend=c_bend,
                t_data=StemSpec(
                    name_side=t_name_side, wrap=t_num_lines, face=t_face, node=t_node, anchor_at=t_anchor),
                p_data=StemSpec(
                    name_side=p_name_side, wrap=p_num_lines, face=p_face, node=p_node, anchor_at=p_anchor),
            )
        return DiagramLayout(layout_spec=lspec, node_placement=node_pdict, connector_placement=conn_pdict)


if __name__ == "__main__":
    # For diagnostics
    layout_path = Path(__file__).parent.parent / 'Model Markup/test.mss'
    x = LayoutParser(layout_file_path=layout_path, debug=True)
    x.parse()