"""
connector.py

Covers the Connector class in the Flatland3 Connector Subsystem Class Diagram

Attributes
---

"""
from stem import Stem
from flatland_types import New_Stem
from typing import List


class Connector:
    """

    """

    def __init__(self, diagram, connector_type, stems: List[New_Stem]):
        self.Diagram = diagram
        self.Connector_type = connector_type
        self.Stems = [
            Stem(connector=self, stem_type=s.stem_type,
                 node=s.node, node_face=s.face, lateral_position=s.position,
                 connector_semantic=s.connector_semantic)
            for s in stems]

        # Create each Stem at min height with its associated symbols
        # Draw branch to tie them all together depending on geometry
