"""
drawn_stem_end.py – A Decorated Stem End drawn on the Canvas at the end of a Stem
"""

from sqlalchemy import select
from connection_types import DecoratedStemEnd
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from stem import Stem


class DrawnStemEnd:
    def __init__(self, stem: 'Stem', decorated_stem_end: DecoratedStemEnd):
        self.Stem = stem
        self.Decorated_stem_end = decorated_stem_end
        db = self.Stem.Connector.Diagram.Canvas.Database
        sdecs = db.MetaData.tables['Stem Decoration']

        q = select([sdecs.c.Symbol]).where(
            sdecs.c['Stem type'] == decorated_stem_end.stem_type
        )

