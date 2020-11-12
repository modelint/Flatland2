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

    def visit_number(self, node, children):
        """Natural number"""
        return int(node.value)

    def visit_notch(self, node, children):
        """The digit 0 or a positive or negative number of notches"""
        if children[0] == '0':
            return 0
        else:
            scale = -1 if children[0] == '-' else 1
            return int(children[1]) * scale

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

    def visit_wrap(self, node, children):
        """Number of lines to wrap"""
        return {node.rule_name: int(children[0]) }

    def visit_node_loc(self, node, children):
        return {node.rule_name: children}

    def visit_node_name(self, node, children):
        return {node.rule_name: ''.join(children)}

    def visit_node_placement(self, node, children):
        """node_name, wrap?, row, column"""
        # Combine all child dictionaries
        items = {k: v for d in children for k, v in d.items()}
        return items

    def visit_node_block(self, node, children):
        """All node placements"""
        return children

    def visit_valign(self, node, children):
        """Vertical alignment of noce in its cell"""
        return {node.rule_name: children[0].upper()}

    def visit_halign(self, node, children):
        """Horizontal alignment of noce in its cell"""
        return {node.rule_name: children[0].upper()}

    def visit_node_align(self, node, children):
        """Vertical and/or horizontal alignment of node in its cell"""
        if len(children) == 2:
            # Merge the two dictionaries
            return {**children[0], **children[1]}
        else:
            return children[0]

    def visit_node_face(self, node, children):
        """Where connector attaches to node face"""
        return {k:v[0] for k,v in children.results.items()}

    def visit_sname_place(self, node, children):
        """Side of stem axis and number of lines in text block"""
        d = {'stem_dir': children[0]}  # initialize d
        d.update(children[1]) # Add wrap key
        return d

    def visit_bend(self, node, children):
        """Number of bend where cname appears"""
        return int(children[0])

    def visit_tstem(self, node, children):
        """T stem layout info"""
        items = {k: v for d in children for k, v in d.items()}
        d = {node.rule_name: items}
        return d

    def visit_pstem(self, node, children):
        """P stem layout info"""
        items = {k: v for d in children for k, v in d.items()}
        d = {node.rule_name: items}
        return d

    def visit_tertiary_node(self, node, children):
        """Tertiary node face and anchor"""
        return {node.rule_name: children[0]}

    def visit_path(self, node, children):
        """Lane and rut followed by a connector bend"""
        return {'lane': children[0], 'rut': children.results.get('notch', [0])[0]}  # Rut is 0 by default

    def visit_paths(self, node, children):
        """A sequence of one or more paths"""
        return {node.rule_name: children}

    def visit_cname_place(self, node, children):
        """Side of connector axis and name of connector and optional bend where cname is placed"""
        d = {'cname': children.results['name'][0], 'bend': children.results.get('bend', [1])[0],
             'dir': children.results.get('dir', [1])[0]}
        return d

    def visit_trunk_face(self, node, children):
        """A single trunk node at the top of the tree layout"""
        r = children.results
        if 'notch' in r:
            r['anchor'] = r.pop('notch')  # In this context, notch represents an anchor
        d = {node.rule_name: {k:v[0] for k,v in r.items()}}
        return d

    def visit_leaf_faces(self, node, children):
        """All layout info for the tree connector"""
        d = {}
        for r in children:
            n = r.pop('name')
            if 'notch' in r:
                r['anchor'] = r.pop('notch')  # In this context, notch represents an anchor
            d[n] = r
        return d

    def visit_tree_layout(self, node, children):
        """All layout info for the tree connector"""
        # First two elements layout trunk and leaf nodes with an optional path
        # Create a single key dictionary with the path data if any is specified
        p = { 'path': None if 'path' not in children.results.keys() else children.results['path'][0] }
        # Fold trunk, leaf and path dictionaries together
        items = {**children[0], **children[1], **p}
        return items

    def visit_binary_layout(self, node, children):
        """All layout info for the binary connector"""
        # Combine all child dictionaries
        items = {k: v for d in children for k, v in d.items()}
        return items

    def visit_connector_layout(self, node, children):
        """All layout info for the connector"""
        # Combine all child dictionaries
        items = {k: v for d in children for k, v in d.items()}
        return items

    def visit_connector_block(self, node, children):
        return children

    def visit_layout_spec(self, node, children):
        return children.results

    def visit_diagram_layout(self, node, children):
        return children


