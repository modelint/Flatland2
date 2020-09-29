"""
c1.py – First attempt to parse class block
"""
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF, ParserPython, PTNodeVisitor, visit_parse_tree
from arpeggio import RegExMatch as _
from collections import namedtuple
import os

ClassData = namedtuple('ClassData', 'class_name attributes')

indent_length = 4

input_text = '''class Shape
    attributes
        ID: Nominal | I
        Tablet > Tablet.ID:R13
        Line style > Line Style.Name:R14
    --
'''


# def ws_end():
#     """Continguous white space"""
#     return _(r'[ \t\r\n]*')
#
# def ws_delim():
#     """A single non-newline whitespace character"""
#     return _(r'[ \t]*')

def nl():
    return '\n'


def indent():
    return ' ' * indent_length


def name():
    return _(r'[a-zA-Z0-9]*')


def block_end():
    return indent, '--'


def attr_line():
    return indent, indent, _(r'.*'), nl


def attr_header():
    return indent, 'attributes', nl


def attr_block():
    return attr_header, OneOrMore(attr_line), block_end


def class_header():
    return 'class', ' ', name, nl


def class_block():
    return class_header, attr_block


def class_text():
    return OneOrMore(class_block)


class ClassVisitor(PTNodeVisitor):

    def visit_class_header(self, node, children):
        class_name = children[0]
        if self.debug:
            print(f':>>> Returning class name: "{class_name}"')
        return class_name

    def visit_attr_line(self, node, children):
        attr_text_line = children[0]
        if self.debug:
            print(f':>>> Returning attribute line: "{attr_text_line}"')
        return attr_text_line

    def visit_attr_block(self, node, children):
        if self.debug:
            print(f':>>> Returning attribute block? {children}')
        return children

    def visit_class_block(self, node, children):
        if self.debug:
            print(f':>>> Returning class block? {children}')
        return children


root = class_text
classes = []


def main(debug=False):
    parser = ParserPython(root, skipws=False, debug=debug)
    parse_tree = parser.parse(input_text)
    result = visit_parse_tree(parse_tree, ClassVisitor(debug=debug))
    cd = ClassData(class_name=result[0], attributes=result[1])
    os.system('dot -Tpdf class_text_parse_tree.dot -o ct_tree.pdf')
    os.system('dot -Tpdf class_text_parser_model.dot -o ct_model.pdf')
    print(input_text)


if __name__ == "__main__":
    main(debug=True)
