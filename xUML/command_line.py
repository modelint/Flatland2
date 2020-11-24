
def parse(cl_input):
    import argparse

    parser = argparse.ArgumentParser(description='Flatland model diagram generator')
    parser.add_argument('-m', '--model', action='store', default='',
                        help='Input model file name, defaults to standard input')
    parser.add_argument('-d', '--diagram', action='store', default='class',
                        help='Diagram type: class, state, collab or domain')
    parser.add_argument('-s', '--sheet', action='store', default='tabloid',
                        help='Standard sheet size such as: letter, tabloid, A1-A4')
    parser.add_argument('-o', '--orientation', action='store', default='landscape',
                        help='Landscape orientation is assumed by default')
    parser.add_argument('-f', '--file', action='store', default='',
                        help='Name of file to generate, .pdf extension automatically added, defaults to standard output')

    return parser.parse_args(cl_input)
