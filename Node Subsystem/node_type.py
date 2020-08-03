"""
node_type.py
"""

from typing import Dict
from geometry_types import Rect_Size


class NodeType:
    def __init__(self, ntype_data: Dict):
        self.Name = ntype_data['Name']
        self.About = ntype_data['About']
        self.Why_use_it = ntype_data['Why use it']
        self.Corner_rounding = ntype_data['Corner rounding']
        self.Border = ntype_data['Border']
        self.Default_size = Rect_Size(height=ntype_data['Default height'], width=ntype_data['Default width'])
        self.Max_size = Rect_Size(height=ntype_data['Max height'], width=ntype_data['Max width'])
        self.Corner_margine = ntype_data['Corner margin']

