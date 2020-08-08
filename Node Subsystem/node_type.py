"""
node_type.py
"""

from flatland_exceptions import UnknownNodeType
from geometry_types import Rect_Size
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from compartment_type import create_compartment_types


class NodeType:
    def __init__(self, node_type_name, diagram_type_name):

        ntypes = fdb.MetaData.tables['Node Type']
        q = select([ntypes]).where(
            and_( ntypes.c.Name == node_type_name, ntypes.c['Diagram type'] == diagram_type_name )
        )
        i = fdb.Connection.execute(q).fetchone()
        if not i:
            raise UnknownNodeType(node_type_name, diagram_type_name)

        self.Name = i.Name
        self.About = i.About
        self.Corner_rounding = i['Corner rounding']
        self.Border = i.Border
        self.Default_size = Rect_Size(height=i['Default height'], width=i['Default width'])
        self.Max_size = Rect_Size(height=i['Max height'], width=i['Max width'])
        self.Diagram_type = diagram_type_name

        self.Compartment_types = create_compartment_types(self)

    def __repr__(self):
        return f'Name: {self.Name}, Corner rounding: {self.Corner_rounding}, Border: {self.Border}, ' \
               f'Default size: {self.Default_size}, Max size: {self.Max_size}'
