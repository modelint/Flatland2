"""
db_play.py - diagnostic experiments with flatland db
"""
from sqlalchemy import create_engine, MetaData, select, and_

engine = create_engine(f'sqlite:///../Database/flatland.db', echo=True)
conn = engine.connect()
metadata = MetaData()
metadata.reflect(engine)

# ctypes = metadata.tables['Node Type']
# q = select([ctypes.c['Name'], ctypes.c['Diagram type']]).where(ctypes.c['Name'] == "class")
# i = conn.execute(q).fetchone()

content = [ ['Aircraft'], ['ID', 'Altitude'] ]
comps = metadata.tables['Compartment Type']
q = select([comps]).where(
    and_(comps.c['Node type'] == 'class', comps.c['Diagram type'] == 'class')
).order_by('Stack order')
found = conn.execute(q).fetchall()
z = zip(content, found)
for text, i in z:
    print(f'Text: |{text}|, Compartment: {dict(i)["Name"]}')
    #print(f'Text: |{text}|, Compartment: {i["Name"]}')


# stem_end_decs = metadata.tables['Stem End Decoration']
# q = select([stem_end_decs.c.Symbol, stem_end_decs.c.End]).where(and_(
#     stem_end_decs.c['Stem type'] == 'to initial state',
#     stem_end_decs.c['Semantic'] == 'initial pseudo state',
#     stem_end_decs.c['Diagram type'] == 'state machine',
#     stem_end_decs.c['Notation'] == 'xUML'
# )
# )

# print('===')
# print(f'Query: {str(q)}')
# print('--- Returned rows ---')
# for i in found:
#     print(i)
# print('---')


# dec_stems = metadata.tables['Decorated Stem']
# stem_sigs = metadata.tables['Stem Signification']
# j = stem_sigs.join(dec_stems)
#q = select([j]).where(and_(
#q = select([dec_stems.c.Stroke]).where(and_(
# q = select([dec_stems.c.Stroke]).where(and_(
#     dec_stems.c['Stem type'] == 'class mult',
#     dec_stems.c['Semantic'] == 'Mc mult',
#     dec_stems.c['Diagram type'] == 'class',
#     dec_stems.c['Notation'] == 'Starr'
# )
# )





#cols = [dec_stems.c['Stroke']]
#cols = [stem_end_decs.c['Symbol'], stem_end_decs.c['End'], dec_stems.c['Stroke']]
# j = stem_sigs.join(dec_stems)
#q = select(cols)

#q2 = select([j]).where(dsend.c['Notation'] == 'Shlaer-Mellor')
# q3 = select([sdec]).where(sdec.c['Notation'] == 'Shlaer-Mellor')
#     and_(
#         sdec.c['Notation'] == 'Shlaer-Mellor',
#         sdec.c['Stem type'] == 'class mult',
#         sdec.c['Diagram type'] == 'class',
#         sdec.c['Semantic'] == 'Mc mult'
#     )
# )
# cols = [sdec.c['Symbol'], sdec.c['Shape']]
# query = select(cols)
# query = query.select_from(dsend.join(sdec)).where(
#     and_(
#         sdec.c['Stem type'] == 'class mult',
#         sdec.c['Diagram type'] == 'class',
#         sdec.c['Notation'] == 'Shlaer-Mellor'
#         # sdec.c['Semantic'] == 'Mc mult'
#     )
# )
# query = select([sdec.c.Symbol, sdec.c.Shape]).select_from(dsend.join(sdec)).where( and_(
#     sdec.c['Stem type'] == 'class mult',
#     sdec.c['Diagram type'] == 'class',
#     sdec.c['Notation'] == 'Shlaer-Mellor',
#     sdec.c['Semantic'] == 'Mc mult'
#     )
# )
#
# found = conn.execute(q).fetchall()
# print("\n")
# print("Found:")
# print("---")
# for f in found:
#     print(f)
#     # print(f"Symbol: {f['Symbol']} Shape: {f['Shape']}")
# print("---")
if __name__ == "__main__":
    print("Hello from main!")
