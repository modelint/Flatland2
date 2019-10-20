from canvas import Canvas


flatland_canvas = Canvas(
    diagram_type="class",
    standard_sheet_name="tabloid",
    orientation="landscape",
    drawoutput="grid_test.pdf",
    show_margin=True
)
flatland_canvas.Diagram.Grid.place_node(row=1, column=2, node_type='class', content='Aircraft')
flatland_canvas.render()
