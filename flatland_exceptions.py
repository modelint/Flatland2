"""
flatland_exceptions.py – Flatland specific exceptions
"""


class FlatlandException(Exception):
    pass


class UnsupportedNotation(FlatlandException):
    pass


class UnsupportedDiagramType(FlatlandException):
    pass


class NotationUnsupportedForDiagramType(FlatlandException):
    pass


class SheetWidthExceededFE(FlatlandException):
    pass


class SheetHeightExceededFE(FlatlandException):
    pass


class CellOccupiedFE(FlatlandException):
    pass


class UnknownNodeType(FlatlandException):
    pass


class CellOutofBounds:
    pass


class NoContentForCompartment(FlatlandException):
    pass
