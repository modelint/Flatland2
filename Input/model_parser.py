""" model_parser.py – First attempt to parse class block """

from flatland_exceptions import ModelGrammarFileOpen, ModelInputFileOpen, ModelInputFileEmpty
from model_visitor import SubsystemVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
from collections import namedtuple
from nocomment import nocomment
import os
from pathlib import Path

ClassData = namedtuple('ClassData', 'name attributes methods')
GenRelSpec = namedtuple('GenRelSpec', 'superclass subclasses')
RelSideSpec = namedtuple('RelSideSpec', 'phrase mult cname')
BinaryRelSpec = namedtuple('BinaryRelSpec', 't_side p_side')
RelData = namedtuple('RelData', 'rnum rspec')
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
    grammar_file = Path(__file__).parent.parent / "Model Markup/model.peg"
    root_rule_name = 'subsystem'  # We don't draw a diagram larger than a single subsystem

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
        class_records = []
        rel_records = []
        for cblock in result[1]:
            attrs = None if len(cblock) < 2 else cblock[1]
            methods = None if len(cblock) < 3 else cblock[2]
            class_record = ClassData(name=cblock[0], attributes=attrs, methods=methods)
            class_records.append(class_record)
        for rel in result[2]:
            if 'gen_rel' in rel.results.keys():
                br = GenRelSpec(superclass=rel[1][0], subclasses=rel[1][1:])
            else:
                tside = RelSideSpec(phrase=rel[1][0][0], mult=rel[1][0][1], cname=rel[1][0][2])
                pside = RelSideSpec(phrase=rel[1][1][0], mult=rel[1][1][1], cname=rel[1][1][2])
                br = BinaryRelSpec(t_side=tside, p_side=pside)
            rdata = RelData(rnum=rel[0], rspec=br)
            rel_records.append(rdata)
        if self.debug:
            # Transform dot files into pdfs
            os.system('dot -Tpdf subsystem_parse_tree.dot -o subsys_tree.pdf')
            os.system('dot -Tpdf subsystem_peg_parser_model.dot -o subsys_model.pdf')
        # Return the refined model data
        return Subsystem(name=result[0], classes=class_records, rels=rel_records)


if __name__ == "__main__":
    markup_path = Path(__file__).parent.parent / 'Model Markup/test.xmm'
    x = ModelParser(model_file_path=markup_path, debug=True)
    x.parse()
