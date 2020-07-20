"""
create_flatland_db.py – Create and populate the flatland database
"""
import os
from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer, ForeignKey

db_filename = 'flatland.db'
if os.path.exists(db_filename):
    os.remove(db_filename)

# Initialize the database file
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(f'sqlite:///{db_filename}')
metadata = MetaData()

# Define the relvars (tables)
Sheet = Table('Sheet', metadata,
              Column('Name', String(20), nullable=False, unique=True, primary_key=True),
              Column('Group', String(3), nullable=False),
              Column('Height', String(8), nullable=False),
              Column('Width', String(8), nullable=False)
              )

Notation = Table('Notation', metadata,
                 Column('Name', String, nullable=False, unique=True, primary_key=True),
                 Column('About', String, nullable=False),
                 Column('Why_use_it', String, nullable=False)
                 )

# Create the schema
metadata.create_all(engine)

conn = engine.connect()

# Populate the database
sheet_us_pop = [
    {'Name': 'letter', 'Group': 'US', 'Height': '11', 'Width': '8.5'},
    {'Name': 'tabloid', 'Group': 'US', 'Height': '11', 'Width': '17'},
    {'Name': 'C', 'Group': 'US', 'Height': '17', 'Width': '22'},
    {'Name': 'D', 'Group': 'US', 'Height': '22', 'Width': '34'},
    {'Name': 'E', 'Group': 'US', 'Height': '34', 'Width': '44'},
]

sheet_int_pop = [
    {'Name': 'A4', 'Group': 'INT', 'Height': '210', 'Width': '297'},
    {'Name': 'A3', 'Group': 'INT', 'Height': '297', 'Width': '420'},
    {'Name': 'A2', 'Group': 'INT', 'Height': '420', 'Width': '594'},
    {'Name': 'A1', 'Group': 'INT', 'Height': '594', 'Width': '841'}
]

notation_pop = [ {
    'Name': 'Shlaer-Mellor',
    'About': 'Source of Executable UML / xUML modeling semantics',
    'Why_use_it': 'Designed for fast easy hand drawing.Great for whiteboards and notes!'
}, {
    'Name': 'Starr',
    'About': 'Stealth mode! Mimimal drawing clutter to put the focus on the subject. Easy to draw online',
    'Why_use_it': 'Stealth mode! Mimimal drawing clutter to put the focus on the subject. Easy to draw online'
}, {
    'Name': 'xUML',
    'About': 'AKA, Executable UML. Usage of UML to represent executable semantics',
    'Why_use_it': 'Standards conformance. You are showing diagram to someone who knows, uses or must use UML'
} ]

conn.execute(Sheet.insert(), sheet_us_pop)
conn.execute(Sheet.insert(), sheet_int_pop)
conn.execute(Notation.insert(), notation_pop)
print("debug")
