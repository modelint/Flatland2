"""
relvars.py – Relation variables (relvars / tables) in the flatland database
"""
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy import ForeignKey, UniqueConstraint, PrimaryKeyConstraint, ForeignKeyConstraint


def define(db):
    return {
        'sheet': Table('Sheet', db.MetaData,
                       Column('Name', String(20), nullable=False, unique=True, primary_key=True),
                       Column('Group', String(3), nullable=False),
                       Column('Height', String(8), nullable=False),
                       Column('Width', String(8), nullable=False)
                       ),
        'notation': Table('Notation', db.MetaData,
                          Column('Name', String, nullable=False, unique=True, primary_key=True),
                          Column('About', String, nullable=False),
                          Column('Why use it', String, nullable=False)
                          ),
        'diagram_type': Table('Diagram Type', db.MetaData,
                              Column('Name', String, nullable=False, unique=True, primary_key=True),
                              Column('About', String, nullable=False)
                              ),
        'diagram_notation': Table('Diagram Notation', db.MetaData,
                                  Column('Diagram type', String, ForeignKey('Diagram Type.Name'), nullable=False),
                                  Column('Notation', String, ForeignKey('Notation.Name'), nullable=False),
                                  PrimaryKeyConstraint('Diagram type', 'Notation', name='I1')
                                  ),
        'node_type': Table('Node Type', db.MetaData,
                           Column('Name', String, nullable=False),
                           Column('Diagram type', String, ForeignKey('Diagram Type.Name'), nullable=False),
                           Column('About', String, nullable=False),
                           Column('Corner rounding', Integer, nullable=False),
                           Column('Border', String, nullable=False),
                           Column('Default height', Integer, nullable=False),
                           Column('Default width', Integer, nullable=False),
                           Column('Max height', Integer, nullable=False),
                           Column('Max width', Integer, nullable=False),
                           PrimaryKeyConstraint('Name', 'Diagram type', name='I1')
                           ),
        'compartment_type': Table('Compartment Type', db.MetaData,
                                  Column('Name', String, nullable=False),
                                  Column('Vertical alignment', String(10), nullable=False),
                                  Column('Horizontal alignment', String(10), nullable=False),
                                  Column('Pad top', Integer, nullable=False),
                                  Column('Pad bottom', Integer, nullable=False),
                                  Column('Pad left', Integer, nullable=False),
                                  Column('Pad right', Integer, nullable=False),
                                  Column('Text style', String(15), nullable=False),
                                  Column('Node type', String, ForeignKey('Node Type.Name'), nullable=False),
                                  Column('Diagram type', String, ForeignKey('Node Type.Diagram type'), nullable=False),
                                  Column('Stack order', Integer, nullable=False),
                                  PrimaryKeyConstraint('Stack order', 'Node type', 'Diagram type', name='I1'),
                                  UniqueConstraint('Name', 'Node type', 'Diagram type', name='I2')
                                  )
    }
