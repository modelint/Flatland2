"""
connector_layout_specification.py – Connector Layout Specification
"""

from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select


class ConnectorLayoutSpecification:
    """
    Defines a set of values that determine how a Connector is drawn.
    """

    Default_stem_positions = None
    Default_rut_positions = None
    Runaround_lane_width = None

    def __init__(self):
        spec = fdb.MetaData.tables['Connector Layout Specification']
        q = select([spec])
        i = fdb.Connection.execute(q).fetchone()
        assert i, "No Connector Layout Specification in database"

        ConnectorLayoutSpecification.Default_stem_positions = i['Default stem positions']
        ConnectorLayoutSpecification.Default_rut_positions = i['Default rut positions']
        ConnectorLayoutSpecification.Runaround_lane_width = i['Runaround lane width']
