"""
sheet.py – The canvas is drawn on this instance of sheet
"""

from sqlalchemy import select
from flatland_exceptions import UnknownSheetSize, UnknownSheetGroup
from flatlanddb import FlatlandDB as fdb
from geometry_types import Rect_Size
from enum import Enum


class Group(Enum):
    US = 0
    INT = 1


class Sheet:
    def __init__(self, name):
        sheets = fdb.MetaData.tables['Sheet']
        query = select([sheets]).where(sheets.c.Name == name)
        i = fdb.Connection.execute(query).fetchone()
        if not i:
            raise UnknownSheetSize(name)
        self.Name = name
        if i.Group == 'us':
            self.Group = Group.US
        elif i.Group == 'int':
            self.Group = Group.INT
        else:
            raise UnknownSheetGroup("Group: [{i.Group}]")

        if self.Group == Group.US:
            self.Size = Rect_Size(height=float(i.Height), width=float(i.Width))
        else:
            self.Size = Rect_Size(height=int(i.Height), width=int(i.Width))

    def __repr__(self):
        u = "in" if self.Group == Group.US else 'mm'
        return f'Name: {self.Name}, Size: h{self.Size.height} {u} x w{self.Size.width} {u}'
