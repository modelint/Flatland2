"""
stem.py
"""

from sqlalchemy import select, and_
from geometry_types import Position
from rendered_symbol import RenderedSymbol
from stem_type import StemTypeName
from connection_types import NodeFace
from notation import StemSemantic

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector import Connector
    from node import Node


class Stem:
    """
    This is a line drawn from a face on a Node outward. The terminator on the node face is the root and the
    terminator on the other side of the line is the vine. A Stem may be decorated on either, both or neither end.
    A decoration consists of a graphic symbol such as an arrowhead or a circle or a fixed text label such as the
    UML '0..1' multiplicity label. A graphic symbol may be combined with a text symbol such as the Shlaer-Mellor
    arrow head 'c' conditionality combination.

    Attributes
    ---
    Connector : Stem is on one end of this Connector
    Stem_type : Specifies charactersitics and decoration, if any, of this Stem
    Node : Stem is attached to this Node
    Node_face : On this face of the Node
    Root_end : Where the Stem attaches to the Node face
    Vine_end : End of Stem away from Node face with clearance for any decoration
    """

    def __init__(self,
                 connector: 'Connector', stem_type: StemTypeName, semantic: StemSemantic, node: 'Node',
                 node_face: NodeFace, root_position: Position, vine_position: Position):
        self.Connector = connector
        self.Stem_type = stem_type
        self.Node = node
        self.Node_face = node_face
        self.Semantic = semantic
        self.Root_end = root_position
        self.Vine_end = vine_position

    def render(self):
        """
        Draw a stem decoration at either, both or neither end
        If there are no stem decorations to draw, just draw a short line from the root to the vine end
        using the connector line style and the default node face offset value
        """
        # Create a Rendered Symbol for each Stem End Decoration
        db = self.Connector.Diagram.Canvas.Database
        stem_end_decs = db.MetaData.tables['Stem End Decoration']
        q = select([stem_end_decs.c.Symbol, stem_end_decs.c.End], stem_end_decs.c.Growth).where(and_(
            stem_end_decs.c['Stem type'] == self.Stem_type,
            stem_end_decs.c['Semantic'] == self.Semantic,
            stem_end_decs.c['Diagram type'] == self.Connector.Diagram.Diagram_type,
            stem_end_decs.c['Notation'] == self.Connector.Diagram.Notation
        )
        )
        found = db.Connection.execute(q)
        for i in found:
            RenderedSymbol(stem=self, end=i['End'], symbol=i['Symbol'], growth=i['Growth'] )
        if not found:
            print("No rendered symbols")
            pass  # Set vine at no_decoration_offset, Draw line from root to vine
