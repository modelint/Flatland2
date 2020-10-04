""" model_visitor.py """

from arpeggio import PTNodeVisitor

class SubsystemVisitor(PTNodeVisitor):

    def visit_nl(self, node, children):
        return None

    def visit_sp(self, node, children):
        return None

    def visit_mult(self, node, children):
        mult = node.value
        if self.debug:
            print(f':>>> Returning mult: "{mult}"')
        return mult

    def visit_icaps_name(self, node, children):
        name = ''.join(children)
        if self.debug:
            print(f':>>> Returning icaps name: "{children}"')
        return name

    def visit_class_header(self, node, children):
        cname = children[0]
        if self.debug:
            print(f':>>> Returning class header: "{cname}"')
        return cname

    def visit_subsystem_header(self, node, children):
        subsys_name = children[0]
        if self.debug:
            print(f':>>> Returning class header: "{subsys_name}"')
        return subsys_name

    def visit_body_line(self, node, children):
        body_text_line = children[0]
        if self.debug:
            print(f':>>> Returning body line: "{body_text_line}"')
        return body_text_line

    def visit_phrase(self, node, children):
        phrase = ''.join(children)
        if self.debug:
            print(f':>>> Returning phrase: "{children}"')
        return phrase

    def visit_rel_side(self, node, children):
        phrase, mult, cname = children
        if self.debug:
            print(f':>>> Children rel side: "phrase: {phrase}, mult: {mult}, class: {cname}')
        return phrase, mult, cname

    def visit_rname(self, node, children):
        rnum = children[0]
        if self.debug:
            print(f':>>> Returning rnum: {rnum}')
        return rnum

    def visit_superclass(self, node, children):
        superclass_name = children[0]
        if self.debug:
            print(f':>>> Returning superclass: {superclass_name}')
        return superclass_name

    def visit_subclass(self, node, children):
        subclass_name = children[0]
        if self.debug:
            print(f':>>> Returning subclass: {subclass_name}')
        return subclass_name

    def visit_gen_rel(self, node, children):
        if self.debug:
            print(f':>>> Returning gen rel classes: {children}')
        return children

    def visit_binary_rel(self, node, children):
        if self.debug:
            print(f':>>> Returning rel sides: {children}')
        return children

    def visit_rel(self, node, children):
        if self.debug:
            print(f':>>> Returning rel: {children}')
        return children

    def visit_method_block(self, node, children):
        if self.debug:
            print(f':>>> Returning method block: {children}')
        return children  # truncate newline terminator

    def visit_attr_block(self, node, children):
        if self.debug:
            print(f':>>> Returning attribute block: {children}')
        return children

    def visit_class_set(self, node, children):
        if self.debug:
            print(f':>>> Returning class set: {children}')
        return children

    def visit_class_block(self, node, children):
        if self.debug:
            print(f':>>> Returning class block: {children}')
        return children

    def visit_rel_section(self, node, children):
        if self.debug:
            print(f':>>> Returning rel section: {children}')
        return children.results['rel']


    def visit_subsystem(self, node, children):
        if self.debug:
            print(f':>>> Returning subsystem: {children}')
        return children


