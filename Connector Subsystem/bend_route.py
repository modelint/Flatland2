"""
bend_route.py

A Bend Route is one or more corner to corner stretches in the Stem-Stem portion of a binary
or tertiary geometry Connector. Each such stretch is called a Bend. Each Bend specifies a line
through a Lane (Row or Column) at some alignment.
"""

from collections import namedtuple

Bend = namedtuple('Bend', 'lane_number direction alignment')
Bend_Route = namedtuple('Bend_Route', 'start_stem bends')
