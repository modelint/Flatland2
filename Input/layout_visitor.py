""" layout_visitor.py """
from arpeggio import PTNodeVisitor
from connection_types import NodeFace

face_map = {'r': NodeFace.RIGHT, 'l': NodeFace.LEFT, 't': NodeFace.TOP, 'b': NodeFace.BOTTOM}

class LayoutVisitor(PTNodeVisitor):

    def visit_space(self, node, children):
        """Discard spaces"""
        return None

    def visit_face(self, node, children):
        """Face character"""
        return face_map[node.value]

    def visit_dir(self, node, children):
        """Pos-neg direction"""
        return 1 if node.value == '+' else -1

    def visit_name(self, node, children):
        """Words and delmiters joined to form a complete name"""
        name = ''.join(children)
        return name

    def visit_diagram(self, node, children):
        """Keyword argument"""
        return children[0]

    def visit_notation(self, node, children):
        """Keyword argument"""
        return children[0]

    def visit_presentation(self, node, children):
        """Keyword argument"""
        return children[0]

    def visit_sheet(self, node, children):
        """Keyword argument"""
        return children[0]

    def visit_orientation(self, node, children):
        """Keyword argument"""
        return children[0]

    def visit_node_placement(self, node, children):
        """node_name, row, column"""
        return [ children[0], int(children[1]), int(children[2])]

    def visit_node_block(self, node, children):
        """All node placements"""
        return children

    def visit_anchor(self, node, children):
        """Placement of anchor position direction (1 or -1 * number of notches"""
        return children[0] * int(children[1])

    def visit_node_face(self, node, children):
        if len(children) == 3:
            return [ children[0], children[2], children[1] ]
        return children

    def visit_sname_place(self, node, children):
        """Side of stem axis and number of lines in text block"""
        return children[0], int(children[1])

    def visit_cname_place(self, node, children):
        """Side of connector axis and name of connector"""
        return children

    def visit_connector_layout(self, node, children):
        """"""
        return children

    def visit_connector_block(self, node, children):
        return children

    def visit_layout_spec(self, node, children):
        return children.results

    def visit_diagram_layout(self, node, children):
        return children


