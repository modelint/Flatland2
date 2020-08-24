"""
connector_type.py - Connector Type
"""
from stem_type import StemType
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_


class ConnectorType:
    """
    One or more Nmodes may be interrelated by some model level relationship such as a state transition, generalization,
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

    def __init__(self, name: str, diagram_type_name: str, about: str, geometry: str, notation: str):
        """
        Create all stem ends for this Connector Type
        """
        self.Stem_type = {}
        self.Diagram_type = diagram_type_name
        self.About = about
        self.Geometry = geometry

        # Load Stem types on model relationship R59
        self.Name = name
        stem_types_t = fdb.MetaData.tables['Stem Type']
        p = [stem_types_t.c.Name, stem_types_t.c.About, stem_types_t.c['Minimum length'], stem_types_t.c.Geometry]
        r = and_(
            (stem_types_t.c['Connector type'] == self.Name),
            (stem_types_t.c['Diagram type'] == diagram_type_name)
        )
        q = select(p).where(r)
        rows = fdb.Connection.execute(q).fetchall()
        for r in rows:
            self.Stem_type[r.Name] = StemType(
                name=r.Name, connector_type_name=self.Name, diagram_type_name=self.Diagram_type,
                about=r.About, minimum_length=r['Minimum length'], geometry=r.Geometry, notation=notation)
