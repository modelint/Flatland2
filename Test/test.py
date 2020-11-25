"""
flatland_test.py – This is the Flatland test driver
"""
from xUML_class_diagram import XumlClassDiagram
from pathlib import Path

# Here we map the test code to a tuple defining the model and layout file
# combination to test
tests = {
    # Binary connectors (associations)
    't001': ('aircraft2', 't001_straight_binary_horiz'),
    't002': ('aircraftpilot_compsym', 't002_straight_binary_horiz_compsym.py'),
    't020': ('aircraft2', 't020_bending_binary_horiz'),
    't023': ('aircraft2', 't023_bending_binary_twice'),
    't030': ('aircraft3', 't030_straight_binary_tertiary'),
    't031': ('aircraft3', 't031_straight_binary_tertiary_horizontal'),
    't032': ('aircraft3', 't032_1bend_tertiary_left'),
    't033': ('aircraft3', 't033_2bend_tertiary_below'),
    't034': ('aircraft3', 't034_2bend_tertiary_above'),
    't035': ('aircraft3', 't035_2bend_tertiary_right'),
    't036': ('aircraft3', 't036_2bend_tertiary_left'),
    # Tree connectors (generalization)
    't040': ('aircraft_tree1', 't040_ibranch_horiz'),
    't041': ('aircraft_tree1', 't041_ibranch_vert'),
    't050': ('aircraft_tree1', 't050_rbranch_horiz'),
    't051': ('aircraft_tree1', 't051_rbranch_vert'),
    't052': ('aircraft_tree2', 't052_rbranch_vert_corner'),
    't053': ('aircraft_tree1', 't053_p1_rbranch_vertical'),
    't054': ('aircraft_tree3', 't054_p2_gbranch_no_float'),
    't055': ('aircraft_tree4', 't055_p2_three_branch_one_graft'),
    't056': ('aircraft_tree4', 't056_p3_single_branch_graft_float'),
}

selected_test = 't001'  # The combination we are going to run

# We using the selected_test key, we compose our model and layout file names
model_file_path = (Path(__file__).parent / tests[selected_test][0]).with_suffix(".xmm")
layout_file_path = (Path(__file__).parent / tests[selected_test][1]).with_suffix(".mss")

# The diagram output will always go into this file for visual inspection
diagram_file_path = (Path(__file__).parent.parent / "Diagnostics" / "ftest").with_suffix(".pdf")

# Generate the xUML class diagram
# This is the same command that would be triggered from the command line wrapper
cd = XumlClassDiagram(
    xuml_model_path=model_file_path,
    flatland_layout_path=layout_file_path,
    diagram_file_path=diagram_file_path
)