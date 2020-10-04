""" layout_parser.py """

from flatland_exceptions import LayoutGrammarFileOpen, LayoutFileOpen, LayoutFileEmpty
from layout_visitor import LayoutVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
import os
from collections import namedtuple

DiagramLayout = namedtuple('DiagramLayout', 'layout_spec node_placement connector_placement')


class LayoutParser:
    """
    Parses a flatland diagram layout specification for a corresponding model file.

        Attributes

        - grammar_file -- (class based) Name of the system file defining the layout grammar
        - layout_file -- Name of user specified diagram layout specification file
    """
    grammar_file = "Model Markup/mss.peg"
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
            self.layout_grammar = open(LayoutParser.grammar_file, 'r').read()
        except OSError as e:
            raise LayoutGrammarFileOpen(LayoutParser.grammar_file)

        # Read the layout file
        try:
            self.layout_text = open(self.layout_file_path, 'r').read()
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

        return DiagramLayout(layout_spec=result[0], node_placement=result[1], connector_placement=result[2])


if __name__ == "__main__":
    LayoutParser(layout_file_path='../Model Markup/test.mss', debug=True)