"""
test_tablet.py - Tests the tablet module
"""

from tablet import Tablet
from flatland_types import Rect_Size, Line, Position

t = Tablet(Rect_Size(width=1224,height=792))

t.Lines.append( Line(1, Position(x=10,y=10), Position(x=10,y=783)) )
t.Lines.append( Line(1, Position(x=110,y=10), Position(x=110,y=783)) )
t.Lines.append( Line(1, Position(x=210,y=10), Position(x=210,y=783)) )

t.render("tablet1.pdf")
