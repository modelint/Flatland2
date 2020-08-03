"""
diagram_layout_specification.py
"""

from flatlanddb import FlatlandDB as fdb
from geometry_types import Padding, Position, Alignment
from sqlalchemy import select


class DiagramLayoutSpecification:
    """
    Defines a set of values that determine how a Diagram and Grid is positioned on a Canvas and
    how Nodes are positioned relative to the Diagram and Grid.
    """
    Default_margin = None
    Default_diagram_origin = None
    Default_cell_padding = None
    Default_cell_alignment = None


    def __init__(self):
        spec = fdb.MetaData.tables['Diagram Layout Specification']
        q = select([spec])
        i = fdb.Connection.execute(q).fetchone()
        assert i, "No Diagram Layout Specification in database"

        DiagramLayoutSpecification.Default_margin = Padding(
            top=i['Default margin top'], bottom=i['Default margin bottom'],
            left=i['Default margin left'], right=i['Default margin right']
        )

        DiagramLayoutSpecification.Default_diagram_origin = Position(x=i['Default diagram origin x'], y=i['Default diagram origin y'])

        DiagramLayoutSpecification.Default_cell_padding = Padding(
            top=i['Default cell padding top'], bottom=i['Default cell padding bottom'],
            left=i['Default cell padding left'], right=i['Default cell padding right']
        )

        DiagramLayoutSpecification.Default_cell_alignment = Alignment(
            vertical=i['Default cell alignment vertical'],
            horizontal=i['Default cell alignment horizontal']
        )
