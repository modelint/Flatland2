"""
stem_type_usage.py

Stem Type Usage class
"""

from collections import namedtuple
from connector_type import ConnectorTypeName, ConnectionRole
from diagram_type import DiagramTypeName
from stem_type import StemTypeName


StemTypeUsageID = namedtuple("Stem_Type_Usage_ID", "connector_type diagram_type stem_type")

stem_type_usages = {
    # Binary and Association Class Stems
    StemTypeUsageID(connector_type=ConnectorTypeName.binary_assoc,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.class_mult): ConnectionRole.opposing,
    StemTypeUsageID(connector_type=ConnectorTypeName.assoc_class,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.class_mult): ConnectionRole.opposing,
    StemTypeUsageID(connector_type=ConnectorTypeName.assoc_class,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.assoc_class_mult): ConnectionRole.tee,

    # Generalization stems
    StemTypeUsageID(connector_type=ConnectorTypeName.gen,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.gen_superclass): ConnectionRole.trunk,
    StemTypeUsageID(connector_type=ConnectorTypeName.gen,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.gen_subclass): ConnectionRole.branch,

    # State diagram stems
    StemTypeUsageID(connector_type=ConnectorTypeName.init_trans,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.to_init_state): ConnectionRole.free,
    StemTypeUsageID(connector_type=ConnectorTypeName.del_trans,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.from_state): ConnectionRole.free,
    StemTypeUsageID(connector_type=ConnectorTypeName.trans,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.from_state): ConnectionRole.opposing,
    StemTypeUsageID(connector_type=ConnectorTypeName.trans,
                    diagram_type=DiagramTypeName.CD, stem_type=StemTypeName.to_state): ConnectionRole.opposing,
}

