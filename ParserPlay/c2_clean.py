""" c1_clean.py – First attempt to parse class block """

from visitor import SubsystemVisitor
from arpeggio import visit_parse_tree
from arpeggio.cleanpeg import ParserPEG
from collections import namedtuple
import os

ClassData = namedtuple('ClassData', 'name attributes methods')
GenRelSpec = namedtuple('GenRelSpec', 'superclass subclasses')
RelSideSpec = namedtuple('RelSideSpec', 'phrase mult cname')
BinaryRelSpec = namedtuple('BinaryRelSpec', 't_side p_side')
RelData = namedtuple('RelData', 'rnum rspec')
Subsystem = namedtuple('Subsystem', 'name classes rels')

input_file = os.path.expandvars("$FLATLAND3_PYCHARM/Model Markup/test.xmm")
input_text = open(input_file, 'r').read()


def main(debug=False):
    grammar_file = os.path.expandvars("$FLATLAND3_PYCHARM/Model Markup/car.peg")
    model_grammar = open(grammar_file, 'r').read()
    parser = ParserPEG(model_grammar, 'subsystem', skipws=False, debug=debug)
    parse_tree = parser.parse(input_text)
    result = visit_parse_tree(parse_tree, SubsystemVisitor(debug=debug))
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
            pside = RelSideSpec(phrase=rel[1][1][0], mult=rel[1][1][0], cname=rel[1][1][2])
            br = BinaryRelSpec(t_side=tside, p_side=pside)
        rdata = RelData(rnum=rel[0], rspec=br)
        rel_records.append(rdata)
    s = Subsystem(name=result[0], classes=class_records, rels=rel_records)
    print(s)
    os.system('dot -Tpdf subsystem_parse_tree.dot -o subsys_tree.pdf')
    os.system('dot -Tpdf subsystem_peg_parser_model.dot -o subsys_model.pdf')


if __name__ == "__main__":
    main(debug=True)