"""
linear_geometry.py

A small library of 1D measurements that can be applied to the Canvas and Grid.
This makes it possible to apply the same type of logic to horizontal and vertical distances without
the need to differentiate between the two.

"""

scale = 2  # For float rounding errors (change to 3 or 4 if errors are visible on drawings)


def expand_boundaries(boundaries, start_boundary, expansion):
    """Push boundaries out by exapnsion from starting boundary"""
    return boundaries[:start_boundary] + [b + expansion for b in boundaries[start_boundary:]]


def span(boundaries, from_grid_unit, to_grid_unit):
    """Returns the distance between two grid_unit"""
    assert to_grid_unit >= from_grid_unit > 0, "Grid unit number out of range"
    return boundaries[to_grid_unit] - boundaries[from_grid_unit - 1]


def align_on_axis(axis_alignment: int, boundaries, from_grid_unit, to_grid_unit, from_padding, to_padding,
                  node_extent) -> float:
    """Compute distance from from_boundary of the node edge (resulting in either a lower left x or y delta)

    Parameters
    ---
    axis_alignment: axis relative alignment of low:0, middle:1 or high:2 from vert/horiz align enums
    boundaries : an ascending list of grid boundaries on the x or y axis
    from_grid_unit : a row or column number
    to_grid_unit : a row or column number >= than the from number (must be on same axis as from_grid_unit)
    from_padding : the padding after the from bondary
    to_padding : the padding before the to boundary
    node_extent : drawn extent of the node placed in the cell without any padding
    """
    assert len(boundaries) > 1, "Empty grid"
    assert to_grid_unit >= from_grid_unit, "Grid units in wrong order?"
    assert to_padding >= 0, "Negative padding"
    assert from_padding >= 0, "Negative padding"
    assert node_extent > 0, "Missing node size"
    assert 0 <= axis_alignment <= 2

    cell_extent = boundaries[to_grid_unit] - boundaries[from_grid_unit - 1]
    leftover_space = round(cell_extent - from_padding - to_padding - node_extent, scale)
    if leftover_space:
        if axis_alignment == 1:  # middle alignment
            return round(cell_extent / 2 + boundaries[from_grid_unit - 1], scale)
        elif axis_alignment == 0:  # left or bottom alignment
            return boundaries[from_grid_unit - 1] + from_padding
        elif axis_alignment == 2:  # right or top alignment
            return boundaries[to_grid_unit] - node_extent - to_padding
    else:
        return from_padding
