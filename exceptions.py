"""
exceptions.py – Flatland specific exceptions
"""


class FlatlandException(Exception):
    pass


class SheetWidthExceededFE(FlatlandException):
    pass


class SheetHeightExceededFE(FlatlandException):
    pass


class CellOccupiedFE(FlatlandException):
    pass

