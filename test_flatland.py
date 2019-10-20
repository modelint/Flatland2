from canvas import Canvas


flatland_canvas = Canvas(
    diagram_type="class",
    standard_sheet_name="tabloid",
    orientation="landscape",
    drawoutput="grid_test.pdf"
)
flatland_canvas.render()
