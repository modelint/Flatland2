""" c1_clean.py – First attempt to parse class block """

from arpeggio import PTNodeVisitor, visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
from collections import namedtuple
import os

ClassData = namedtuple('ClassData', 'class_name attributes methods')

input_file = os.path.expandvars("$FLATLAND3_PYCHARM/Model Markup/test.xmm")
input_text = open(input_file, 'r').read()

class ClassVisitor(PTNodeVisitor):

    def visit_class_header(self, node, children):
        class_name = children[0]
        if self.debug:
            print(f':>>> Returning class name: "{class_name}"')
        return class_name

    def visit_body_line(self, node, children):
        body_text_line = children[0]
        if self.debug:
            print(f':>>> Returning body line: "{body_text_line}"')
        return body_text_line

    def visit_method_block(self, node, children):
        if self.debug:
            print(f':>>> Returning method block: {children}')
        return children[:-1]  # truncate newline terminator

    def visit_attr_block(self, node, children):
        if self.debug:
            print(f':>>> Returning attribute block: {children}')
        return children[:-1]  # truncate newline terminator

    def visit_class_block(self, node, children):
        if self.debug:
            print(f':>>> Returning class block: {children}')
        return children

    def visit_class_set(self, node, children):
        if self.debug:
            print(f':>>> Returning class set: {children}')
        return children


def main(debug=False):
    grammar_file = os.path.expandvars("$FLATLAND3_PYCHARM/Model Markup/car.peg")
    model_grammar = open(grammar_file, 'r').read()
    parser = ParserPEG(model_grammar, 'class_set', skipws=False, debug=debug)
    parse_tree = parser.parse(input_text)
    result = visit_parse_tree(parse_tree, ClassVisitor(debug=debug))
    cd = []
    for r in result:
        print("Class extracted:")
        c = r[0]
        a = None if len(r) < 2 else r[1]
        m = None if len(r) < 3 else r[2]
        cd.append(ClassData(class_name=c, attributes=a, methods=m))
        print(r)
    os.system('dot -Tpdf class_text_parse_tree.dot -o ct_tree.pdf')
    os.system('dot -Tpdf class_text_peg_parser_model.dot -o ct_model.pdf')


if __name__ == "__main__":
    main(debug=True)