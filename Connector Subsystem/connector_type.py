"""
connector_type.py - Connector Type
"""
from stem_type import StemType
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from diagram_type import DiagramType


class ConnectorType:
    """
    One or more Nodes may be interrelated by some model level relationship such as a state transition, generalization,
    association, dependency and so forth. Each such relationship is drawn with one or more connecting lines and
    terminating symbols.   A Connector Type defines the symbols, line connection geometry and appearance of Connectors
    corresponding to some model level relationship.

        Attributes

        - Name -- A descriptive name
        - Geometry -- The overall Connector branching layout corresponding to supported (modeled) Connector
          subclasses: *unary*, *binary* or *tree*

        Relationships

        - Stem Type / R59 -- Stem Types that appear on this Connector Type

    """

    def __init__(self, name: str, diagram_type: 'DiagramType', geometry: str, notation: str):
        """
        Create all stem ends for this Connector Type
        
        :param diagram_type:
        """
        self.Stem_type = {}
        self.Diagram_type = diagram_type
        self.Geometry = geometry

        # Load Stem types on model relationship R59
        self.Name = name
        stem_types_t = fdb.MetaData.tables['Stem Type']
        p = [stem_types_t.c.Name, stem_types_t.c['Minimum length']]
        r = and_(
            (stem_types_t.c['Connector type'] == self.Name),
            (stem_types_t.c['Diagram type'] == self.Diagram_type.Name)
        )
        q = select(p).where(r)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            self.Stem_type[r.Name] = StemType(
                name=r.Name, connector_type=self, minimum_length=r['Minimum length'], notation=notation)
