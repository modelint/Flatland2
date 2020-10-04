""" layout_visitor.py """
from arpeggio import PTNodeVisitor

class LayoutVisitor(PTNodeVisitor):

    def visit_space(self, node, children):
        return None

    def visit_ss(self, node, children):
        return None

    def visit_name(self, node, children):
        name = ''.join(children)
        return name

    def visit_diagram(self, node, children):
        return children[0]

    def visit_notation(self, node, children):
        return children[0]

    def visit_presentation(self, node, children):
        return children[0]

    def visit_sheet(self, node, children):
        return children[0]

    def visit_orientation(self, node, children):
        return children[0]

    def visit_node_placement(self, node, children):
        return children

    def visit_node_block(self, node, children):
        return children

    def visit_shift(self, node, children):
        return children

    def visit_anchor(self, node, children):
        return children

    def visit_connector_placement(self, node, children):
        return children

    def visit_connector_block(self, node, children):
        return children

    def visit_layout_spec(self, node, children):
        return children.results

    def visit_diagram_layout(self, node, children):
        return children


