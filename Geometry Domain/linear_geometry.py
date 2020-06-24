"""
linear_geometry.py

A small library of 1D measurements that can be applied to the Canvas and Grid.
This makes it possible to apply the same type of logic to horizontal and vertical distances without
the need to differentiate between the two.

"""

scale = 2  # For float rounding errors (change to 3 or 4 if errors are visible on drawings)


def step_edge_distance(num_of_steps, extent, step):
    """
    You have a line segment with a given extent (length). In distance coordinates such as points, 0 is at the
    beginning of the segment increasing to the extent at the other end. A number line is defined with step
    increment 0 at the center of the line segment. Steps increase positively toward the extent and negatively toward
    the 0 coordinate. There is no step increment defined at either boundary (0 or the extent).

    Let's say the line segment is 100 pt long and we want 5 steps.  The zero step will be at coordinate 50.
    All negative steps will have a value less than 50 and all positive steps will be greater than 50.
    To make this work we divide the line segment into equally spaced increments by dividing the extent by the total
    number of steps plus one. With 5 steps then, we get 6 increments each 20 pt wide. There will be three on each
    side of the zero step. This means the number line will be -2, -1, 0, 1, 2 giving us our five step positions.

    Given a step number, return the distance coordinate. In our example, step 0 will return 50 pt.
    Step -1 will return 30 pt and so on. Note that no step will return either the extent or 0 pt since
    the whole idea is to avoid stepping to the edge of the line segment.

    :param num_of_steps: Line segment is divided into this number of steps
    :param extent: Length of line segment
    :param step: You want the distance of this step from the beginning of the line segment
    :return: Distance from edge of extent
    """
    # divide the face into equal size steps, 5 anchor positions = 6 steps
    stem_step_size = extent / (num_of_steps + 1)
    # add distance from center going away in either direction based on +/- anchor position
    return extent / 2 + step * stem_step_size


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
            return cell_extent/2 - node_extent/2 + boundaries[from_grid_unit - 1]
        elif axis_alignment == 0:  # left or bottom alignment
            return boundaries[from_grid_unit - 1] + from_padding
        elif axis_alignment == 2:  # right or top alignment
            return boundaries[to_grid_unit] - node_extent - to_padding
    else:
        return from_padding + boundaries[from_grid_unit -1]
