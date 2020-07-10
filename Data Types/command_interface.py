"""
command_interface.py
"""

from collections import namedtuple

New_Stem = namedtuple('New_Stem', 'stem_type semantic node face anchor')
New_Trunk_Branch = namedtuple('New_Branch', 'path graft trunk_stem leaf_stems floating_leaf_stem')
New_Offshoot_Branch = namedtuple('New_Branch', 'path graft leaf_stems floating_leaf_stem')
New_Branch_Set = namedtuple('New_Branch_Set', 'trunk_branch offshoot_branches')
New_Path = namedtuple('New_Path', 'lane rut')