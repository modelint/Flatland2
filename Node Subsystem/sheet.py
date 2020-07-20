"""
sheet.py – Standard and non-standard sheet sizes

"""
from sqlalchemy import create_engine, select, MetaData
from geometry_types import Rect_Size

us_sheet_sizes = {}
int_sheet_sizes = {}
default_us_sheet = 'tabloid'
default_int_sheet = 'A3'


def load_sizes():
    engine = create_engine('sqlite:///../Database population/sheet_data.db')
    conn = engine.connect()
    meta = MetaData()
    meta.reflect(bind=engine)
    sheets = meta.tables['Sheet']

    s_us = select([sheets]).where(sheets.c.Group == 'US')
    sheet_rows = conn.execute(s_us)
    for r in sheet_rows:
        us_sheet_sizes[r['Name']] = Rect_Size(width=float(r['Width']), height=float(r['Height']))

    s_int = select([sheets]).where(sheets.c.Group == 'INT')
    sheet_rows = conn.execute(s_int)
    for r in sheet_rows:
        int_sheet_sizes[r['Name']] = Rect_Size(width=int(r['Width']), height=int(r['Height']))
