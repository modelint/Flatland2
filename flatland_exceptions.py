"""
flatland_exceptions.py – Flatland specific exceptions
"""


class FlatlandException(Exception):
    pass


class UnknownConnectorType(FlatlandException):
    pass


class IncompatibleNodeType(FlatlandException):
    def __init__(self, node_type_name, diagram_type_name):
        self.node_type_name = node_type_name
        self.diagram_type_name = diagram_type_name

    def __str__(self):
        return f'Node Type: "{self.node_type_name}" is not defined for Diagram Type: "{self.diagram_type_name}"'


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
    def __init__(self, node_type_name):
        self.node_type_name = node_type_name

    def __str__(self):
        return f'Node Type: {self.node_type_name} is undefined for any Diagram Type'


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
