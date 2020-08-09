"""
styledb.py
"""
from flatlanddb import FlatlandDB as fdb
from sqlalchemy import select, and_
from collections import namedtuple
# import Cocoa

# manager = Cocoa.NSFontManager.sharedFontManager()
# Fonts = set(manager.availableFontFamilies())  # To test if font is locally available

Float_RGB = namedtuple('Float_RGB', 'R G B')
Line_Style = namedtuple('Line_Style', 'pattern width color')
Text_Style = namedtuple('Text_Style', 'typeface size slant weight color leading')
Dash_Pattern = namedtuple('Dash_Pattern', 'solid blank')


class StyleDB:
    rgbF = {}  # rgb color float representation
    dash_pattern = {}
    line_style = {}
    text_style = {}
    shape_presentation = {} # asset : style (for loaded presentation)
    text_presentation = {}

    def __init__(self, drawing_type, presentation):
        load_colors()
        load_dash_patterns()
        load_line_styles()
        load_text_styles()
        load_asset_presentations(drawing_type=drawing_type, presentation=presentation)


def load_colors():
    colors = fdb.MetaData.tables['Color']
    q = select([colors])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.rgbF[i.Name] = Float_RGB(R=round(i.R / 255, 2), G=round(i.G / 255, 2), B=round(i.B / 255, 2))


def load_dash_patterns():
    patterns = fdb.MetaData.tables['Dash Pattern']
    q = select([patterns])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.dash_pattern[i.Name] = Dash_Pattern( solid=i.Solid, blank=i.Blank )


def load_text_styles():
    tstyle = fdb.MetaData.tables['Text Style']
    q = select([tstyle])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.text_style[i.Name] = Text_Style(
            typeface=i.Typeface, size=i.Size, slant=i.Slant, weight=i.Weight, color=i.Color, leading=i.Leading)


def load_line_styles():
    lstyles = fdb.MetaData.tables['Line Style']
    q = select([lstyles])
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.line_style[i.Name] = Line_Style( pattern=i.Pattern, width=i.Width, color=i.Color )


def load_asset_presentations(presentation: str, drawing_type: str):
    shape_pres = fdb.MetaData.tables['Shape Presentation']
    q = select([shape_pres.c.Asset, shape_pres.c['Line style']]).where( and_(
        shape_pres.c.Presentation == presentation, shape_pres.c['Drawing type'] == drawing_type
    ))
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.shape_presentation[i.Asset] = i['Line style']

    text_pres = fdb.MetaData.tables['Text Presentation']
    q = select([text_pres.c.Asset, text_pres.c['Text style']]).where( and_(
        text_pres.c.Presentation == presentation, text_pres.c['Drawing type'] == drawing_type
    ))
    f = fdb.Connection.execute(q).fetchall()
    for i in f:
        StyleDB.text_presentation[i.Asset] = i['Text style']
