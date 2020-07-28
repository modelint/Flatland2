"""
db_play.py - diagnostic experiments with flatland db
"""
from sqlalchemy import create_engine, MetaData, select, and_

engine = create_engine(f'sqlite:///../Database/flatland.db', echo=True)
conn = engine.connect()
metadata = MetaData()
metadata.reflect(engine)


dsend = metadata.tables['Decorated Stem End']
sdec = metadata.tables['Stem Decoration']
j = sdec.join(dsend)
q2 = select([j]).where(dsend.c['Notation'] == 'Shlaer-Mellor')
# q3 = select([sdec]).where(sdec.c['Notation'] == 'Shlaer-Mellor')
#     and_(
#         sdec.c['Notation'] == 'Shlaer-Mellor',
#         sdec.c['Stem type'] == 'class mult',
#         sdec.c['Diagram type'] == 'class',
#         sdec.c['Semantic'] == 'Mc mult'
#     )
# )
cols = [sdec.c['Symbol'], sdec.c['Shape']]
query = select(cols)
query = query.select_from(dsend.join(sdec)).where(
    and_(
        sdec.c['Stem type'] == 'class mult',
        sdec.c['Diagram type'] == 'class',
        sdec.c['Notation'] == 'Shlaer-Mellor'
        # sdec.c['Semantic'] == 'Mc mult'
    )
)
# query = select([sdec.c.Symbol, sdec.c.Shape]).select_from(dsend.join(sdec)).where( and_(
#     sdec.c['Stem type'] == 'class mult',
#     sdec.c['Diagram type'] == 'class',
#     sdec.c['Notation'] == 'Shlaer-Mellor',
#     sdec.c['Semantic'] == 'Mc mult'
#     )
# )
#
found = conn.execute(q2).fetchall()
print("\n")
print("Found:")
print("---")
for f in found:
    print(f)
    #print(f"Symbol: {f['Symbol']} Shape: {f['Shape']}")
print("---")
