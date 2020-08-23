"""
stem_end_decoration.py
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from stem_type import StemType


class StemEndDecoration:
    """
    Either the root or vine end of a Decorated Stem that features a Symbol when drawn.
    """
    @staticmethod
    def getSymbol(stem_type: 'StemType', semantic: str, end: str, notation: str) -> Optional[str]:
        sedec_t = fdb.MetaData.tables['Stem End Decoration']
        # Project over all columns except Diagram type and Notation
        q_p =[
            sedec_t.c['Stem type'],
            sedec_t.c.Semantic,
            sedec_t.c.Symbol,
            sedec_t.c.End
        ]
        # Restrict to identifier of Stem End Decoration, I on the class diagram
        q_r = and_(
            (sedec_t.c['Diagram type'] == stem_type.Connector_type.Diagram_type.Name),
            (sedec_t.c.Notation == notation),
            (sedec_t.c['Stem type'] == stem_type.Name),
            (sedec_t.c.Semantic == semantic),
            (sedec_t.c.End == end)
        )
        q = select(q_p).where(q_r)
        row = fdb.Connection.execute(q).fetchone()
        return None if not row else row.Symbol


