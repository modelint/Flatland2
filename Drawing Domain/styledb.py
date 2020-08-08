"""
styledb.py
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from collections import namedtuple

FloatRGB = namedtuple('FloatRGB', 'R G B')
Line_Style = namedtuple('LineStyle', 'pattern width color')


class StyleDB:
    rgbF = {}  # rgb color float representation
    line_style = {}
    text_style = {}
    pres_style = { # drawing type: pres style : asset name : style
        'class diagram': { 'default': {'class': 'normal'}}



    def __init__(self):
        load_colors()
        load_patterns()
        load_line_styles()


def load_colors():
    colors = fdb.MetaData.tables['Color']
    q = select([colors])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.rgbF[i.Name] = FloatRGB( R=round(i.R/255, 2), G=round(i.G/255, 2), B=round(i.B/255, 2) )


def load_line_styles():
    lstyles = fdb.MetaData.tables['Line Style']
    q = select([lstyles])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.line_style[i.Name] = Line_Style( pattern=i.Pattern, width=i.Width, color=i.Color )


def presentation_styles():
    lstyles = fdb.MetaData.tables['Line Style']
    q = select([lstyles])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        line_style[i.Name] = Line_Style( pattern=i.Pattern, width=i.Width, color=i.Color )
