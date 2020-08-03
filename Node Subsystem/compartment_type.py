"""
compartment_type.py – Specifies how a Node Type's compartment and text is drawn
"""
from geometry_types import Alignment, Padding


class CompartmentType:
    def __init__(self, name: str, alignment: Alignment, padding: Padding, text_style: str):
        self.Name = name
        self.Alignment = alignment
        self.Padding = padding
        self.Text_style = text_style

    def __repr__(self):
        return f'Name: {self.Name}, Alignment: {self.Alignment}, Padding: {self.Padding}, Text style: {self.Text_style}'