""" model_parser.py – First attempt to parse class block """

from flatland_exceptions import ModelGrammarFileOpen, ModelInputFileOpen, ModelInputFileEmpty
from model_visitor import SubsystemVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
from collections import namedtuple
from nocomment import nocomment
import os
from pathlib import Path

Subsystem = namedtuple('Subsystem', 'name classes rels')

class ModelParser:
    """
    Parses an Executable UML subsystem model input file using the arpeggio parser generator

        Attributes

        - grammar_file -- (class based) Name of the system file defining the Executable UML grammar
        - root_rule_name -- (class based) Name of the top level grammar element found in grammar file
        - debug -- debug flag (used to set arpeggio parser mode)
        - model_grammar -- The model grammar text read from the system grammar file
        - model_text -- The input model text read from the user supplied text file
    """
    grammar_file_name = "Model Markup/model.peg"
    grammar_file = Path(__file__).parent.parent / grammar_file_name
    root_rule_name = 'subsystem'  # We don't draw a diagram larger than a single subsystem
    grammar_model_pdf = Path(__file__).parent.parent / "Diagnostics" / "subsystem_model.pdf"
    parse_tree_pdf = Path(__file__).parent.parent / "Diagnostics" / "subsystem_parse_tree.pdf"

    def __init__(self, model_file_path, debug=True):
        """
        Constructor

        :param model_file_path:  Where to find the user supplied model input file
        :param debug:  Debug flag
        """
        self.debug = debug
        self.model_file_path = model_file_path

        # Read the grammar file
        try:
            self.model_grammar = nocomment(open(ModelParser.grammar_file, 'r').read())
        except OSError as e:
            raise ModelGrammarFileOpen(ModelParser.grammar_file)

        # Read the model file
        try:
            self.model_text = nocomment(open(self.model_file_path, 'r').read())
        except OSError as e:
            raise ModelInputFileOpen(self.model_file_path)

        if not self.model_text:
            raise ModelInputFileEmpty(self.model_file_path)

    def parse(self) -> Subsystem:
        """
        Parse the model file and return the content
        :return:  The abstract syntax tree content of interest
        """
        # Create an arpeggio parser for our model grammar that does not eliminate whitespace
        # We interpret newlines and indents in our grammar, so whitespace must be preserved
        parser = ParserPEG(self.model_grammar, ModelParser.root_rule_name, skipws=False, debug=self.debug)
        # Now create an abstract syntax tree from our model text
        parse_tree = parser.parse(self.model_text)
        # Transform that into a result that is better organized with grammar artifacts filtered out
        result = visit_parse_tree(parse_tree, SubsystemVisitor(debug=self.debug))
        # Make it even nicer using easy to reference named tuples
        if self.debug:
            # Transform dot files into pdfs
            peg_tree_dot = Path("peggrammar_parse_tree.dot")
            peg_model_dot = Path("peggrammar_parser_model.dot")
            parse_tree_dot = Path("subsystem_parse_tree.dot")
            parser_model_dot = Path("subsystem_peg_parser_model.dot")
            os.system(f'dot -Tpdf {parse_tree_dot} -o {ModelParser.parse_tree_pdf}')
            os.system(f'dot -Tpdf {parser_model_dot} -o {ModelParser.grammar_model_pdf}')
            # Cleanup unneeded dot files, we just use the PDFs for now
            if Path.exists(parse_tree_dot):
                parse_tree_dot.unlink()
            if Path.exists(parser_model_dot):
                parser_model_dot.unlink()
            if Path.exists(peg_tree_dot):
                peg_tree_dot.unlink()
            if Path.exists(peg_model_dot):
                peg_model_dot.unlink()
        # Return the refined model data
        return Subsystem(name=result[0], classes=result[1], rels=result[2])


if __name__ == "__main__":
    markup_path = Path(__file__).parent.parent / 'Test/aircraft_tree1.xmm'
    x = ModelParser(model_file_path=markup_path, debug=True)
    x.parse()
