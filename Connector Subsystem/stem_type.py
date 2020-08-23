"""
stem_type.py - Stem Type
"""
from annotation import Annotation
from stem_end_decoration import StemEndDecoration
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from connector_type import ConnectorType


class StemType:
    """
    Defines the characteristics of the portion of a Connector attached to a Node called a *Stem*.

    In a binary association connector of a class model, for example, there are two *class mult* Stem Types and
    one *associative mult* Stem Type defined. A transition Connector Type in a state machine diagram defines two
    Stem Types, *to state* and *from state*.

    Characteristics of primary interest are the semantics and notation and any other visual aspects of a Stem.

        Attributes

        - Name -- Each Stem Type has a unique name local to its Connector Type
        - Minimum_length -- A Stem of this type can never be shorter than this length. This keeps a bend or the Diagram edge
          from getting too close to the Node face. You wouldn’t want to bend at 90 degrees less than a point away from
          a Node face, for example.

          This value also serves to provide a default distance between the Root and Vine Ends, thus readily
          establishing the coordinate of the Vine End (assuming the Stem’s Vine end isn’t based on some other factor.
          In the case of a Tertiary Stem in a Binary Connector, for example, the Vine End will extend out to the
          nearest normal connector line, thus exceeding the Minimum Length  usually.

        Relationships

        - Connector type -- back reference via R59
        - Decorated stem -- All Decorated Stem instances via /R62/R55 for Diagram Type and Notation
        - Root symbol -- /R62/R55/R58/Stem End Decoration.Symbol(End : 'root')
        - Vine symbol -- /R62/R55/R58/Stem End Decoration.Symbol(End : 'vine')

    """
    def __init__(self, name: str, connector_type: 'ConnectorType', minimum_length: int, notation: str ):
        """
        Create all Decorated Stems for this Stem Type. See class description comments
        for meanings of the initialzing parameters
        """

        self.Name = name
        self.Connector_type = connector_type
        self.Minimum_length = minimum_length

        dec_stem_t = fdb.MetaData.tables['Decorated Stem']
        p = [dec_stem_t.c.Semantic]
        r = and_(
            (dec_stem_t.c['Stem type'] == self.Name),
            (dec_stem_t.c['Diagram type'] == self.Connector_type.Diagram_type.Name),
            (dec_stem_t.c['Notation'] == notation)
        )
        q = select(p).where(r)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            self.Root_symbol = StemEndDecoration.getSymbol(
                stem_type=self, end='root', semantic=r.Semantic, notation=notation)
            self.Vine_symbol = StemEndDecoration.getSymbol(
                stem_type=self, end='vine', semantic=r.Semantic, notation=notation)
            self.Label = Annotation.getLabel(stem_type=self, semantic=r.Semantic, notation=notation)

