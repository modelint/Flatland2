"""
stem_type.py - Stem Type
"""
from decorated_stem import DecoratedStem
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_


class StemType:
    """
    Defines the characteristics of the portion of a Connector attached to a Node called a *Stem*.

    In a binary association connector of a class model, for example, there are two *class mult* Stem Types and
    one *associative mult* Stem Type defined. A transition Connector Type in a state machine diagram defines two
    Stem Types, *to state* and *from state*.

    Characteristics of primary interest are the semantics and notation and any other visual aspects of a Stem.

        Attributes

        - Name -- Each Stem Type has a unique name local to its Connector Type
        - About -- Description of the purpose/usage of this Stem Type
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
    """
    def __init__(self, name: str, connector_type_name: str, diagram_type_name: str, about: str,
                 minimum_length: int, geometry: str, notation: str ):
        """
        Create all Decorated Stems for this Stem Type. See class description comments
        for meanings of the initialzing parameters

        :param name:
        :param connector_type_name:
        :param diagram_type_name:
        :param about:
        :param minimum_length:
        :param notation:
        """

        self.Name = name
        self.About = about
        self.Connector_type = connector_type_name
        self.Diagram_type = diagram_type_name
        self.Minimum_length = minimum_length
        self.Geometry = geometry
        self.DecoratedStems = {}

        # Load only those Decorated Stems for the user selected Diagram Type and Notation
        dec_stem_t = fdb.MetaData.tables['Decorated Stem']
        p = [dec_stem_t.c.Semantic]
        r = and_(
            (dec_stem_t.c['Stem type'] == self.Name),
            (dec_stem_t.c['Diagram type'] == self.Diagram_type),
            (dec_stem_t.c['Notation'] == notation)
        )
        q = select(p).where(r)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            self.DecoratedStems[r.Semantic] = DecoratedStem(
                stem_type=self.Name, semantic=r.Semantic, notation=notation,
                diagram_type_name=self.Diagram_type)

