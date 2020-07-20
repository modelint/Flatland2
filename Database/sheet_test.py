"""
sheet_test.py – Standard and non-standard sheet sizes

"""
from geometry_types import Rect_Size
from sqlalchemy import create_engine, select, MetaData

engine = create_engine('sqlite:///sheet_data.db')
conn = engine.connect()
meta = MetaData()
meta.reflect(bind=engine)
sheets = meta.tables['Sheet']


us_sheet_sizes = {}
s_us = select([sheets]).where(sheets.c.Group == 'US')
sheet_rows = conn.execute(s_us)
for r in sheet_rows:
    us_sheet_sizes[r['Name']] = Rect_Size(width=float(r['Width']), height=float(r['Height']))

int_sheet_sizes = {}
s_int = select([sheets]).where(sheets.c.Group == 'INT')
sheet_rows = conn.execute(s_int)
for r in sheet_rows:
    int_sheet_sizes[r['Name']] = Rect_Size(width=int(r['Width']), height=int(r['Height']))

print("debug")

