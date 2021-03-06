""" layout_parser.py """

from flatland_exceptions import LayoutGrammarFileOpen, LayoutFileOpen, LayoutFileEmpty, LayoutParseError
from layout_visitor import LayoutVisitor
from arpeggio import visit_parse_tree, NoMatch
from arpeggio.cleanpeg import ParserPEG
from pathlib import Path
import os
from collections import namedtuple
from nocomment import nocomment

DiagramLayout = namedtuple('DiagramLayout', 'layout_spec node_placement connector_placement')
LayoutSpec = namedtuple('LayoutSpec', 'dtype pres notation sheet orientation')
NodePlacement = namedtuple('NodePlacement', 'wrap row column halign valign')
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
    grammar_model_pdf = Path(__file__).parent.parent / "Diagnostics" / "layout_model.pdf"
    parse_tree_pdf = Path(__file__).parent.parent / "Diagnostics" / "layout_parse_tree.pdf"

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
        try:
            parse_tree = parser.parse(self.layout_text)
        except NoMatch as e:
            raise LayoutParseError(self.layout_file_path.name, e) from None
        # Transform that into a result that is better organized with grammar artifacts filtered out
        result = visit_parse_tree(parse_tree, LayoutVisitor(debug=self.debug))
        if self.debug:
            # Transform dot files into pdfs
            peg_tree_dot = Path("peggrammar_parse_tree.dot")
            peg_model_dot = Path("peggrammar_parser_model.dot")
            parse_tree_dot = Path("diagram_layout_parse_tree.dot")
            parser_model_dot = Path("diagram_layout_peg_parser_model.dot")
            os.system(f'dot -Tpdf {parse_tree_dot} -o {LayoutParser.parse_tree_pdf}')
            os.system(f'dot -Tpdf {parser_model_dot} -o {LayoutParser.grammar_model_pdf}')
            # Cleanup unneeded dot files, we just use the PDFs for now
            if Path.exists(parse_tree_dot):
                parse_tree_dot.unlink()
            if Path.exists(parser_model_dot):
                parser_model_dot.unlink()
            if Path.exists(peg_tree_dot):
                peg_tree_dot.unlink()
            if Path.exists(peg_model_dot):
                peg_model_dot.unlink()
        # Refine parsed result into something more useful for the client
        ld = result.results['layout_spec'][0] # layout data
        lspec = LayoutSpec(dtype=ld['diagram'][0], notation=ld['notation'][0], pres=ld['presentation'][0],
                           orientation=ld['orientation'][0], sheet=ld['sheet'][0])
        node_pdict = { n['node_name']: n for n in result.results['node_block'][0] }
        if 'connector_block' in result.results:
            conn_pdict = { c['cname']: c for c in result.results['connector_block'][0] }
        else:
            conn_pdict = None
        return DiagramLayout(layout_spec=lspec, node_placement=node_pdict, connector_placement=conn_pdict)


if __name__ == "__main__":
    # For diagnostics
    layout_path = Path(__file__).parent.parent / 'Test/t052_rbranch_vert_corner.mss'
    x = LayoutParser(layout_file_path=layout_path, debug=True)
    x.parse()