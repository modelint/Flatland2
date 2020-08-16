"""
symbol.py - Computes the length of each symbol and updates the database
"""
from sqlalchemy import select, join, func

class Symbol:
    """

    """

    @staticmethod
    def update_symbol_lengths(fdb):
        # Simple Symbols first
        arrow_t = fdb.MetaData.tables['Arrow Symbol']
        circle_t = fdb.MetaData.tables['Circle Symbol']
        cross_t = fdb.MetaData.tables['Cross Symbol']
        symbol_t = fdb.MetaData.tables['Symbol']

        query = select([symbol_t]).where(symbol_t.c.Shape != 'compound')
        simple_symbols = fdb.Connection.execute(query).fetchall()
        for s in simple_symbols:
            if s.Shape == 'arrow':
                query = select([arrow_t.c.Height]).where( arrow_t.c.Name == s.Name)
                v = fdb.Connection.execute(query).scalar()
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)
            if s.Shape == 'circle':
                query = select([circle_t.c.Radius]).where( circle_t.c.Name == s.Name)
                v = 2*fdb.Connection.execute(query).scalar()
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)
            if s.Shape == 'cross':
                query = select([cross_t.c['Root offset'], cross_t.c['Vine offset']]).where( cross_t.c.Name == s.Name)
                result = fdb.Connection.execute(query).fetchone()
                v = result['Root offset'] + result['Vine offset']
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)

        # Compound symbols
        # We want the sum for side-by-side simple symbols and the max for vertically stacked symbols
        splace_t = fdb.MetaData.tables['Symbol Stack Placement']
        j = join(symbol_t, splace_t, splace_t.c['Simple symbol'] == symbol_t.c.Name)
        q = select( # simple symbol inclusions in adjacency arrangement, compound, simple, length
            [splace_t.c['Compound symbol'], splace_t.c['Simple symbol'], symbol_t.c.Length, func.sum(symbol_t.c.Length).label("Total")]
            ).select_from(j).where(splace_t.c.Arrange.in_(['adjacent', 'last'])).group_by(splace_t.c['Compound symbol'])
        found = fdb.Connection.execute(q).fetchall()
        for r in found:
            u = symbol_t.update().where(symbol_t.c.Name == r['Compound symbol']).values(Length=r.Total)
            fdb.Connection.execute(u)

        q = select( # simple symbol inclusions in adjacency arrangement, compound, simple, length
            [splace_t.c['Compound symbol'], splace_t.c['Simple symbol'], symbol_t.c.Length, func.max(symbol_t.c.Length).label("Max")]
        ).select_from(j).where(splace_t.c.Arrange.in_(['layer', 'top'])).group_by(splace_t.c['Compound symbol'])
        found = fdb.Connection.execute(q).fetchall()
        for r in found:
            u = symbol_t.update().where(symbol_t.c.Name == r['Compound symbol']).values(Length=r.Max)
            fdb.Connection.execute(u)
