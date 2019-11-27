""" single_cell_node.py """

from node import Node


class SingleCellNode(Node):
    """
        A node enveloped by a single Cell

        Attributes
        ---
        Row : Placed in this row
        Column : Placed at this column
        """

    def __init__(self, node_type_name, content, grid, row, column, local_alignment=None):
        assert row > 0, "Negative row"
        assert column > 0, "Negative column"
        self.Row = row
        self.Column = column
        super().__init__(node_type_name, content, grid, local_alignment)



