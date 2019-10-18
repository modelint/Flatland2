"""
node.py
"""
from flatland_types import Rect_Size

class Node:
    def __init__(self, node_type, content):
        self.content = content
        self.node_type = node_type
        self.Size = Rect_Size(200, 150)  # Placeholder values
        self.Location = 0 # initializes as unknown
