"""
p1.py – Parser exmaple from web
"""

from pypeg2 import *


class Type(Keyword):
    grammar = Enum( K("int"), K("long"))


class Parameter:
    grammar = attr("typing", Type), name()


class Parameters(Namespace):
    grammar = optional(csl(Parameter))


class Instruction(str):
    grammar = word, ";"


block = "{", maybe_some(Instruction), "}"


class Function(List):
    grammar = attr("typing", Type), name(), "(", attr("parms", Parameters), ")", block


f = parse("int f(int a, long b) { do_this; do_that; }", Function)

print()


