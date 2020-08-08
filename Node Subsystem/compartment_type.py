"""
compartment_type.py – Specifies how a Node Type's compartment and text is drawn
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from geometry_types import Alignment, Padding
from draw_types import Text_Style, TypeFace, StrokeStyle, FontWeight, FontSlant
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from node_type import NodeType


class CompartmentType:
    def __init__(self, name: str, alignment: Alignment, padding: Padding, text_style: str):
        self.Name = name
        self.Alignment = alignment
        self.Padding = padding
        self.Text_style = Text_Style(typeface=TypeFace.PALATINO, size=9, slant=FontSlant.NORMAL, weight=FontWeight.NORMAL)

    def __repr__(self):
        return f'Name: {self.Name}, Alignment: {self.Alignment}, Padding: {self.Padding}, Text style: {self.Text_style}'


def create_compartment_types(node_type: 'NodeType') -> List[CompartmentType]:
    ct_list = []
    ctypes = fdb.MetaData.tables['Compartment Type']
    q = select([ctypes]).where(
        and_(ctypes.c['Node type'] == node_type.Name, ctypes.c['Diagram type'] == node_type.Diagram_type)
    ).order_by('Stack order')
    found = fdb.Connection.execute(q).fetchall()
    for i in found:
        ct_list.append(
            CompartmentType(
                name=i.Name,
                alignment=Alignment(vertical=i['Vertical alignment'], horizontal=i['Horizontal alignment']),
                padding=Padding(top=i['Pad top'], bottom=i['Pad bottom'], left=i['Pad left'], right=i['Pad right']),
                text_style=i['Text style']
            )
        )
    return ct_list
