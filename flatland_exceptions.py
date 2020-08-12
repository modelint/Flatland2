"""
flatland_exceptions.py – Flatland specific exceptions
"""


class FlatlandException(Exception):
    pass


class FlatlandDBException(FlatlandException):
    pass


class FlatlandUserInputException(FlatlandException):
    pass


class UnknownSheetGroup(FlatlandDBException):
    pass


class InvalidOrientation(FlatlandUserInputException):
    def __init__(self, orientation):
        self.orientation = orientation

    def __str__(self):
        return f'Orientation must be portrait or landscape, got: [{self.orientation}]'


class BadRowNumber(FlatlandException):
    def __init__(self, col_num):
        self.col_num = col_num

    def __str__(self):
        return f'Illegal Row number: [{col_num}]'


class BadColNumber(FlatlandException):
    def __init__(self, col_num):
        self.col_num = col_num

    def __str__(self):
        return f'Illegal Col number: [{col_num}]'


class UnknownConnectorType(FlatlandException):
    pass


class IncompatibleConnectorType(FlatlandException):
    def __init__(self, connector_type_name, diagram_type_name):
        self.connector_type_name = connector_type_name
        self.diagram_type_name = diagram_type_name

    def __str__(self):
        return f'Connector Type: "{self.connector_type_name}" is not defined for Diagram Type: "{self.diagram_type_name}"'


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
    def __init__(self, node_type_name, diagram_type_name):
        self.node_type_name = node_type_name
        self.diagram_type_name = diagram_type_name

    def __str__(self):
        return f'Node Type: {self.node_type_name} is undefined for Diagram Type: {self.diagram_type_name}'


class UnknownSheetSize(FlatlandException):
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name

    def __str__(self):
        return f'Sheet: {self.sheet_name} is not defined'


class CellOutofBounds:
    pass


class EmptyTitleCompartment(FlatlandException):
    pass


class BranchCannotBeInterpolated(FlatlandException):
    pass
