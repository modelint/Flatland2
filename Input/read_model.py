"""
read_model.py - Reads the model and style sheet
"""
from canvas import Canvas
from collections import namedtuple


CanvasSig = namedtuple("canvas_command", 'diagram_type presentation notation sheet_name orientation')

signature = {
    'create_canvas': None
}

style_lines = None
model_lines = None
comment_prefix = '///'


def read_files(model_fname, style_fname):
    global model_lines
    global style_lines
    # remove comments and blank lines
    fmodel = open(model_fname, 'r')
    model_lines = [l for l in fmodel.readlines() if l.strip() and l[0:3] != comment_prefix]
    fmodel.close()
    fstyle = open(style_fname, 'r')
    style_lines = fstyle.readlines()
    fstyle.close()

def canvas_command():
    for line in style_lines:
        pass
        # if pattern = assign value
        # else enter indented mode and parse each line according to header











if __name__ == "__main__":
    model_path = "../Model Markup/test1.xmm"
    style_path = "../Model Markup/test1.mss"
    read_files(model_path, style_path)
    print("Done")




