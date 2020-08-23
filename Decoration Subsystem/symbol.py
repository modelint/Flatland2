"""
symbol.py - Symbols from the Decoration Subsystem, loaded from the database
"""
from geometry_types import Position
from sqlalchemy import select, join, func, and_
from typing import TYPE_CHECKING
from collections import namedtuple
from flatlanddb import FlatlandDB as fdb

if TYPE_CHECKING:
    from diagram_type import DiagramType

# Symbol subclasses in the Decoration Subsystem are implemented as named tuples
# See Decoration Subsystem class model descriptions for full details on named tuple attributes summarized here

SymbolSpec = namedtuple('Symbol', 'length spec')
"""
Symbol

- length -- extent of the drawn symbol along a connector's axis
- spec -- the shape definition via R103 on the class diagram
"""

SimpleSymbol = namedtuple('SimpleSymbol', 'terminal_offset shape')
"""
Simple Symbol

- terminal_offset -- distance away from root or vine end
- shape -- shape specific definition via R100 on the class diagram
"""

StackPlacement = namedtuple('StackPlacement', 'symbol arrange offset')
"""
Symbol Stack Placement

The placement of a Simple Symbol within a Compound Symbol
A sequence of these constitues the spec for a Compound Symbol

- symbol -- Name of a Simple Symbol positioned in the stack
- arrange -- layered on top or adjacent to the previous Simple Symbol in the stack
- offset -- positional offset from the center if layered or side if adjacent
"""

# Simple Symbol shape specific attributes
ArrowSymbol = namedtuple('ArrowSymbol', 'base height fill')
CircleSymbol = namedtuple('CircleSymbol', 'radius solid')
CrossSymbol = namedtuple('CrossSymbol', 'root_offset vine_offset width angle')


class Symbol:
    """
    All Symbols are loaded from the database and held in the instances dictionary keyed by Symbol.Name
    """
    instances = {}

    def __init__(self, diagram_type: str, notation: str):
        """
        Load all symbols used on this diagram type for this notation

        :param diagram_type:
        :param notation:
        """
        self.update_symbol_lengths()

        # Tables
        sdecs_t = fdb.MetaData.tables['Stem End Decoration']
        arrow_t = fdb.MetaData.tables['Arrow Symbol']
        circle_t = fdb.MetaData.tables['Circle Symbol']
        cross_t = fdb.MetaData.tables['Cross Symbol']
        symbol_t = fdb.MetaData.tables['Symbol']
        s_symbol_t = fdb.MetaData.tables['Simple Symbol']
        stackp_t = fdb.MetaData.tables['Symbol Stack Placement']

        f = and_(
            (sdecs_t.c['Diagram type'] == diagram_type),
            (sdecs_t.c['Notation'] == notation)
        )
        # Simple symbols
        # Arrow symbols
        p = [symbol_t.c.Name, symbol_t.c.Length, s_symbol_t.c['Terminal offset'], arrow_t.c.Base, arrow_t.c.Height,
             arrow_t.c.Fill]
        j = sdecs_t.join(symbol_t, sdecs_t.c.Symbol == symbol_t.c.Name).join(s_symbol_t).join(arrow_t)
        q = select(p).select_from(j).where(f)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            Symbol.instances[r.Name] = SymbolSpec(
                length=r.Length,
                spec=SimpleSymbol(
                    terminal_offset=r['Terminal offset'],
                    shape=ArrowSymbol(base=r.Base, height=r.Height, fill=r.Fill)
                ),
            )
        # Circle symbols
        p = [symbol_t.c.Name, symbol_t.c.Length, s_symbol_t.c['Terminal offset'], circle_t.c.Radius, circle_t.c.Solid]
        j = sdecs_t.join(symbol_t, sdecs_t.c.Symbol == symbol_t.c.Name).join(s_symbol_t).join(circle_t)
        q = select(p).select_from(j).where(f)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            Symbol.instances[r.Name] = SymbolSpec(
                length=r.Length,
                spec=SimpleSymbol(
                    terminal_offset=r['Terminal offset'],
                    shape=CircleSymbol(radius=r.Radius, solid=r.Solid)
                ),
            )
        # Cross symbols
        p = [symbol_t.c.Name, symbol_t.c.Length, s_symbol_t.c['Terminal offset'],
             cross_t.c['Root offset'], cross_t.c['Vine offset'], cross_t.c.Width, cross_t.c.Angle]
        j = sdecs_t.join(symbol_t, sdecs_t.c.Symbol == symbol_t.c.Name).join(s_symbol_t).join(cross_t)
        q = select(p).select_from(j).where(f)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            Symbol.instances[r.Name] = SymbolSpec(
                length=r.Length,
                spec=SimpleSymbol(
                    terminal_offset=r['Terminal offset'],
                    shape=CrossSymbol(
                        root_offset=r['Root offset'], vine_offset=r['Vine offset'], width=r.Width, angle=r.Angle
                    )
                ),
            )

        # Compound symbols
        p = [symbol_t.c.Name, symbol_t.c.Length, stackp_t.c.Position, stackp_t.c['Simple symbol'],
             stackp_t.c.Arrange, stackp_t.c['Offset x'], stackp_t.c['Offset y']]
        j = sdecs_t.join(symbol_t, sdecs_t.c.Symbol == symbol_t.c.Name).join(
            stackp_t, symbol_t.c.Name == stackp_t.c['Compound symbol'])
        q = select(p).select_from(j).distinct().where(f).order_by("Name", "Position")
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            if r.Position == 1:  # First item of new stack
                # Start a new stack of simple symbols
                stack = [StackPlacement(
                    symbol=r['Simple symbol'], arrange=r.Arrange, offset=Position(r['Offset x'], r['Offset y'])
                )]
            else:
                # We don't neeed the terminating arrange value in a list
                arrange = r.Arrange if r.Arrange not in ('top', 'last') else None
                # Put the simple symbol on the stack using this clipped arrange value
                stack.append( StackPlacement(
                    symbol=r['Simple symbol'], arrange=arrange,  offset=Position(r['Offset x'], r['Offset y']))
                )
                if not arrange:
                    # No more simple symbols on this stack, so add the compound symbol to the instance dict
                    Symbol.instances[r.Name] = SymbolSpec(length=r.Length, spec=stack[:])  # COPY the stack


    @staticmethod
    def update_symbol_lengths():
        """
        Symbol.Length is a derived attribute in the Decoration Subsystem class model
        Compute total drawn length along Connector axis for each Symbol and update the database
        """
        # Simple Symbols first
        arrow_t = fdb.MetaData.tables['Arrow Symbol']
        circle_t = fdb.MetaData.tables['Circle Symbol']
        cross_t = fdb.MetaData.tables['Cross Symbol']
        symbol_t = fdb.MetaData.tables['Symbol']

        query = select([symbol_t]).where(symbol_t.c.Shape != 'compound')
        simple_symbols = fdb.Connection.execute(query).fetchall()
        for s in simple_symbols:
            if s.Shape == 'arrow':
                query = select([arrow_t.c.Height]).where(arrow_t.c.Name == s.Name)
                v = fdb.Connection.execute(query).scalar()
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)
            if s.Shape == 'circle':
                query = select([circle_t.c.Radius]).where(circle_t.c.Name == s.Name)
                v = 2 * fdb.Connection.execute(query).scalar()
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)
            if s.Shape == 'cross':
                query = select([cross_t.c['Root offset'], cross_t.c['Vine offset']]).where(cross_t.c.Name == s.Name)
                result = fdb.Connection.execute(query).fetchone()
                v = result['Root offset'] + result['Vine offset']
                u = symbol_t.update().where(symbol_t.c.Name == s.Name).values(Length=v)
                fdb.Connection.execute(u)

        # Compound symbols
        # We want the sum for side-by-side simple symbols and the max for vertically stacked symbols
        splace_t = fdb.MetaData.tables['Symbol Stack Placement']
        j = join(symbol_t, splace_t, splace_t.c['Simple symbol'] == symbol_t.c.Name)
        q = select(  # simple symbol inclusions in adjacency arrangement, compound, simple, length
            [splace_t.c['Compound symbol'], splace_t.c['Simple symbol'], symbol_t.c.Length,
             func.sum(symbol_t.c.Length).label("Total")]
        ).select_from(j).where(splace_t.c.Arrange.in_(['adjacent', 'last'])).group_by(splace_t.c['Compound symbol'])
        found = fdb.Connection.execute(q).fetchall()
        for r in found:
            u = symbol_t.update().where(symbol_t.c.Name == r['Compound symbol']).values(Length=r.Total)
            fdb.Connection.execute(u)

        q = select(  # simple symbol inclusions in adjacency arrangement, compound, simple, length
            [splace_t.c['Compound symbol'], splace_t.c['Simple symbol'], symbol_t.c.Length,
             func.max(symbol_t.c.Length).label("Max")]
        ).select_from(j).where(splace_t.c.Arrange.in_(['layer', 'top'])).group_by(splace_t.c['Compound symbol'])
        found = fdb.Connection.execute(q).fetchall()
        for r in found:
            u = symbol_t.update().where(symbol_t.c.Name == r['Compound symbol']).values(Length=r.Max)
            fdb.Connection.execute(u)


if __name__ == "__main__":
    fdb()
    Symbol.update_symbol_lengths(fdb)
    starr = 'Starr'
    sm = 'Shlaer-Mellor'
    x = 'xUML'
    smd = 'state machine'
    cd = 'class'
    s = Symbol(diagram_type=cd, notation=starr)
