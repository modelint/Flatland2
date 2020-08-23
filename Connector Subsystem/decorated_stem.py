"""
decorated_stem.py - Decorated Stem
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem_type import StemType


class DecoratedStem:
    """
    A Stem Signification that is decorated somehow when it appears on a Diagram is considered a
    Decorated Stem. Not all Stem Significations are decorated. The stem attaching a class diagram
    subclass is not notated in many class diagram notations.
    """
    def __init__(self, stem_type: 'StemType'):
        """

        :param stem_type:
        """
        self.Stem_type = stem_type
        self.Root_symbol = None
        self.Vine_symbol = None

        stem_end_dec_t = fdb.MetaData.tables['Stem End Decoration']
        p = [stem_end_dec_t.c.Symbol, stem_end_dec_t.c.End]
        r = and_(
            (stem_end_dec_t.c['Stem type'] == self.Stem_type),
            (stem_end_dec_t.c['Diagram type'] == self.Stem_type.Connector_type.Diagram_type.Name),
            (stem_end_dec_t.c['Notation'] == self.Stem_type.Connector_type.Diagram_type.Diagram.Notation),
        )
        q = select(p).where(r)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            if r.End == 'root':
                self.Root_symbol = r.Symbol
            elif r.End == 'vine':
                self.Vine_symbol = r.Symbol
            else:  # Illegal enum value in database for some reason
                assert False, f"Illegal enum value for End in {stem_type}"


